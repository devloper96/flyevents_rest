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

@app.route('/getImage')
def getImage():
	tu="www.google.com"
	url = "http://api.page2images.com/restfullink?p2i_url=www.google.com&p2i_key=6658882a4001ef71&p2i_screen=1024x768&p2i_device=6&p2i_size=512x384"
	data = requests.get(url)
	print(data.content)
	return data.content

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))	
if __name__ == '__main__':
	app.run(host='0.0.0.0')
