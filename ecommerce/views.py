from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from ecommerce.forms import ContactForm, LoginForm, RegistrationForm


def home_page(request):
    context = {
        "title": "Home page",
        "content": "Welcome to the home page"
    }
    template_name = "home_page.html"
    return render(request, template_name, context)


def about_page(request):
    context = {
        "title": "About page",
        "content": "Welcome to the about page"
    }
    template_name = "home_page.html"
    return render(request, template_name, context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    context = {
        "title": "Contact page",
        "form": contact_form
    }
    template_name = "contact/view.html"
    return render(request, template_name, context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form,
        "title": "Login Form"
    }

    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            print(request.user)
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            # No backend authenticated the credentials
            print("Error")

    template_name = "auth/login.html"
    return render(request, template_name, context)


User = get_user_model()
def registration_page(request):
    registration_form = RegistrationForm(request.POST or None)
    context = {
        "form": registration_form,
        "title": "Registration Form"
    }
    if registration_form.is_valid():
        print(registration_form.cleaned_data)
        username = registration_form.cleaned_data.get("username")
        email = registration_form.cleaned_data.get("email")
        password = registration_form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        context['form'] = RegistrationForm()

    template_name = "auth/registration.html"
    return render(request, template_name, context)
