class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.language_spoken = ["Urhobo", "English", "Magyar"]

    def display_attributes(self):
        print(self.last_name, self.first_name, self.language_spoken)

class Trainer(Person):

    def __init__(self, salary, fname = "", lname = "", age = 6):
        super(Trainer, self).__init__(fname, lname, age)
        self.salary = salary

class Spartan(Person):

    def __init__(self, part_time_job):
        self.part_time_job = part_time_job

person_one = Person("Javier", "Martinez Romero", 22)
trainer_one = Trainer("£2")
trainer_two = Trainer("£3","Jane", "Doe", 57)
spartan_one = Spartan(False)

