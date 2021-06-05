from django.shortcuts import redirect, render
from .forms import CreateUserForm

from django.contrib.auth import logout

# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)