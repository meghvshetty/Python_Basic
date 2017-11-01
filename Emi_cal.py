print ('Welcome To Smart Emi')

OR=input('Enter Your On-Road Amount of your Bike:-') #On-Road amount input
DP=input('Enter Your DownPaymet Amount:-') #Down Paymet input
RI=input('Enter the  Rate of Intrest:-') #intrest rate input
LP=input('Enter the Loan Period in months:-') #loan period input 
a=int(OR)-int(DP) # to get the remaining loan amount
b=int(a)/100*float(RI) #to get the intrest rate amount 
c=int(a)+int(b) #Adding loan amount and the intrest rate amount
d=c/int(LP) #dividing the amount for per month
print ('Emi for your Bike', d)
#IP=int(b)-int(OR)
print (b)
