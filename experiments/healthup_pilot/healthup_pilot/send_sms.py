"""
	A module that uses twillio apis to send sms
"""
from twilio.rest import Client 
# For sending sms
 
account_sid = 'AC6266dddb895823ea68d8174f9750c24d' 
auth_token = 'b5171a3b4c0ad2aab9c4d3c9ec7f3ca5' 

def send_sms(message, phone_number):
	client = Client(account_sid, auth_token) 
 
	message = client.messages.create( 
                              from_='+15623860858',   #number      
                              to=phone_number,
                              body=body 
    	                      ) 
 	
 	print("sent sms!")
	print(message.sid)