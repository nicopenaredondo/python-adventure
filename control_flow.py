number = 23
guess = int(raw_input('Enter an Integer : '))

if guess == number:
	print 'Your guess is right'
elif guess < number: 
	print 'A lil bit higher'
else: 
	print 'wtf'

print 'Done!'