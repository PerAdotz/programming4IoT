class Student:
    def __init__(self,name,surname, birthYear , bachelor , master):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear
        # self.age = 2024 - self.birthYear
        # self.studentFile = open('student.txt' , 'w')
        self.bachelor = bachelor
        self.master = master
        self.gradesList = []
        self.avgGrade = 0
    

    def show(self):
        print(f"Hi, i'm {self.name} {self.surname}")

    def age(self):
        print(f"Age: {2024 - self.birthYear}")

    def save(self):
        f = open('student.txt' , 'w')
        f.write(f'{self.name},{self.surname},{2024 - self.birthYear}')
        f.close()

    def isBachelor(self):
        if self.bachelor == "Y":
            self.bachelor = True
            print(f"{self.name} {self.surname} is a Bachelor student")
        else:
            self.bachelor = False
            print(f"{self.name} {self.surname} is not a Bachelor student")

    def isMaster(self):
        if self.master == "Y":
            self.master = True
            print(f"{self.name} {self.surname} is a Master student")
        else:
            self.master = False
            print(f"{self.name} {self.surname} is not a Master student")

    def readGrades(self):
        f = open('studentVotes.txt','r').read()
        self.gradesList = f.split(',')
        self.gradesList = [int(i) for i in self.gradesList]
    
    def averageGrades(self):
        if len(self.gradesList) > 0:
            self.avgGrade = sum(self.gradesList)/len(self.gradesList)
            print(f"Avg grade: {self.avgGrade}")
        else:
            print(f"No grades")
        

    def minGrade(self):
        if len(self.gradesList) > 0:
            self.minGrade = min(self.gradesList)
            print(f"Min grade: {self.minGrade}")
        else:
            print(f"No grades")
        
    
    def maxGrade(self):
        if len(self.gradesList) > 0:
            self.maxGrade = max(self.gradesList)
            print(f"Max grade: {self.maxGrade}")
        else:
            print(f"No grades")

    def asDictionary(self):
        d = {
            "nome": self.name,
            "surname" : self.surname,
            "birthYear" : self.birthYear,
            "grades": self.gradesList
            }
        print(d)



if __name__ == "__main__":
    name = input("Please write your name ")
    surname = input("Please write your surname ")
    birthYear = int(input("Please write your birth Year "))
    bachelor = input("Is the student enrolled on a bachelr degree?(Y/N) ")
    master = input("Is the student enrolled on a master degree?(Y/N) ")
    studentA = Student(name,surname , birthYear , bachelor , master)
    studentA.show()
    studentA.age()
    studentA.save()
    studentA.isBachelor()
    studentA.isMaster()
    studentA.readGrades()
    studentA.averageGrades()
    studentA.minGrade()
    studentA.maxGrade()
    studentA.asDictionary()

