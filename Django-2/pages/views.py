from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function-based vs Class-based
# takes in an HTTP request and returns an HTTP response

#context concept: used to create python dictionary to pass variable into the front end of app or site




# homepage
def home(request):
    #return HttpResponse("<h1>Home Page</h1>") 
#have to use a render function which is a different language
    context = {"page_name": "Home Page",
               "title": "Home"}
    return render(request, 'pages/home.html', context)

# about us
def about(request):
    #return HttpResponse("<h1>About us Page</h1>")
    context = {"page_name": "About Us Page",
               "title": "About"}
    return render(request, 'pages/about.html')


# contact us
def contact(request):
    #return HttpResponse("<h1>Contact us Page</h1>")
    {"page_name": "Contact Us Page",
               "title": "Contact"}
    return render(request, 'pages/contact.html') #rendering full html file


# services
def services(request):
    #return HttpResponse("<h1>Services Page</h1>")
    {"page_name": "Our Services Page",
               "title": "Services"}
    return render(request, 'pages/services.html')
