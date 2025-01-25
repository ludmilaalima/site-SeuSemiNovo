from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_view(request):
    user_form = UserCreationForm

    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            return redirect('login')



    return render(request,
                  'register.html',
                  {'user_form' : user_form})


def login_view(request):
    form_user = AuthenticationForm()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            return
        
        elif user:
            login(request, user)
            return redirect('cars_list')

        else:
            messages.error(request, "Credenciais Inválidas")

    return render(request,
                  'login.html',
                  {'form_user': form_user})


def logout_view(request):
    logout(request)
    return redirect('cars_list')