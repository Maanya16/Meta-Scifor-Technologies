#A palindrome is a word, number, phrase, or other sequence of characters that reads the same backward as forward, such as madam or racecar. Arunima got a new puppy (pet) and
#she wants to decide the name for her pet. The name of the pet should be a palindrome. Write a program to take the pet name as input and print "true" if it is palindrome or
#print "false" on screen. Help Arunima to decide the name ( should be palindrome ) of the puppy. Hint: reverse the name and compare it with the original name.

pet_name = input("Enter the name of the pet: ")
reverse_name = pet_name[::-1]
if pet_name == reverse_name:
    print("True")
    print("Arunima can name her pet",pet_name,"because its a palindrome name")
else:
    print("False")
    print("Arunima cannot name her pet",pet_name,"because its not palindrome name")

#Aarush and Yash are two friends in the same grade and they decided to create their secret language to communicate with each other. First of all, they decided to reverse each
#word. For example: come here = "emoc ereh". But this was very easy to understand for other students. They tried to make it a bit difficult and decided to put all the characters
#which are at odd indices first then all the characters which are at even indices. For example: come here = "oecm eehr". Write a program in python to create such type of secret
#language and convert the word Codeyoung into secret language using the same program.

word=input("Enter the word:")
reverse_word= word[::-1]
print("Reversed word:",reverse_word)
odd_chars = reverse_word[1::2]
even_chars = reverse_word[0::2]
print("Word after getting reversed and then putting odd indices first then all the characters which are at even indices after:",odd_chars+even_chars)



#Vishal is creating a form and he wants to take the contact number as input. However, some people do not enter the number properly. Vishal is confused about how to verify
#whether the given number is in the correct format or not. To help Vishal write a python program to show how we can verify whether a given phone number is valid or not. ● Note:
#A valid phone number contains 10 digits with 9,8 or 7 as the first digit. Phone number only contains numbers and not any character. ● Hint: ● User len() function to verify the
#number of digits. ● Use isnumeric() function to check it only contains numeric values.Use indexing to check whether the first character is 9,8 or 7 or not.

contact_number=input("Enter the contact number:")
if len(contact_number)==10 and contact_number[0] in ['9','8','7'] and contact_number.isnumeric():
    print("Valid Number")
else:
    print("Invalid Number")