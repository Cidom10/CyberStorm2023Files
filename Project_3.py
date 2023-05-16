#######################################################################################################################
# Group Members: Reese Seals, Ben Meister, Trisha Carter, Calvin Idom, Samman Regmi, Michael Herbert, Cameron McCarthy
#######################################################################################################################

from ftplib import FTP
import os
import sys


METHOD = 7

def ftp():
	# FTP server details
	IP = "138.47.99.64"
	PORT = 21
	USER = "anonymous"
	PASSWORD = ""
	FOLDER = "/7/"
	USE_PASSIVE = True # set to False if the connection times out

	# connect and login to the FTP server
	ftp = FTP()
	ftp.connect(IP, PORT)
	ftp.login(USER, PASSWORD)
	ftp.set_pasv(USE_PASSIVE)

	# navigate to the specified directory and list files
	ftp.cwd(FOLDER)
	files = []
	ftp.dir(files.append)

	# exit the FTP server
	ftp.quit()
	return files




def decoder(status):
	binary = ""
	for c in status:
		if(c == "-"):
			binary += "0"
		else:
			binary += "1"
	return binary



def decode7(status):
	binary = decoder(status)
	if(binary[0:3] == "000"):
		return chr(int(binary, 2))
	return ""
		


def decode10(string):
	counter = 0
	bits = ""
	msg = ""
	for n in string:
		bits += n
		counter = (counter % 7) + 1
		if(counter == 7):
			#print(f'Binary7: {bits}', end=" ")
			msg += str(chr(int(bits, 2)))
			#print(msg)
			bits = ""
	return msg



def main(method):
	files = ftp()

	if(method == 7):
		msg = ""
		for f in files:
			data = f.split(' ')
			msg += decode7(data[0])
		print(msg)
	elif(method == 10):
		string = ""
		for f in files:
			data = f.split(' ')
			string += data[0]
		binary = decoder(string)
		msg = decode10(binary)
		print(msg)
	else:
		print("Not an accepted bit length. Please try again...")
		main()

main(METHOD)