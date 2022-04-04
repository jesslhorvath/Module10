class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        gpa_char = set("1234567890.")
        if not (name_char.issuperset(lname) and name_char.issuperset(fname) and name_char.issuperset(major)):
            raise ValueError
        if not (isinstance(gpa, float) and 0 <= gpa <= 4.00):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
