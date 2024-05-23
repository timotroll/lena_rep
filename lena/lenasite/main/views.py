
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/home.html', data)

def about(request):
    return render(request, 'main/about.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})
