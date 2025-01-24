class Rectangle:
    def __init__(self):
        self.width=20
        self.height=40

    def calc_area(self):
        return self.height *self.width

room_1=Rectangle()
room_1.width=32
room_1.height=45
print("The area of the room is :",room_1.calc_area())            
