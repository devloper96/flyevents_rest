from flask import Flask
from flask import request
import random
import string
import requests
from exotel import Exotel

app = Flask(__name__)

@app.route('/hello')
def hello():
	return "hello"
@app.route('/mobileConfirmation')
def sendsms():
	phoneno = request.args.get('phoneno')
	print(phoneno)
	code = id_generator()	
	print(code)

	#url = 'https://punchitio:2771852343d707d6673d077656c1e27bf857a32e@twilix.exotel.in/v1/Accounts/punchitio/Sms/send'
	#data = '{"query":{"bool":{"must":[From:"07930256894",To:"'+phoneno+'",Body="'+code+'"]}'
	client = Exotel('punchitio','2771852343d707d6673d077656c1e27bf857a32e')
	client.sms('07930256894',phoneno,code)
	print("sms")
 	return code

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))	
if __name__ == '__main__':
	app.run(host='0.0.0.0')