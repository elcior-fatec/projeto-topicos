from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
