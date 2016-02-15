# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print(formatter % (1,2,3,4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)
)

print("-" *10)
print(formatter % ("one", 2, False, 10/2))