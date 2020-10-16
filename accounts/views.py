from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404


def login(request):
    if request.user.is_authenticated:
        return redirect('/accounts/login')
    else:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                return redirect('/accounts/login')
        else:
            form = AuthenticationForm()

        return render(request, 'registration/login.html', {'form': form})


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, please Login')

            return redirect('/accounts/login')
    else:
        form = UserCreationForm

    return render(request, 'accounts/sign_up.html', {'form': form})


def user_detail(request, pk):
    # I retrieve user information if it exists. Otherwise I raise an exception http404
    user = get_object_or_404(User, pk=pk)
    return render(request, 'accounts/user_detail.html', {'user': user})


def main_page(request):
    return redirect('/accounts/login')
