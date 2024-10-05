from django.shortcuts import render, get_object_or_404
from .models import Book , BookUser
from .forms import UserForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required



def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)                                 #fetching a Book object from db using pk
    return render(request, 'books/book_detail.html', {'book': book})      #renders the template (book object passed as context of template)
                                                                          #accessing book details

@csrf_exempt                                                              #decorator which allows the view to accept POST requests without requiring a CSRF token
def signup(request):
    if request.method == 'POST':                                         #checking if the form was submitted using the POST method
        form = UserForm(request.POST)                                    #UserForm forms.py
        if form.is_valid():                                              #checking if form data passes all validations
            name  = form.cleaned_data['name']                            #returning a dictionary of validated form input fields and their values
            email = form.cleaned_data['email']
            pasw = form.cleaned_data['password']
            print(f" name : {name}  , email : {email} , passw : {pasw}")
            request.session['name']=name                                 #keep the user’s data accessible across different views without requiring them to log in again
        if BookUser.objects.filter(name=name).exists():                  #checks if a user with the same name already exists in the database
                messages.error(request, "You are already registered, please login!")  #error msg
        else:  #If no user with the same name exists the registration continues
            user =BookUser(name=name, email=email, password=pasw) #new BookUser instance
            user.save()                                           #saving in db
            messages.success(request, "Thanks for Registering")   #success msg
    return render(request, 'books/signup.html')              


@csrf_exempt
def user_login(request):
    if request.method == 'POST':                                     #checking if the form was submitted using the POST method
        name = request.POST.get('name')                              #retrieving the name from form data
        passw = request.POST.get('password')                         ##retrieving the password from form data
        print(f" name : {name}  , passw : {passw}")
        #finding user with same name and password
        try:
            user = BookUser.objects.get(name=name, password=passw)     #trying to get the BookUser from the database
            request.session['username'] = name                         #If the user is found, the username is stored in the session so that the user is recognized across different views
            return redirect('Home')
        #no matching user is found, this block handles the exception
        except BookUser.DoesNotExist:
            messages.error(request, "Invalid username or password, please try again!")    
    return render(request, 'books/login.html')

@login_required
def home(request):
    name =  request.session.get('name')                                #retrieving the value of 'name' stored in the session during the login or signup process
    if name:                                                           #Checks if the name exists in the session 
        user = BookUser.objects.get(name=name)           #If the name exists, this line fetches the BookUser object from the database using the name
        return render(request,'books/home.html', {'user':user})
        
    return render(request,'books/home.html')


@login_required
def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('bookname')       #retrieves the value of the bookname field from the form data
        author = request.POST.get('author')       #retrieves the value of the author field from the form data
        descrp = request.POST.get('description')  #retrieves the value of the description field from the form data
        price = request.POST.get('price')         #retrieves the value of the price field from the form data
        Pb = request.POST.get('publishedDate')    #retrieves the value of the published date field from the form data
        print(f"name : {name} , author : {author} , descrp : {descrp} , price : {price} ")
        #ensuring all req fields are filled by the user
        if name and author and price and Pb:
            try:
                #creating the Book object
                book = Book(
                    title=name,
                    author=author,
                    description=descrp,
                    price=float(price),
                    published_date=Pb
                )
                #saving the book to the db
                book.save()
                messages.success(request, "Book added successfully.")
                return redirect('Home') 
            #If there’s any error while saving the book
            except Exception as e:
                print(f"Error occurred: {e}")  
                messages.error(request, "An error occurred while adding the book.")
        else:
            messages.error(request, "Please fill in all required fields.")
    return render(request, 'books/add_book.html')  


@login_required
def delete_book(request):
    if request.method == "POST":
         book_title=request.POST.get('title')              #retrieving the title of the book from the form data
         Book.objects.filter(title=book_title).delete()    #filters books with given book title and then deletes it
         messages.success(request, f'Book "{book_title}" has been deleted successfully.')
    return render(request,'books/delete_book.html')

def book_list(request):
    books=Book.objects.all()                                #gives list of all the books in db
    return render(request,'book.html',{"books": books})

def logout(request):
    #trying to delete the session
    try:
        del request.session
    #if there is an issue with deleting the session
    except:
        return HttpResponse("Error")
    return render(request, 'books/logout.html' )

