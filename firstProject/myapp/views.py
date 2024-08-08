# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from django.contrib.auth import logout


# Define a view function for the home page
def home(request):
    return render(request, "home.html")


# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        print("phone_number is:", phone_number)
        print("password is:", password)

        try:
            # Check if a user with the provided phone number exists
            find_user = Student.objects.get(phone_number=phone_number)
            print("user name according to find_user is:", find_user)
            data = {"username": find_user.username, "contact": find_user.phone_number}
            # Manually verify the password
            if find_user.password == password:
                # Log in the user by setting the session or any other method you prefer
                request.session["user_id"] = find_user.id
                return render(request, "home.html", data)
            else:
                print("inside invalid password")
                # Display an error message if authentication fails (invalid password)
                messages.error(request, "Invalid Password")
                return redirect("/login/")
        except Student.DoesNotExist:
            print("inside user not found")
            # Display an error message if the username does not exist
            messages.error(request, "Invalid Username")
            return redirect("/login/")

    # Render the login page template (GET request)
    return render(request, "login.html")


# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")

        print("user_name:", user_name)
        print("password:", password)
        print("phone_number:", phone_number)

        # Check if a user with the provided phone number already exists
        if Student.objects.filter(phone_number=phone_number).exists():
            # Display an information message if the username is taken
            messages.info(request, "Phone number already taken!")
            return redirect("/register/")

        # Create a new Student object with the provided information
        user = Student.objects.create(
            username=user_name,
            phone_number=phone_number,
            password=password,  # Store the password as plain text
        )

        print("user object is:", user)

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect("/login/")

    # Render the registration page template (GET request)
    return render(request, "register.html")


def logout(request):
    return redirect('/login/')
