""" Stage 2: Make Your Own Quiz """
# The followings are the big picture of the game quiz which consists of questions, answers, and blanks.

# questions base on 3 levels
easy_quiz = ("The number of states in the United States is", "The capital city of the United States is", "The current current president of the United States is", "The largest state in the United States is")
medium_quiz = ("The number of countries in Southeast Asia is", "The capital city of Malaysia is", "The capital city of Thailand is", "The capital city of Indonesia is")
hard_quiz = ("The largest country in the world is", "Panda is the national animal for", "Andean condor is the national animal for", "Steppe eagle is the national animal for")

# answers 
easy_answers = ('50', 'Washington DC', 'Obama', 'Alaska')
medium_answers = ('11', 'Kuala Lumpur', 'Bangkok', 'Jakarta')
hard_answers = ('Russia', 'China', 'Colombia', 'Egypt')

# blanks
blanks = ("__1__", "__2__", "__3__", "__4__")

""" Greet user """
# input: user's name.
# output: greeting sentence with user's name in it.

def greeting (user_name) :
	print "\nWelcome to my quiz!" + user_name + ". The purpose of the game is to fill in the blanks for the quiz chose by you. Please be noted that you only have 3 chances for the whole game quiz. Use it wisely! "

""" Match up levels, questions, and answers """
# input: user's level of choice.
# output: questions of user's choice and answers that match with that specific question.

def game_entrance (level) :

	if level == "easy":
		print "\nGreat! Let's start!\n"
		return easy_answers, easy_quiz

	elif level == "medium":
		print "\nGreat! Let's start!\n"
		return medium_answers, medium_quiz

	elif level == "hard":
		print "\nGreat! Let's start!\n"
		return hard_answers, hard_quiz

""" Construct game structure and answer assessment """
# input: user's answer.
# output: number of attempts they are getting for the whole game quiz, etc.

def answer_quiz (answers, quizzes, blanks) :
	index, tries, count = 0, 0, 1
	total_blanks = 4
	while index < total_blanks:
		user_guess = raw_input("\nPlease enter your answer for" + " " + blanks[index]+ " ")
		if user_guess == answers[index] :
			print str (quizzes[index]) + "  " + user_guess.upper() + "." + " You are right!"
			correct_ans = 4
			if count < correct_ans:
				print quizzes[count] + "  " + blanks[count]
			count += 1
			index += 1
		else:
			max_attempts = 3
			tries = tries + 1 
			if tries > max_attempts:
				exit ()

""" Proper structure and output for the correct answer """
# input: correct answer
# output: "Thank you for playing"

def complete (answers, quizzes) :
	print ""
	sentence = quizzes[0] + " " + answers[0] + "." + " " + quizzes[1] + " " +answers[1] + "." + " " + quizzes[2] + " " + answers[2] + "." + " " + quizzes[3] + " " + answers[3] + "."
	print sentence
	end_statement = "\nGreat Job! Thank you for playing!\n"
	print end_statement
	
""" Game quiz execution """

# start out by greeting user 
# input: none
# output: the entire game quiz

def play_game():
	user_name = raw_input ("Hello! How may I address you? ")
	greeting (user_name)

# ask user their preferred level	
	level = raw_input ("\nPlease select a level: easy/ medium/ hard ")
# assign quiz base on user's selected level
# assess answer
	if level in ["easy", "medium", "hard"]:		
		answers, quizzes = game_entrance (level)
		print quizzes[0] + " " + blanks[0] + "." + " " + quizzes[1] + " " + blanks[1] + "." + " " + quizzes[2] + " " + blanks[2] + "." + " " + quizzes[3] + " " + blanks[3] + "."
		answer_quiz (answers, quizzes, blanks) 

	else:
		print "Let's try again!"
		play_game()

play_game()
