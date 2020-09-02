# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:36:16 2020

@author: Venkat
"""


# Define your functions
#general message to print
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

#to get size of drink user wants
def get_size():
  res=input('What size of drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n')
  if res.lower() == "a":
    return "small"
  elif res.lower() == "b":
    return "Medium"
  elif res.lower() =="c":
    return "Large"
  else: 
    print_message()
    return get_size()


#Function to get drink type from user
def get_drink_type():
  res=input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n')
  if res.lower() == "a":
    return "Brewed Coffee"
  elif res.lower() == "b":
    return "Mocha"
  elif res.lower() =="c":
    return "latte with " + get_milk_type()
  else: 
    print_message()
    return get_drink_type()

#Function to get kind of milk from user
def get_milk_type():
  res=input('And What kind of milk would you like? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy Milk \n')
  if res.lower() == "a":
    return "2% milk"
  elif res.lower() == "b":
    return "Non-fat milk"
  elif res.lower() =="c":
    return "Soy milk"
  else: 
    print_message()
    return get_milk_type()


# Call coffee_bot()!
def coffee_bot():
  print("Welcome to the Cafe!")
  size = get_size()
  drinkType = get_drink_type()
  
  print("Alright, that\'s a {} {}!.".format(size,drinkType))
  name = input("Can I get your name?\n")
  print("Thanks,{}! Your drink will be ready shortly".format(name))

#print("Welcome to the Cafe!")
coffee_bot()
