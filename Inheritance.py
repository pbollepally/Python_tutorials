class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent contructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name " +self.last_name)
        print("Eye color " +self.eye_color)

class Child(Parent):
    def __init__(self,last_name, eye_color, no_of_toys):
        print("Child contructor called")
        Parent.__init__(self,last_name, eye_color)
        self.no_of_toys =no_of_toys

    def show_info(self):
        print("Last name " + self.last_name)
        print("Eye color " + self.eye_color)
        print("Eye color " +str(self.no_of_toys))

billy = Parent("1cyrus","blue")
#print(billy.last_name)
#print(billy.eye_color)

miley = Child("2cyrus","brown",6)

#billy.show_info()
miley.show_info()
#print(miley.last_name)
#print(miley.eye_color)
#print(miley.no_of_toys)



