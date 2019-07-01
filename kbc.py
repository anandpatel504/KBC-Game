
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",150)
engine.setProperty("volume",2)

print("-------------- Welcome to the KBC game -------------")
print()
engine.say("Welcome to the KBC game!")
engine.runAndWait()

question_list=["(1)Which animal is known as the ship of the desert?","(2)How many consonant are there in the English alphabet","(3)Which planet is known as the red planet?","(4)Which is the following is not a metal:gold,resin,glass?","(5)Which country does Volleyball originate from?","(6)During which year did world war 1st begin?","(7)Which first electrical item did Thomas Edison invent?","(8)How many players are there in an Volleyball team?","(9)How many days are there in a year?","(10)How many colours are there in a rainbow?"]
first_option=["1 horse","1 21","1 shani","1 resin","1 India","1 1920","1 Train engin","1 eight","1 366","1 7"]
second_option=["2 camel","2 23","2 Varun","2 gold","2 the USA","2 1915","2 Light bulb","2 four","2 365","2 9"]
third_option=["3 lion","3 20","3 mars","3 glass","3 england","3 1914","3 fan","3 seven","3 360","3 8"]
fourth_option=["4 tiger","4 26","4 sun","4 silver","4 australia","4 1916","4 watch","4 six","4 368","4 10"]
#all_options=[first_option,second_option,third_option,fourth_option]
ans_key=[2,1,3,1,2,3,2,4,2,1]
amount=[20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
index=0

ans_list=[]
while index<len(question_list):
	if index%5==0 and index!=0:
		print("congrats!aapka pehla padaav pura ho gaya hai")
		engine.say("congrats!aapka pehla padaav pura ho gaya hai")
		engine.runAndWait()
		print()

	print(question_list[index],len(question_list[index]))
	engine.say(question_list[index],len(question_list[index]))
	engine.runAndWait()
	print()

	print(first_option[index])
	engine.say(first_option[index])
	engine.runAndWait()
	print()

	print(second_option[index])
	engine.say(second_option[index])
	engine.runAndWait()
	print()

	print(third_option[index])
	engine.say(third_option[index])
	engine.runAndWait()
	print()

	print(fourth_option[index])
	engine.say(fourth_option[index])
	engine.runAndWait()
	print()
	# print(ans_key[a])
	engine.say("input your option number-")
	engine.runAndWait()
	ans=input("input your option number-")

	if int(ans)==ans_key[index]:
		print("congrates! aapka answer sahi hai aap",amount[index],"rupaye jeet gaye")
		engine.say("congrates! aapka answer sahi hai aap"+str(amount[index])+"rupaye jeet gaye")
		engine.runAndWait()
		print()

	else:
		print("aapka answer galat hai")
		engine.say("aapka answer galat hai")
		engine.runAndWait()
		print()
		break
	ans_list.append(ans)
	index = index+1
else:
	print("Congrates! aap ek coror(10000000)rupaye jeet gaye hai")
	engine.say("Congrates! aap ek coror(10000000)rupaye jeet gaye hai")
	engine.runAndWait()

print("Total your right answer keys",ans_list)
engine.say("Total your right answer keys",ans_list)
engine.runAndWait()
