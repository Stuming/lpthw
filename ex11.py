# -*- coding: utf-8 -*-

print("How old are you?"),
#age = raw_input() # 在python3里不可用
age = input()
print("How tall are you?"),
height = input()
print("How much do you weigh?"),
weight = input()

print("So, you're %r old, %r tall and %r high." % (
    age, height, weight))