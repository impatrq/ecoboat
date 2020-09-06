from time import time, sleep

inicio= time()
while True:
	final= time()
	if int(final- inicio)%1==0 and int(final- inicio)!=0:
		print("1")
	if int(final- inicio)%2==0 and int(final- inicio)!=0:
		print("2")
	if int(final- inicio)%3==0 and int(final- inicio)!=0:
		print("3")
	if int(final- inicio)%4==0 and int(final- inicio)!=0:
		print("4")
		break