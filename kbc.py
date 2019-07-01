import random, pyttsx3, pprint
engine = pyttsx3.init() # Gets a reference to an engine instance that will use the given driver.
engine.setProperty('rate', 150) # Integer speech rate in words per minute. Defaults to 200 word per minute.
engine.setProperty('volume', 2) # To increase the volume of the speaker.

question_list = [
	"How many continents are there in the world?",  	# first question
	"What is the capital of France?",			# second question
	"Gateway of India is located in which city?",		# third question
	"Which is the largest populated country in the world?" 	# fourth question
]
options_list = [
	# options for first question
	["Four", "Nine", "Seven", "Eight"],
	# options for second question
	["New York", "Beijing", "Paris", "Delhi"],
	# options for third question
	["Delhi", "Mumbai", "Lucknow", "Kolkata"],
	# options for fourth question
	["China", "Australia", "India", "Afghanistan"]
]

solution_list = [3, 3, 2, 1] # solution option list.

price_list = [1000, 2000, 3000, 5000] # price list that user would win.
price_list_speak = ['one-thousand', 'two-thousand', 'three thousand', 'five-thousand']
total_earned_balance = 0 # to print the final balance that user have won when the game ends.

question_couter = ['first', 'second', 'third'] # to print which number of question, the user is appearing for.
fifty_fifty_checker = 0 # to check whether the user has already used his 50-50 lifeline or not.
count = 0 # to print all the questions while iterating a while loop over it.

print ('\n>>>>>>>>> ** Welcome to KBC ** <<<<<<<<<')
engine.say('Welcome to KBC')
engine.runAndWait()

while count < len(question_list):
	if fifty_fifty_checker == 0:
		
		print ('**You can use 5050 lifeline by giving 5050 in the user input**')
		engine.say('You can use 50 50 lifeline by giving 50 50 in the user input')
		engine.runAndWait()
	print ('\n')
	ninja = 0 # it is used to iterate loop while incrementing it to print all the options for a particular question.
	hatori = 0 # it is used to give the serial number to the two questions after 50-50 lifeline.

	if count == len(question_list)-1:
		print ('Your last question is: ')
		engine.say('Your last question is')
		engine.runAndWait()
	else:
		print ('Your ' + question_couter[count] + ' question is: ')
		engine.say('Your ' + question_couter[count] + ' question is')
		engine.runAndWait()

	print ('Ques', str(count+1) + '.',question_list[count]) # asking the question while iterating loop over it.
	engine.say(question_list[count])
	engine.runAndWait()

	while ninja < len(options_list[count]):

		print (str(ninja+1) + '.',options_list[count][ninja])
		engine.say(options_list[count][ninja])
		engine.runAndWait()
		ninja+=1

	engine.say('Enter your option number')
	engine.runAndWait()
	user = (input('Enter your option number: ')) # taking user input in option number.

	# checking if the user input is right.
	if user == 'quit' or user == 'q' or user == 'exit': # if the user wants to quit the match.

		print ('Thanks for playing\n ')
		engine.say('Thanks for playing')
		engine.runAndWait()
		break

	if int(user) == solution_list[count]:

		print ("You're correct!\n")
		print ("**Congratulations! You've won Rs.", str(price_list[count]) + '**')

		engine.say('You are correct')
		engine.say("Congratulations! You've won " + price_list_speak[count] + 'Rupees')
		engine.runAndWait()

		total_earned_balance = str(price_list[count]) # taking the last price in this variable to show the last earned money.

	# checking if user wants 50-50 lifeline, the first time.
	elif user == "5050":
		if fifty_fifty_checker == 0:

			print ("Your two options are: \n")
			engine.say("Your two options are")
			engine.runAndWait()

		if fifty_fifty_checker == 0:
			fifty_fifty_checker += 1 
			randomansindex = random.randint(0, 2) # randomly generating a wrong answer index.
			rightansindex = (solution_list[count]-1) # correct answer index.

			if rightansindex == randomansindex: # checking if both the indices are matching to random it again.
				while True: 					# iterating while loop over it.
					randomansindex = random.randint(0, 3)
					if rightansindex != randomansindex:
						break

			checkit = [randomansindex, rightansindex] # saving the wrong answer index and right answer index in a list.
			random.shuffle(checkit) # shuffling the two options list indices.
			
			checkinglist = []
			for checkitindex in range(len(checkit)):

				engine.say(options_list[count][checkit[checkitindex]])
				engine.runAndWait()

				print (checkitindex+1,'.',options_list[count][checkit[checkitindex]])

				checkinglist.append(options_list[count][checkit[checkitindex]]) # appending the wrong and right answer in a list.

			indexlist = [hatori+1, hatori+2] # for serial number for the two options in 50-50 lifeline.
			ansdata = checkinglist 
			
			againuser = (input('Enter your option number: ')) # again taking user input to select one option from two options.
			engine.say('Enter your option number')
			engine.runAndWait()

			data = int(againuser)-1
			correctchoice = options_list[count].index(ansdata[data])+1

			if correctchoice == solution_list[count]: # checking the given index of by the user(acc. to solution_list) with the solution list indices.
				
				print ('You are right!')
				engine.say('You are right')

				print ("**Congratulations! You've won Rs.", str(price_list[count]) + '**')
				engine.say("Congratulations! You've won " + price_list_speak[count] + "Rupees")

				engine.runAndWait()

				total_earned_balance = str(price_list[count]) 

			else:
				print ('You are wrong\nYou have lost the match!') # if the user has still given the wrong input using this lifeline.
				engine.say('You are wrong and You have lost the match!')
				engine.runAndWait()
				break

		elif fifty_fifty_checker > 0 and user == "5050": # if the user has already used his/her lifeline.
			print ('\nYou have already used this lifeline')
			engine.say('Sorry! You have already used this lifeline')
			engine.runAndWait()
			count-=1

	# if the user-input would be wrong, the user will lost the match.
	else:
		print ('You are wrong\nYou have lost the match!')
		engine.say('You are wrong and You have lost the match!')
		engine.runAndWait()
		break
	count+=1
print ('**Your total earned Money is Rs.', total_earned_balance + '**') # printing the last earned money by the user during the game. 
engine.say('Your total earned Money is Rs.', total_earned_balance)