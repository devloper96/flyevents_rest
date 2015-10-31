from flask import Flask
from flask import request
import random
import string
from twilio.rest import TwilioRestClient

app = Flask(__name__)

@app.route('/hello')
def hello():
	return "hello"
@app.route('/mobileConfirmation')
def sendsms():
	phoneno = "+91"+request.args.get('phoneno')
	print(phoneno)
	code = id_generator()	
	print(code)
	ACCOUNT_SID = "AC5a8cd025e6a9a49c91a60d8b57fded16" 
	AUTH_TOKEN = "409ee4348b706cfd238cdafc423943ae" 
 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
	client.messages.create(to=phoneno, from_="+16504926725", body=code)
	print("sms")
 	return code

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))	
if __name__ == '__main__':
	app.run(host='0.0.0.0')