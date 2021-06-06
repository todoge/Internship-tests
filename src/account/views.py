from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
# from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def registerPage(request):
    form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                print(form)
                print(form.cleaned_data)
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)
                return HttpResponseRedirect("/")

    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)