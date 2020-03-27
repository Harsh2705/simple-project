class student():
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
	def display(self):
		print("name is:", self.name)
		print("rollno is:",self.rollno)
class test(student):
	def __init__(self,name,rollno,marks1,marks2):
		self.marks1=marks1
		self.marks2=marks2
		student.__init__(self,name,rollno)
	def getdata(self):
		print("marks of sub1 is:",self.marks1)
		print("marks of sub2 is:",self.marks2)

obj=test("lalu",12,34,55)
obj.display()
obj.getdata()