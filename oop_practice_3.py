# create a class with a class attribute a; create an object from
#  it and set a directly using object a = 0. Does the change the class attribute  NO

class Sample:
    a ="abhishek"#here a is class attribute

obj =Sample()
obj.a="vikky"#here a is instance attribute 

print(Sample.a)

print(obj.a)

