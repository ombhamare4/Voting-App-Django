from django.shortcuts import render,HttpResponse
# from django.http import HttpResponse
# Create your views here.
def top(request):
    return render(request,'top.html')

def login(request):
    return render(request,'login.html')
    pass

def signup(request):
    return render(request,'signup.html')
    pass

def about(request):
    return render(request,'about.html')
    pass

def add_poll(request):
    return render(request,'add_poll')
    pass

def list_poll(request):
    return render(request,'poll_list')
    pass

def vote_poll(request):
    return render(request,'poll_vote.html')
    pass

def result_poll(request):
    return render(request,'poll_result.html')
    pass