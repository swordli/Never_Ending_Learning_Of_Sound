import os

def populate():
	with open("static/downloaded_files/downloaded_files.csv", "r") as userfile:
		count = 0
		for line in userfile:
			terms = line.split(",")
			terms[0] = terms[0].lower()
			objects = terms[0].split(" ")
			object1 = objects[0]
			#print objects				
			for i in objects:
				if (i!=object1):
					object1 = object1 + "-" + i

			#print object1
			terms[1] = terms[1].lower()
			category = terms[1].split(" ")
			category1 = category[0]
			for i in category:
				if (i!=category1):
					category1 = category1 + "-" + i

			print category1
			count = count+1
			if(count>100):
				break
	
	
populate()
