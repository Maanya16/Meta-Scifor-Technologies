from django.db import models  #imports the 'models' module from django database library

#BookUser model is designed to store information about users, including their name, email, and password.
class BookUser(models.Model):                        #model class which is a table in db models.Model means that the BookUser will have all the functionality Django provide for a model.
    name = models.CharField(max_length=100)          #field in BookUser model (textfield) 
    email = models.EmailField(unique=True)           #special field in BookUser model used to store emails ('unique=true' is a constraint meaning no two users can have the same email address)
    password = models.CharField(max_length=128)      #another field for storing password in string in BookUser model

    def __str__(self):                               
         return self.name

#Book model is designed to store information about books, including the title, author, description, price, and publication date.    
class Book(models.Model):                            #model class which is another table in db
    title = models.CharField(max_length=200)         #text field in Book model
    author = models.CharField(max_length=200)        #text field in Book model
    description = models.TextField()                 #text field used for storing large amount of text
    price = models.DecimalField(max_digits=6, decimal_places=2)      #decimal field used for storing decimal values
    published_date = models.DateField()                              #date field used to store the date when the book got published

    def __str__(self):
        return self.title
