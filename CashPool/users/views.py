from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from email_validator import validate_email, EmailNotValidError
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate, login, logout

import re
# Create your views here.

def register(request):
    if request.method == "POST":
        result = validate_registration_inputs(dict(request.POST))
        if result["status"]:
            user = User.objects.create_user(result["email"], result["email"], result["password"])
            user.save()

            print("User created")

            if request.user.is_authenticated:
                logout(request)

            login(request, user)
            print("User Logged In")

            return redirect("/")
        else:
            return render(request, "users/register.html", {"error_message": result["message"], "location": result["location"]})
    else:
        return render(request, "users/register.html", {"location": "", "error_message": ""})

def login(request):
    if request.user.is_authenticated:
        print("User already logged in")
        redirect("/")

    if request.method == "POST":
        result = validate_login_inputs(dict(request.POST))
        if result["status"]:
            user = authenticate(username=result["email"], password=result["password"])
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(request, "users/login.html",
                          {"error_message": "No user found with this login information.", "location": "email"})
        else:
            return render(request, "users/login.html", {"error_message": result["message"], "location": result["location"]})
    else:
        return render(request, "users/login.html", {"location":"", "error_message":""})

def validate_login_inputs(formInputs):
    if "email" in formInputs and "password" in formInputs:
        email = formInputs["email"][0]
        password = formInputs["password"][0]
        try:
            email = validate_email(email).email
        except EmailNotValidError as e:
            return {"status": False, "message": str(e), "location": "email"}

        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if not mat:
            return {"status": False, "message": "No account found with email and password combination.",
                "location": "password"}

    return {"status": True, "email": email, "password": password}

def validate_registration_inputs(formInputs):
    if "email" in formInputs and "password" in formInputs and "password-conf" in formInputs:
        email = formInputs["email"][0]
        password = formInputs["password"][0]
        password_conf = formInputs["password-conf"][0]

        if password != password_conf:
            return {"status":False, "message":"Passwords do not match.", "location": "password-conf"}
        try:
            email = validate_email(email).email
        except EmailNotValidError as e:
            return {"status":False, "message":str(e), "location": "email"}

        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if not mat:
            return {"status": False, "message": "Password is not valid. Please ensure all criteria are met.", "location": "password"}

        if User.objects.filter(username=email).exists():
            return {"status": False, "message": "This email has already been registered.", "location": "email"}

    return {"status": True, "email": email, "password": password}