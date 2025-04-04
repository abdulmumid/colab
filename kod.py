class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def info(self):
        return f"Admin(name={self.name}, password={self.password})"
