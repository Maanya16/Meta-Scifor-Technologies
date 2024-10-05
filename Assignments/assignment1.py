#Arvind just started learning python and he is very interested to know how he can print his name on the screen using python. Write a program to print Arvind on the screen.
#Print your name and age as well using a python print statement.

print("Name:Arvind\nAge:20")

#Sahil challenged Chirag to print the names of his friend in different lines using a single print statement. Sahil thought that this would be impossible to do. To help Chirag
#write a python program to print the names of your five friends in five different lines using a single print statement

print("My 5 friends are:\nMaanya\nMeena\nPankaj\nErica\nJai")

#A teacher told students to write an essay on themselves. Nidhi created a python program that can generate an essay just by taking inputs. She shared the program with her
#friends to help them. Write a python program that can take inputs like name, age, address, etc, and convert it into an essay.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
school_name = input("Enter your school name: ")
hobbies=input("Enter your hobbies: ")
aim=input("Enter your aim: ")
print(f"My name is {name}. I am {age} years old. I live in {address}. My school name is {school_name}. My hobbies are {hobbies}. My aim is {aim}.")


#Rakshita wants to create a simple chatbot using python language. Write a program in python to help Rakshita in creating the chatbot. ● Hint: with the help of variables store
#the answers of the user and use it for further conversation by the chatbot. ● Example : ● >> ● Hi, I am a chatbot. What is your name? ● >>Nidhi ● Oh, Nidhi in which grade you
#are right now? ● >>8 ● Nidhi you are in 8th grade. Can I ask you one question? yes or no? ● >>yes ● Tell me 1024+98=? ● >>1122 ● Good! Your answer is correct. Bye ● >>bye

print("Hi, I am a chatbot. What is your name?")
name=input()
print("Oh,",name,"in which grade you are right now?")
grade=int(input())
print(name, "you are in", grade,"grade. Can I ask you one question?")
choice=input("yes or no?")
if choice=="yes":
    print("Tell me 1024+98=?")
    ask=input()
    if ask =="1122":
        print("Good! Your answer is correct. Bye")
    else:
        print("Your answer is incorrect.You need more practice.")
else:
    print("Bye")
    

#Himanshu sells notebooks. Sometimes it becomes a bit difficult for him to calculate the total amount to charge from the customer. To help Himanshu create a program that asks
#the user to enter the number of books to buy and then print the amount to be paid. ● Hint: Assume the cost of one notebook - $2

books=int(input("Enter the number of books to buy:"))
amount=books*2
print("The amount to be paid is:",amount,"$")


#Shubh is excited to do something mathematical in python. He decided to create a program that could add, subtract, multiply and divide two numbers. To help Shubh write a python
#program to apply addition, subtraction, multiplication, and division between two numbers.

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("Addition of given numbers are:",num1+num2)
print("Subtraction of given numbers are:",num1-num2)
print("Multiplication of given numbers are:",num1*num2)
print("Division of given numbers are:",num1/num2)

#Rakshita wants to calculate her age. So she subtracted her year of birth from the current year. Her classmates also wanted to find their age in the same way. So she decides to
#write a python program where students can input their year of birth, then the program will print their age. Write the same program to find your age and help your classmates
#in finding their age.

present_year=2024
year_of_birth=int(input("Enter your year of birth:"))
age=present_year-year_of_birth
print("Your age is:",age)
