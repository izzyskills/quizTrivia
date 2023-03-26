from django.shortcuts import render, redirect
from . import models, forms
import csv,io
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('register')

    return render(request, 'login.html')


def register_view(request):
    userForm = forms.UserCreationForm()
    profileForm = forms.ProfileCreationForm()
    context = {'userForm': userForm, 'profileForm': profileForm}
    if request.method == "POST":
        userForm = forms.UserCreationForm(request.POST)
        profileForm = forms.ProfileCreationForm(request.POST, request.FILES)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save(commit=False)
            user.username = user.username.lower()
            user.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('login')
    return render(request, 'register.html', context)


@login_required(login_url='login')
def dashboard_view(request):
    user = User.objects.get(id=request.user.id)
    context = {'user': user}

    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def select_exam_view(request):
    q = request.GET.get("q") if request.GET.get('q') != None else ''

    courses = models.Course.objects.filter(
        Q(course_name__icontains=q) |
        Q(course_code__icontains=q)
    )

    context = {'courses': courses}
    return render(request, 'exam_select.html', context)

@login_required(login_url='login')
def submit_new_quiz_view(request):
    course_form = forms.CourseCreationForm()
    context = {'courseForm':course_form}
    if request.method == 'POST':
        course_form = forms.CourseCreationForm(request.POST,request.FILES)
        if course_form.is_valid():
            csv_file = io.TextIOWrapper(request.FILES["questions"], encoding='utf-8')
            reader = csv.DictReader(csv_file)
            expected_headers = ['question','optiona','optionb','optionc','optiond','answer']
            headers = [header.lower().strip() for header in reader.fieldnames]
            if headers != expected_headers:
                context['error'] = 'invalid header names'
                return render(request,'submit_new_quiz.html',context)
            expected_num_questions = request.POST.get('num_of_question')
            num_of_questions = sum(1 for row in reader)
            if int(num_of_questions) != int(expected_num_questions):
                context['error']= f'Expected {expected_num_questions} questions, but found {num_of_questions}'
                return render(request, 'submit_new_quiz.html',context)
            course = course_form.save(commit=False)
            course.uploaded_by = models.Profile.objects.get(user=request.user)
            course.save()

    return render(request, 'submit_new_quiz.html',context)
