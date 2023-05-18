from random import shuffle
def shuffle_list(mylist):
	shuffle(mylist)
	return mylist
def player_guess():
	guess = ''
	while guess not in [0,1,2]:
		guess = int(input('Pick up a number between 0 ,1 or 2'))
	return guess	 	
def check_guess(mylist,guess):
	if mylist[guess] == 'O':
		print('Correct!')
	else:
		print('Wrong guess!')
		print(mylist)
mylist = ['','O','']
mixedlist = shuffle_list(mylist)				
guess = player_guess()
check_guess(mixedlist,guess)