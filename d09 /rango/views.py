from django.shortcuts import render
from rango.models import Students
from rango.forms import Stu_form, User_form
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User


def index(request):
    stu_list = Students.objects.order_by('card_no')
    context_dict = {'stu_list': stu_list}
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            query = query.strip()
            print query
            return HttpResponseRedirect('/stu/'+query+'/')
    return render(request, 'index.html', context_dict)


def student(request, student_name_slug):
    context_dict = {}
    try:
        stu = Students.objects.get(slug=student_name_slug)
        context_dict['stu_name'] = stu.name
        context_dict['card_no'] = stu.card_no
        context_dict['stu_sex'] = stu.sex
        context_dict['grade'] = stu.grade
        context_dict['profile'] = stu.picture

    except Students.DoesNotExist:
        pass

    return render(request, 'student.html', context_dict)


def add_stu(request):
    if request.method == 'POST':
        form = Stu_form(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=False)
            if 'picture' in request.FILES['picture']:
                form.picture = request.FILES['picture']

            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = Stu_form()

    return render(request, 'add_stu.html', {'form': form})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = User_form(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = User_form()

    return render(request, 'register.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/stu/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print "Invalid login details:{0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'login.html', {})


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/stu/')
