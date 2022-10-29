class DataUser:

    def __init__(self, first_name, last_name, email, age, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.salary = salary
        self.department = department

    def get_set_full_info(self):
        list_info = [self.first_name, self.last_name, self.email, str(self.age), str(self.salary), self.department]
        return list_info
