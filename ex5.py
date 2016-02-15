# -*- coding: utf-8 -*-

my_name = 'Stuming'
my_age = 22 # not a lie
my_height = 175 # centimeters
my_weight = 55 # kilograms
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let’s talk about %s." % my_name)
print("He’s %d cm tall. Equal to %d inches." % (my_height, my_height / 2.54))
print("He’s %d kg heavy. Equal to %d pounds." % (my_weight, my_weight / 0.45))
print("Actually that’s not heavy.")
print("He’s got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight))