#!/usr/bin/env python

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def speak(self):
		print("hello my name is sandeepr"+self.name)
	
p1 = Person("sandeepr",30)
print(p1.name)
p1.speak()
