from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Menu, Food, Contact, Order, OrderItem, Coupon
# Create your views here.
def index(request):
    menus = Menu.objects.all()
    foods = Food.objects.all()
    
    context = {
        "menus": menus,
        "foods": foods
    }
    return render(request,"home/index.html", context)
def login(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(email=email).first()
        print(user)
        if user is not None:
            if user.check_password(password):
                print("User is authenticated")
                return render(request, "home/index.html")
            else:
                print("User is not authenticated")
                return render(request, "home/login.html")

    return render(request, "home/login.html")
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        print(email)
        print(password)
        print(confirm_password)
        
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print("User created")
            return render(request, "home/index.html")
        else:
            print("Password and confirm password do not match")
            return render(request, "home/register.html")
    return render(request, "home/register.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name)
    return render(request, "home/contact.html")
def menu(request):
    menus = Menu.objects.all()
    foods = Food.objects.all()

    context = {
        "menus": menus,
        "foods": foods
    }
    return render(request, "home/menu.html", context)
def about(request):
    return render(request, "home/about.html")