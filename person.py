class Person():

    def __init__(self, first_name, last_name, age, sex: bool, ssn):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex # TRUE for MALE , FALSE FEMALE
        self.SSN = ssn

    # ----- MUTATOR METHODS -----

    def change_first_name(self, new_name):
        self.first_name = new_name

    def update_last_name(self, new_last):
        self.last_name = new_last

    def update_age(self, new_age):
        self.age = new_age

    def birthday(self):
        self.update_age(self.age + 1)

    def transition(self):
        self.sex = not self.sex

    # ----- ACCESSOR METHODS -----

    def display_sex(self):
        if self.sex:
            return "Male"
        else:
            return "Female"

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return f"{self.get_first_name()} {self.get_last_name()}"
    
    def get_age(self):
        return f"{self.age}"
    
    def get_ssn(self):
        return f"{self.SSN}"

    def get_info(self):

        return (f"Name: {self.get_first_name()} {self.get_first_name()}\n Age: {self.age}\nSex: {(self.display_sex())[:1]}\nSNN: ***-**-{self.SNN % 10000}")