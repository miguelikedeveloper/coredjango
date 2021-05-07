from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import RegistratrionForm

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
