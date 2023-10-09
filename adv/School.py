class Subject:
    def __init__(self, title, teacher, topics):
        self.title = title
        self.teacher = teacher
        self.topics = topics


class Room:
    rooms = []
    
    def __init__(self, name, size, teacher):
        self.name = name
        self.size = size
        self.teacher = teacher
        self.__class__.rooms.append(self)
    
    def get_rooms(self):
        for room in self.__class__.rooms:
            print(room.name)



class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def create_subject(self, title, teacher, topics):
        self.subject = Subject(title, teacher, topics)
        self.title = title
        return self.subject
    
    def create_room(self, name, size,teacher):
        self.room = Room(name, size,teacher)
        self.name = name
        self.size = size
        self.teacher = teacher
        

# Create instances of Room
teacher = Teacher("John", 30, "Maths")
teacher2 = Teacher("Tim",43, "Physics") 
topics = ["Algebra", "Geometry", "Calculus"]
subject = teacher.create_subject("Maths", teacher, topics)
room = teacher.create_room("Maths", 20, teacher)
room2 = teacher.create_room("Physics", 20, teacher2)

roo = Room("Maths", 20, teacher)

print(roo.teacher.teacher.name)







        