#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = " ".join([str[str.find("object-oriented"): str.find("object-oriented") + len("object-oriented")], str[str.find("programming"): str.find("programming") + len("programming")], str[str.find("with"): str.find("with") + len("with")], str[str.find("Python"): str.find("Python") + len("Python")]])
print(str)
