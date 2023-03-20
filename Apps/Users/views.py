from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone

from Apps.Users.forms import UserForm
from django.contrib import messages


def home(request):
    now = timezone.now()
    data = {
        'now': now
    }
    return render(request, 'Users/home.html', data)


def sign_up(request):
    data = {
        'form': UserForm(),
    }

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')

            form.save()
            user = authenticate(username=username, password=password1)
            login(request, user)
            messages.success(request, '¡Te haz registrado con éxito!')
            return redirect('home')
        else:
            data['form'] = form
            messages.error(request, 'Ocurrió un error. ¡Revisa e intenta de nuevo!')

    return render(request, 'registration/sign_up.html', data)
