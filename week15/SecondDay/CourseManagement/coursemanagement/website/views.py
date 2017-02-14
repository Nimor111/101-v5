from django.shortcuts import render, redirect

from .decorators import anon_required, login_required

from .models import User, Student, Teacher


# Create your views here.
def index(request):
    return render(request, 'website/index.html', locals())


@anon_required(redirect_url='/website/profile')
def register(request):
    registered = False
    if request.method == 'POST':
        if request.POST.get('home'):
            return redirect("/")
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        if not User.objects.filter(email=email).exists():
            user = User(email=email, password=password, first_name=firstname,
                        last_name=lastname)
            registered = True
            user.save()
        else:
            error = 'User already exists'

    return render(request, 'website/register.html', locals())


@anon_required(redirect_url='/website/profile')
def login(request):
    if request.method == 'POST':
        if request.POST.get('home'):
            return redirect("/")
        email = request.POST.get('email')
        password = request.POST.get('password')

        u = User.login(email, password)

        if u is not None:
            request.session['email'] = email
            return redirect("/website/profile/")
        else:
            error = "No such user! Register or try again!"
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
        perm = Student.objects.get(email=request.session['email'])
        student = True
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
