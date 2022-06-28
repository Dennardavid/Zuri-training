class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
    
    #change name method 
    def change_name(self,name):
        self.name = name
    
    #change age method
    def change_age(self,age):
        self.age = int(age)
    
    #change track method
    def add_track(self,tracks):
        self.tracks = tracks
    
    #get score method
    def get_score(self):
        return self.score

 
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected method
Bob.change_name("Peter")
print(Bob.name)

Bob.change_age(34)
print(Bob.age)

Bob.add_track("UI/UX")
print(Bob.tracks)

print(Bob.get_score())