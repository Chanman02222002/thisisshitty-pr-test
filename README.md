from __future__ import annotations
from flask import Flask, jsonify, request
from services import TRIGGERS, run_all_calls, run_trigger

def create_app() -> Flask:
    app = Flask(__name__)
    @app.get('/')
    def index():
        return jsonify({'name':'AIAPITEST PR + tracking fixture','mock_only':True,'production_call_sites':len(TRIGGERS),'trigger_all':'POST /trigger-all','trigger_one':'POST /trigger/<name>','available':list(TRIGGERS)})
    @app.get('/health')
    def health(): return jsonify({'ok':True})
    @app.post('/trigger/<name>')
    def trigger_one(name: str):
        try: result = run_trigger(name)
        except ValueError as exc: return jsonify({'ok':False,'error':str(exc)}), 404
        return jsonify({'ok':True,'trigger':name,'result':result})
    @app.post('/trigger-all')
    def trigger_all():
        try: repeat = int(request.args.get('repeat','1'))
        except ValueError: return jsonify({'ok':False,'error':'repeat must be an integer'}), 400
        if repeat < 1 or repeat > 25: return jsonify({'ok':False,'error':'repeat must be between 1 and 25'}), 400
        runs = [run_all_calls() for _ in range(repeat)]
        return jsonify({'ok':True,'repeat':repeat,'calls_per_run':len(TRIGGERS),'expected_tracking_events':repeat*len(TRIGGERS),'runs':runs})
    return app

app = create_app()
if __name__ == '__main__': app.run(host='127.0.0.1', port=5000, debug=False)
