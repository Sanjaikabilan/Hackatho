from django.shortcuts import render , redirect
from .models import State
from .models import Stud
from .filters import StateFilter
import random
from random import choice

# Create your views here.

def state(request):
    a = State.objects.all()

    myFilter = StateFilter(request.GET, queryset=a)
    a = myFilter.qs
    for i in a:
        print(i.problem)
    return render(request,'state.html', {'a':a,'myFilter':myFilter})


def reset(request):

    if request.method == 'GET':
        a = State.objects.all()

    return render(request,'state.html', {'a':a})


def cus(request):

    a = State.objects.all()

    if request.method == 'GET':
        a = State.objects.all()

        dom = request.GET.get('domain')
        hard = request.GET.get('hardness')
        a = State.objects.filter(domain=dom)


    return render(request,'cus.html', {'a':a})


def stud(request):

    questions = ['Question1', 'Question2', 'Question3', 'Question4', 'Question5', 'Question6', 'Question7', 'Question8', 'Question9', 'Question10']
    ran = random.choice(questions)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        answer = request.POST.get('answer')
        question = ran

        stud = Stud(name=name, email=email, contact=contact, question=question , answer=answer)

        

        if Stud.objects.filter(email=email).exists():
            return render(request, 'stud.html', {'error': 'Email already exists'})


        if Stud.objects.filter(contact=contact).exists():
            return render(request, 'stud.html', {'error': 'Contact already exists'})
        
        if answer != '':
            stud.save()
            return redirect('suc')
        else:
            return render(request, 'stud.html', {'error': 'Please answer the question'})

    return render(request,'stud.html', {'ran':ran})

def suc(request):
    return render(request,'suc.html')





