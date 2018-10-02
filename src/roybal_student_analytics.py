#Monte Roybal
#Dr. Richard Medina
#Software Engineering
#Student Analytics Class

import json

class Student_Analytics():
	
	def __init__(self,data=[]):
		"""Constructor Method"""
		self.data = data
		self.load_data("/home/monte/Desktop/CS_551/cs451-551-analytics-engine/data/grade-data.json")

	def __str__(self):
		"""Print Method"""
		return ("Average final grade over the entire database is {} \nAverage change in grade from midterm to final is {}, {} to {} \nA count of each final grade (E.g., #A's, #B's, etc.) {},{},{},{},{} \nTotal number of female students is {} \nTotal number of male students is {}".format(s.classify_grade(s.avg_grade(3)),s.grade_change(),s.classify_grade(s.avg_grade(2)),s.classify_grade(s.avg_grade(3)),s.element_count(3,"A"),s.element_count(3,"B"),s.element_count(3,"C"),s.element_count(3,"D"),s.element_count(3,"F"),s.element_count(1,"F"),s.element_count(1,"M")))

	def load_data(self,fname):
		"""Load the json file"""
		file_obj = open(fname)
		self.data = json.loads(file_obj.read())
		file_obj.close()

	def classify_grade(self,grade_val):
		"""Return a grade classification from a given grade value"""
		if grade_val >= 5.00:
			return "A+"
		elif grade_val > 4.7:
			return "A-"
		elif grade_val > 4.3:
			return "B+"
		elif grade_val >= 4.0:
			return "B"
		elif grade_val > 3.7:
			return "B-"
		elif grade_val > 3.3:
			return "C+"
		elif grade_val >= 3.0:
			return "C"
		elif grade_val > 2.7:
			return "C-"
		elif grade_val >1.7:
			return "D"
		else:
			return "F"

	def element_count(self,pos,query):
		"""Return a total number of elements from a given query and data position"""
		total_count = 0
		for i in self.data:
			if i[pos] == query:
				total_count+=1
		return total_count

	def avg_grade(self,pos):
		"""Return the average grade value from a given data position"""
		total_count = len(self.data) 
		total_val = 0
		total_val = (self.element_count(pos,"A")*5+self.element_count(pos,"B")*4+self.element_count(pos,"C")*3+self.element_count(pos,"D")*2+self.element_count(pos,"F")) 
		return (total_val/total_count)

	def grade_change(self):
		"""Return the average change in grade value from midterm to final grades"""
		final_val = self.avg_grade(3)
		mid_val = self.avg_grade(2)
		return (final_val-mid_val)


if __name__ == '__main__':
    s = Student_Analytics()
    print (s)