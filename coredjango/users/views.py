from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import RegistratrionForm , UserAuthenticationForm

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email  = form.cleaned_data.get("form")
            raw_password  = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=password1)
            login(request, account)
            return redirect("admin")

        else:
            context["registration_form"] = form

    else:
        form = RegistratrionForm()
        context["registration_form"]  = form
    return render(request, "users/register.html", context)

def logout_view(request):
    logoupt(request)
    return redirect("admin")

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email = email, password = password)

            if user:
                login(request, user)
                return redirect("home")
    else:
        form = UserAuthenticationForm()
    context["form"] = form

    return render(request, "users/login.html", context)
