# Python program to demonstrate writing to CSV


import csv
	
fields = ['Name', 'Branch', 'Year', 'CGPA']
	
# data rows of csv file
rows = [ ['Ruchi', 'COE', '2', '9.0'],
		['Mohit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Ashfak', 'SE', '1', '9.5'],
		['Manik', 'MCE', '3', '7.8'],
		['Rajvir', 'EP', '2', '9.1']]
	
# name of csv file
filename = "university_records.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(rows)
