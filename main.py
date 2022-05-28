class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name= str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        #pass
    print("New Students details below:")

    def change_name(self, new_name):
        self.name = new_name
        print('My name is', self.name)
        #return self.name

    def change_age(self, new_age):
        self.newage = new_age
        print('And my age is', self.newage)
        #return self.age

    def add_track(self, new_tracks):
        self.tracks.append(new_tracks)
        print('I am offering tracks', self.tracks)
        #return self.tracks

    def get_score(self):
        print('The score i got is', self.score)
        #return new_score

        pass

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

        
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

#print(Bob.change_name)
#print(Bob.change_age)
#print(Bob.add_track)
#print(Bob.get_score)
