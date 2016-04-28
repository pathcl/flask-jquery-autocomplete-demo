from flask import Flask, render_template, request, redirect, jsonify, \
    url_for
import random
import string
import logging
import json
import httplib2
import requests
from flask import make_response


app = Flask(__name__)


# Autocomplete method - called from Jinja template
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
	search = request.args.get('q')
	results = [{'value': 'MIR:00000466', 'label': 'WormBase RNAi'}, \
		{'value': 'MIR:00000031', 'label': 'Wormpep'}, {'value': 'MIR:00000186', 'label': 'Xenbase'}, \
		{'value': 'MIR:00000111', 'label': 'Resource 1'}, {'value': 'MIR:00000222', 'label': 'Resource 2'}, \
		{'value': 'MIR:00000333', 'label': 'Resource 3'}, {'value': 'MIR:00000444', 'label': 'Resource 4'}, \
		{'value': 'MIR:00000555', 'label': 'Resource 5'}, {'value': 'MIR:00000666', 'label': 'Resource 6'}]
	return jsonify(matching_results=results)
	#results = ["car", "carriage", "horse", "dog"]
	#return jsonify(matching_results=results)


# Route to home page
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def show_home():
	return render_template('index.html')


# Main Method
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
