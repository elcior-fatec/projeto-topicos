from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import EditUser


@login_required
def edit_user(request):
    if request.method == 'POST':
        form = EditUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('edit_user')
    else:
        form = EditUser(instance=request.user)
        return render(request, 'edit-user.html', {'form': form})


@login_required
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Sua senha foi atualizada!")
            return redirect('edit_user')
        else:
            messages.error(request, "Por favor corrija os erros abaixo.")
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'change-pass.html', {'form': form})


def new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

        return render(request, 'registration/reg-form.html', {'form': form})
