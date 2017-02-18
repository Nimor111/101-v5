from django.shortcuts import render, redirect

from .decorators import anon_required, login_required

from .models import User, Student, Teacher

from .forms import LoginForm

from .forms2 import RegisterForm


# Create your views here.
def index(request):
    return render(request, 'website/index.html', locals())


@anon_required(redirect_url='/website/profile')
def register(request):
    registered = False
    if request.method == 'POST':
        if request.POST.get('home'):
            return redirect("/")
        form = RegisterForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(email=form.cleaned_data['email'])\
                                      .exists():
                form.save()
                registered = True
                return redirect('/website/login')
            else:
                error = 'User already exists'

    else:
        form = RegisterForm()

    return render(request, 'website/register.html', locals())


@anon_required(redirect_url='/website/profile')
def login(request):
    if request.method == 'POST':
        if request.POST.get('home'):
            return redirect("/")
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.save()
            if u is not None:
                request.session['email'] = form.cleaned_data['email']
                return redirect("/website/profile/")
            else:
                error = "No such user! Register or try again!"
    else:
        form = LoginForm()

    return render(request, 'website/login.html', locals())


def logout(request):
    try:
        del request.session['email']
    except KeyError:
        print("No session detected.")
    return redirect('/website/login')


@login_required(redirect_url='/website/login')
def profile(request):
    perm = None
    teacher = student = False
    try:
        perm = Teacher.objects.get(email=request.session['email'])
        teacher = True
    except Teacher.DoesNotExist:
        try:
            perm = Student.objects.get(email=request.session['email'])
            student = True
        except Student.DoesNotExist:
            return redirect('/')
    if request.method == 'POST':
        if request.POST.get('home'):
            return redirect("/")
        elif request.POST.get('+lecture'):
            return redirect("/lecture/new")
        elif request.POST.get('$lecture'):
            return redirect("/course/{}".format(perm.course.all()[0].name))
        return logout(request)
    error = None
    try:
        greeting = "Hello, " + request.session['email']
    except KeyError:
        error = 'Not logged in.'

    return render(request, 'website/profile.html', locals())
