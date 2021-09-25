class Student:
	avg=0
	def __init__(self,rollno,name,marks):
		self.rollno=rollno
		self.name=name
		self.marks=marks

	def display(self):
		print(self.name)
		print(self.rollno)
		print(self.marks)
		print(self.avg)

	def average(self):
		self.avg=self.marks/400*100

person1 = Student(190010,"Ashfak",85)
person2 = Student(190011,"Ruchi",83)
person3 = Student(190012,"Riya",0)

person1.average()
person2.average()
person3.average()

person1.display()
person2.display()
person3.display()