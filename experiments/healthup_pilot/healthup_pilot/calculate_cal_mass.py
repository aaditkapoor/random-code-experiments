"""w
	A module that calculates body mass and suggests calories in a day for a subject
"""

import os
import sys
import math
import random


"""
		for females = 10 x (Weight in kg) + 6.25 x (Height in cm) - 5 x age - 161; for males= 10 x (Weight in kg) + 6.25 x (Height in cm) - 5 x age + 5
"""

def convert_lb_to_kg(lb):
	 return (lb / 2.2)


def calorie_intake(sex, bmi, activeness,weight):
	# directions taken from: https://diabetesstrong.com/how-to-find-your-daily-calorie-need/
	bmi = bmi[0]
	lean_factor = None
	calories = None
	weight = convert_lb_to_kg(float(weight))
	if sex == "male" or sex == "Male" or sex == "M" or sex == "m":
		weight = weight * 1
		if bmi >= 10 and bmi <=14:
			lean_factor = 1.0
		elif bmi  >= 15 and bmi <= 20:
			lean_factor = 0.95
		elif bmi >= 21 and bmi <= 28:
			lean_factor = 0.90
		elif bmi > 28:
			lean_factor = 0.85
		else:
			weight = weight * 0.9
	else:
		weight = weight * 0.9
		if bmi >= 14 and bmi <=18:
			lean_factor = 1.0
		elif bmi  >= 19 and bmi <= 28:
			lean_factor = 0.95
		elif bmi >= 29 and bmi <= 38:
			lean_factor = 0.90
		elif bmi > 38:
			lean_factor = 0.85

	bmr = weight * 24 * lean_factor # bmr

	if activeness == "active":
		calories = bmr * 1.65
	elif activeness == "very active":
		calories = bmr * 1.80
	else:
		calories = bmr * 1.3



	return round(calories) # final calories to eat	

def return_body_mass_index_and_find_status(weight, height):
	height = float(height) * 0.01 # in metres
	bmi = float(convert_lb_to_kg(float(weight))) / (height * height)
	if bmi >= 25:
		return [round(bmi),"overweight"]
	else :
		return [round(bmi), "healthy"]

