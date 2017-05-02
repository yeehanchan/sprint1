from server import app
from flask import request, render_template, make_response
from server.module.transcribe import transcribe,read_data,parse_request
import json

transcript = []

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/trans', methods=['GET','POST'])
def render_transcription():
	json = request.get_json()
	return transcribe(json)