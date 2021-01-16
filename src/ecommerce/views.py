from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title":"Hello World",
        "content" : "Welcome to Home Page"
    }

    if request.user.is_authenticated():
        context["premium_content"] = "YEJAAAAAAAAAAAAAA"


    return render(request,"home_page.html", context)

def about_page(request):
    context = {
        "title" : "About Page",
        "content" : "Welcome to About Page"
    }
    return render(request,"home_page.html", context)

def contact_page(request):
    contact_form= ContactForm(request.POST or None)

    context ={
        "title" : "Contact Page",
        "content" : "Welcome to Contact Page",
        "form"  : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    """if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    """
    return render(request, "contact/view.html", context)

def login_page(request):
    login_form=LoginForm(request.POST or None)
    context = {
        "form" : login_form
    }
    print("User logged in")
    print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
        context['form']=LoginForm()
        username=login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")
    return render(request,"auth/login.html", context)

User=get_user_model()

def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context={
        "form" : register_form
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        new_user=User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)


def home_page_old(request):
    html_= """
        <!doctype html>
        <html lang="en">
            <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

                <title>Hello, world!</title>
            </head>
            <body>
                <h1>Hello, world with Bootstrap Code! </h1>

                <!-- Optional JavaScript -->
                <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            </body>
        </html>
      """

    #return HttpResponse('<h1>Hello World</h1>')
    return HttpResponse(html_)
