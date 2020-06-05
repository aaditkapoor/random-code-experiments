"""
	A module that schedules apscheduler to send sms every day at 8:00am
"""
import os
import random
import math
#from .model import UserModel
from twilio.rest import Client 
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

# For sending sms
 

account_sid = 'AC6266dddb895823ea68d8174f9750c24d' 
auth_token = 'b5171a3b4c0ad2aab9c4d3c9ec7f3ca5' 

# profile (keeping it generic, first will gather views then inculcate spartan eats profile)
healthy_breakfast = ["eggs", "sausages", "bacon", "waffles", "pancakes","milk", "muffins", "fruits"]
healthy_lunch = ["chicken", "pork" ,"turkey","vegetables", "fruits", "pizza", "brown rice", "cheese burger", "turkey burger", "veggie burger", "hotdog"]
healhy_dinner = ["chicken", "pork", "turkey", "vegetables", "fruits", "pizza", "burgers"]


# predefined standards

def send_sms(body, phone_number):
	client = Client(account_sid, auth_token) 
 
	message = client.messages.create( 
                              from_='+15623860858',   #number      
                              to=phone_number,
                              body=body 
    	                      ) 
 	
	print(message.sid)


def get_complete_eating_profile(name, bmi, calorie_intake, fitness_goal, activeness, weight):
	# generate a custom message with breakfast, lunch and dinner options
	message = name + ","
	if bmi[1] == "overweight":
		message = message + "Your BMI is " + str(bmi[0]) + " and it is overweight.\n "
	else:
		message = message + "Your BMI is " + str(bmi[0]) + " and it is healthy.\n"

	message = message + "For today you have to eat " + str(calorie_intake) + " Calories.\n\n"
	message = message + "With an " + activeness + " lifestyle" + " you can eat: "
	message = message + random.choice(healthy_breakfast) + "," + random.choice(healthy_lunch) + "," + random.choice(healhy_dinner)
	message = message + ".\nHope you have a nice day!\n\n"
	message = message + "Powered by HealthUp!"
	send_sms(message, "+14084313015")
	return message

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=8)
def send_sms_to_all_models():
	pass


#sched.start()