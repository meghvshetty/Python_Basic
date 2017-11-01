a=input()
if int(a)%4==0:
	if int(a)%100==0:
		if int(a)%400==0:
			print('True')
		else:
			print('False')
	else:
		print('True')
else:
	print('False')
