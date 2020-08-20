from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from demo_frontend.models import User_Extended

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Accunt created for {username}')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            # add to user extended
            username = request.POST.get("my_username")
            email = request.POST.get("my_email")
            subject = request.POST.get("subject")
            new_record = User_Extended(username = username, email = email, times_classified=1, subject=subject)
            new_record.save()
            # #############################
            login(request, new_user)
            print("LOGGED IN HERE")
            return redirect('home')
    else:
        form = UserRegisterForm()
    print("UHHHHH NOT WHERE")
    return render(request, 'users/register.html', {'form': form})


def main_page(request):
    return render(request, 'users/main_page.html')
