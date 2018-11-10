#simple calculator using python
#this program is created by fayas midhlaj

def sum(a,b):
	c=a+b
	print c
def sub(a,b):
	c=a-b
	print c
def mul(a,b):
	c=a*b
	print c
def div(a,b):
	c=a/b
	print c
c=input('Addition=1 \t Subtraction=2 \t Multiplication=3 \t Division=4 \n Enter your choice ')
a=input('Enter first number ')
b=input('Enter second number ')
if c==1:
	sum(a,b)
elif c==2:
	sub(a,b)
elif c==3:
	mul(a,b)
elif c==4:
	div(a,b)
else:
	print 'Invalid choice'
