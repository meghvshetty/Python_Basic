a=input('Enter The Year : ')
if int(a)%4==0:
	if int(a)%100==0:
		if int(a)%400==0:
			print('True')
			
		else:
			print('False')
			import webbrowser
			for f in range(2):
					webbrowser.open('https://www.timeanddate.com/date/leapyear.html')
					send='Sending your data....'
			print(send)
	else:
		print('True')
		
else:
	print('False')
	import webbrowser
	for f in range(2):
			webbrowser.open('https://www.timeanddate.com/date/leapyear.html')
			send='Sending your data....'
	print(send)