#Aarush recently learned probability in his school. He was finding the probability of different events and he wondered whether he can develop a program to do the same thing
#or not. To help Aarush create a program in python where user can enter number of favorable outcomes and total number of possible outcomes and then program will print the
#probability of that event on the screen. ● Note: ● Print the probability of the event only up to 2 decimal places. ( For this use round() function ) ● Sample run ● >>Enter
#the number of favorable outcomes: 1 ● >>Enter the total number of possible outcomes: 2 ● >>Probability: 0.5

favourable_outcomes=int(input("Enter the number of favourable coutcomes:"))
total_number_of_outcomes=int(input("Enter the total number of outcomes:"))
probability=round(favourable_outcomes/total_number_of_outcomes,2)
print("The probability of the event is:",probability)

#The RTO (Regional Transport Office) website holds a registration form which is responsible for registering a user for a Driving License. The RTO wants to take the next step
#if and only if the user's age is greater than or equal to 18.So write a program in python to help the RTO find out whether the registered user's age is greater than or
#equal to 18 or not.

print("********Welcome to RTO Official Website********")
name=input("Enter name:")
age=int(input("Enter age:"))
if(age>=18):
  print("You are eligible.\Lets move for further procedures.")

else:
  print("Sorry, You are not eligible.")
  
  #:Scarlet, a fifteen year old, wants to be creative and is inspired by watching alexa, siri, google on how they act as smart chatbots and assistants and wanted to create her
#own chatbot. So write a program in python using the if-else, Nested if-else, if-else-if ladder where ever necessary.The Bot Has the Behave in following manner
#Step 1: ask the user for his/her name.
#Step 2: wish the user by telling his name For Ex: Hi My name is Jenni, chatbot. A Very Good Day To You username!!.
#Step 3: How are you feeling today??(Based on what user entered you are suppose to respond if user entered good statement then say something positive like."It's really a
#productive day to do something innovative and you are close to it. "If the user says something negative then respond accordingly and try to cheer him up.Don't worry!! you
#got this username!!. buckle up and cheer yourself up. Good days are on their way

print("Hello, can i know your name?")
name=input()
if(name=="no"):
 print("Okay, have a good day.")
else:
  print("Hi, my name is Jenni, chatbot. A very good day to you",name)
  print("How are you feeling today?")
  feeling=input()
  if(feeling=="sad"):
    print("Don't worry! You got this",name,"!!. Buckle up and cheer yourself up. Good days are on their way.")
    songs=input("Should i suggest you some good songs?")
    if(songs=="yes"):
      print("Song 1\nSong 2\nSong 3\nSong 4\nSong 5\nSong 6\nSong 7")
    else:
      print("Okay. I am open for you. You can ask anything to me anytime.")
  elif(feeling=="happy"):
    print("It's really a productive day to do something innovative and you are close to it.")
    print("Do you want to see some skills that you can add in your life?:")
    skill=input()
    if(skill=="yes"):
      print("1.Reasoning\n2.Programming\3.Communication skills\n4.Aptitude\n5.Critical Thinking\n6.Flexibility")
    else:
      print("Okay. I am open for you. You can ask anything to me anytime.")
  elif(feeling=="emotional"):
    print("It’s completely normal to feel emotional! Emotions are a natural part of being human. If you’re feeling overwhelmed, consider talking to someone you trust or practicing" )
    print("self-care. Sometimes, a good cry, deep breaths, or engaging in activities you enjoy can help. Remember, you’re not alone, and it’s okay to seek support when needed.🌟")
    print("I am open for you. You can ask anything to me anytime.")
    
    #atm question
account_number=123456789
atm_pin=70093
bank_balance=50000
print("******Welcome to SBI******")
print("MENU\n1.Withdrawl\n2.Cash Deposit\n3.Balance Enquiry\n4.Fast Cash")
user_choice= int(input("Enter the choice:"))
if(user_choice==1):
  withdraw_amount=int(input("Enter the amount you want to withdraw:"))
  if(withdraw_amount>bank_balance):
    print("Insufficient bank balance.")
  elif(withdraw_amount%100 != 0):
    print("Please enter the money which is multiple of 100")
  else:
    print("Cash withdrawled successfully.")
    bank_balance=bank_balance-withdraw_amount
    check_balance= input("Do you want to check your remaining balance:")
    if(check_balance=="yes"):
      print(bank_balance)
    else:
      print("Thankyou for visiting. Visit again.")

elif(user_choice==2):
  deposit_cash=int(input("Enter the amount to be deposited:"))
  print("Money deposited.")
  bank_balance=bank_balance+deposit_cash
  check= input("Do you want to check your remaining balance:")
  if(check=="yes"):
    print(bank_balance)
  else:
    print("Thankyou for visiting. Visit again.")

elif(user_choice==3):
  print("Your current balance is:",bank_balance)

else:
  print("Fast Cash\n1.5000\n2.10000\n3.15000")
  fast_cash_choice=int(input("Enter the fast cash option:"))
  if(fast_cash_choice==1):
    print("5000 withdrawed from your account")
    bank_balance=bank_balance-5000
    print("Remaning balance:",bank_balance)
  elif(fast_cash_choice==2):
    print("10000 withdrawed from your account")
    bank_balance=bank_balance-10000
    print("Remaning balance:",bank_balance)
  else:
    print("15000 withdrawed from your account")
    bank_balance=bank_balance-15000
    print("Remaning balance:",bank_balance)
    
#Jack, a 19 year old, has learnt python. He has written a code using python that will literally accept color names as an input from the user and prints all of the colors.
#Jack is still thinking of a logic and whenever the color is red hence he wrote a if condition inside a for loop but the compiler started throwing an error stating that if
#condition cannot be left empty.So write a python program to help Jack to keep his if condition empty temporarily and print rest of the colors using a for loop
colours=[]
while True:
  colour=input("Enter the colour:")
  if colour=="stop":
    break
  colours.append(colour)

for colour in colours:
  if(colour=="red"):
    pass
  else:
    print(colour)
    

#Nidhi's father is not able to calculate his annual tax correctly. He is a bit confused with the taxation rule also each year his total annual income is different. So to help
#her father Nidhi decides to write a python program that can calculate the tax to be paid based on annual income. Write the same program to calculate the tax to be paid
#based on annual income. ● Hint: take the annual income as input from the user and print the amount of tax to be paid. These are tax rules.

annual_income=int(input("Enter your annual income:"))
if annual_income<=250000:
  print("No tax.")
elif annual_income<=500000:
  print("Tax to be paid:",(annual_income-250000)*0.05)
elif annual_income<=1000000:
  print("Tax to be paid:",(250000*0.05)+(annual_income-500000)*0.20)
else:
  print("Tax to be paid:",(250000*0.05)+(500000*0.20)+(annual_income-1000000)*0.30)

#Shubham is worried about his health. He keeps checking his height and weight daily. Recently he came to know about the BMI report, and now he wants to calculate his own BMI by writing a python program. Write a program in python to check your BMI by putting your height and weight as input. ● Note: ● Body Mass Index is a simple calculation
#using a person's height and weight. The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in meters squared. A BMI of 25.0 or more is
#overweight, while the healthy range is 18.5 to 24.9. BMI applies to most adults 18-65 years.

height=float(input("Enter the height in meter squared:"))
weight=float(input("Enter the weight in kgs:"))
bmi=weight/height
print(bmi)
if(bmi>=25.0):
  print("Over weight.")
elif(bmi>=18.5 and bmi<=24.9):
  print("Healthy")
else:
  print("Consult doctor because BMI is very low.")
  
#A year consists of 365 days. But once in every four years, it consists of 366 days. And that is known as a leap year. Shisha wants to know whether the current year is a
#leap year or not. She found that any year divisible by 4 is a leap year, if the year is divisible by 100 then it will not be a leap year, and if the year is divisible by
#400 then it will be a leap year. Write a program in python to check whether the given year is a leap year or not to help Shisha. ● Hint: Use if elif else condition

year=int(input("Enter the yaer:"))
if(year%4==0 and year%100 !=0):
  print("Given year is a leap year.")
elif(year%100==0 and year%400==0):
  print("Given year is a leap year.")
else:
  print("Given year is not a leap year.")
