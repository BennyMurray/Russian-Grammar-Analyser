# -*- coding: UTF-8 -*-

import sys  
import json
reload(sys)  
from flask import Flask, jsonify,request,render_template
from translator import analyseGrammar
sys.setdefaultencoding('utf-8')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('computer.html')



@app.route('/_add_numbers')
def add_numbers():
	user_input = request.args.get('a')
	list = []
	dict = analyseGrammar(user_input.lstrip(' '))
	list.append(dict)
	#b = getTranslation(a)
	return jsonify(result=list)


	
	

if __name__ == '__main__':
    app.run(debug=True)