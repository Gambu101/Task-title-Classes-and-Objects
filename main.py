class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks,score):
        self.change_name = name
        self.change_age = age
        self.add_track = tracks
        self.get_score = score



# Bob = Student("Bob", 26, ["FE","BE"],20.90)
Bob = Student ("Peter",34,"UI/UX",20.90)
# Expected methods
print(Bob.change_name)
print(Bob.change_age)
print(Bob.add_track)
print(Bob.get_score)
