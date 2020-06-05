from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import UserModel
from .calculate_cal_mass import *
from .day_sender import *

def home(request):
	return render_to_response("index.html")

def register(request):
	return render_to_response("register.html")

def about(request):
	return render_to_response("about.html")

def setup_diet(request):

	# get the data
	name = request.GET.get("name","")
	email = request.GET.get("email","")
	age = request.GET.get("age","")
	number = request.GET.get("mobile_number","")
	weight = request.GET.get("weight","")
	sex = request.GET.get("sex","")
	height = request.GET.get("height", "")
	fitness_goal = request.GET.get("fitness_goal","")
	activeness = request.GET.get("activeness","")

	# apply formula to get bmi and daily calorie intake, save it in a variable 
	# save everything into a model
	# get a message variable in the model for the function to get a personalized message
	# setup apscheduler to start the clock at 8:00am

	bmi = return_body_mass_index_and_find_status(weight, height)
	calorie_to_take = calorie_intake(sex, bmi, activeness,weight)

	# complete eating profile
	UserModel.objects.create()

	message = get_complete_eating_profile(name, bmi, calorie_to_take, fitness_goal, activeness, weight)
	# save model here and show thank you.html
	return render_to_response("thank_you.html")