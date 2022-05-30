from django.shortcuts import render
 
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "Login.html")

def shop(request):
    return render(request, "Shop.html")

def about(request):
    return render(request, "AboutUs.html")

def contact(request):
    return render(request, "Contacts.html")
