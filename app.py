"""Original local-only Compose teaching app. Flask/redis own the HTTP/Redis protocol."""
import os
from datetime import datetime, timezone
from flask import Flask, jsonify, redirect, render_template, request
import redis

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8192
store = redis.Redis(host='store', port=6379, decode_responses=True,
                    socket_connect_timeout=2, socket_timeout=2)

@app.errorhandler(redis.RedisError)
def unavailable(error):
    return render_template('unavailable.html'), 503

@app.get('/health')
def health():
    store.ping()
    return jsonify(status='ok', storage='redis')

@app.get('/api/notes')
def notes():
    return jsonify(notes=[{'id': k, 'text': v} for k, v in sorted(store.hgetall('notes').items())])

@app.get('/')
def index():
    return render_template('index.html', notes=sorted(store.hgetall('notes').items()),
                           instance=os.environ.get('HOSTNAME', 'unknown'))

@app.post('/notes')
def add():
    # This is a local single-user exercise, not a multi-user production service.
    if request.host.split(':')[0] not in {'localhost', '127.0.0.1'}:
        return '仅允许本机访问', 403
    text = request.form.get('text', '').strip()
    if not 1 <= len(text) <= 120:
        return '请填写1至120字的便签', 400
    with store.pipeline(transaction=True) as tx:
        number = store.incr('next_note')
        tx.hset('notes', str(number).zfill(6), text)
        tx.execute()
    return redirect('/', 303)
