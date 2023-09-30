import datetime
import os

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Welcome to voicy!!!\n\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("Error: could not create file " + filename)

def append_data(filename, person, text):
	try:	
		with open(filename, 'a') as f:
			f.write(datetime.date.today().strftime("%d/%m/%Y"))
			f.write(" ")
			f.write(datetime.datetime.now().strftime("%H:%M:%S"))
			f.write(" : ")
			f.write(person)
			f.write(" -> ")
			f.write(text)
			f.write("\n")
	except IOError:
		print("Error: could not append to file " + filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " cleared successfully.")
	
    except IOError:
        print("Error: could not clear file " + filename)