number = 23
flag = True
while flag:
        guess = int(raw_input('Enter an Integer : '))
        if guess == number:
                print 'Your guess is right'
                flag = False
        elif guess < number: 
                print 'A lil bit higher'
        else: 
                  print 'wtf'
else: 
        print 'The while loop is done'
        #lol
print 'Done!'

