from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import createUserForm


def register(request):
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = createUserForm()
    content = {
        'form' : form,
    }
    return render(request, 'user/register.html', content)
def logout(request):
    return render(request, 'user/logout.html')

def profile(request):
    return render(request, 'user/profile.html')