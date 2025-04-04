class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def info(self):
        return f"Admin(name={self.name}, password={self.password})"

class Rashid(Admin):
    def __init__(self, name, password):
        super().__init__(name, password)

rashid = Rashid("Рашид", "12345")
print(rashid.info())