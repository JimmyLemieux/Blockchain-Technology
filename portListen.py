#!/usr/bin/python
import hashlib
from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
	print 'hey there'

while __name__ == '__main__':
	app.run(debug=True)