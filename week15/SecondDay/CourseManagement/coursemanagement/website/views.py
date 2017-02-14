from django.shortcuts import render, redirect

from .decorators import anon_required, login_required

from .models import User


# Create your views here.
def index(request):
    return render(request, 'website/index.html', locals())


@anon_required(redirect_url='/website/profile')
def register(request):
    registered = False
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email=email).exists():
            user = User(email=email, password=password)
            registered = True
            user.save()
        else:
            error = 'User already exists'

    return render(request, 'website/register.html', locals())


@anon_required(redirect_url='/website/profile')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        u = User.login(email, password)

        if u is not None:
            request.session['email'] = email
            return redirect("/website/profile/")
        else:
            error = "No such user!"
    return render(request, 'website/login.html', locals())


def logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return redirect('/website/login')


@login_required(redirect_url='/website/login')
def profile(request):
    if request.method == 'POST':
        return logout(request)
    error = None
    try:
        greeting = "Hello, " + request.session['email']
    except KeyError:
        error = 'Not logged in.'

    return render(request, 'website/profile.html', locals())
