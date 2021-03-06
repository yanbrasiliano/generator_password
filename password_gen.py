from random import choice
import string
from time import sleep
#import os

"""

Created by: Yan Brasiliano Silva Penalva
Objective: Generate strong, random automatic passwords.

string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~

Version 1.0: First scope of the algorithm, without improvements or lean code. 
Version 2.0: Adding some functions to clean up the code. 

"""

def wait():
	sleep(1)
	print('.')

while True:
	print()
	print('\t	GENERATOR STARS v1.0')
	print('-'*60)
	print('''	[ 1 ]  Password with all characters.\n
	[ 2 ]  Password with letters and numbers.\n
	[ 3 ]  Password only with letters[UPPER and LOWER].\n
	[ 4 ]  Password only with numbers.\n
	[ 5 ]  Password with letters and special characters.\n
	[ 6 ]  Password with numbers and special characters.''')
	print('-'*60)
	choose = int(input('Option: '))
	while choose > 6:
		print('Invalided option, try again.')
		choose = int(input('Option: '))
	
	size = int(input('Enter the password size: '))
	while size <= 5:
			print('Easy password to break, recommended: 6 or more characters.')
			size = int(input('Enter the password size: '))
	if choose == 1:
			v= string.ascii_letters + string.digits + string.punctuation
			password =' '
			for i in range (size):
				password+=choice(v)
			#os.system('clear')
			print('Option 1 selected.')
			print('Generating password...')
			wait()
			print(f'Password generated:{password}')
			print()
	if choose == 2: 
			v= string.ascii_letters + string.digits
			password =' '
			for i in range (size):
				password+=choice(v)
			#os.system('clear')
			print('Option 2 selected.')
			print('Generating password...')
			wait()
			print()
			print(f'Password generated:{password}')
			print()
	if choose == 3:
			v= string.ascii_letters 
			password =' '
			for i in range (size):
				password+=choice(v)
			#os.system('clear')
			print('Option 3 selected.')
			print('Generating password...')
			wait()
			print(f'Password generated:{password}')
			print()
	if choose == 4:
			v=string.digits
			password =' '
			for i in range (size):
				password+=choice(v)
			#os.system('clear')
			print('Option 4 selected.')
			print('Generating password...')
			wait()
			wait()
			wait()
			print()
			print(f'Password generated:{password}')
			print()
	if choose == 5:
			v= string.digits + string.punctuation
			password =' '
			for i in range (size):
				password+=choice(v)
			#os.system('clear')
			print('Option 5 selected.')
			print('Generating password...')
			wait()
			wait()
			wait()
			print()
			print(f'Password generated:{password}')
			print()
	if choose == 6:
			v= string.ascii_letters  + string.punctuation
			password =' '
			for i in range (size):
				password+=choice(v)
			#os.system('clear')
			print('Option 6 selected.')
			print('Generating password...')
			wait()
			wait()
			wait()
			print()
			print(f'Password generated:{password}')
			print()
	while True:
			resp = str(input('GENERATE MORE PASSWORDS?[Y/N]: ')).upper().split()[0]
			if resp in 'YN':
					#os.system('clear')
					break
			print('ERROR! ANSWER ONLY Y or N!')
	if resp == 'N':
				break
	#os.system('clear')
	print('Thanks for using GENERATOR STARS.')
	print()
	print()


