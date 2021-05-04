from django.shortcuts import render,HttpResponse
from .models import pollQuetions
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
    if request.method=="POST":
        pollQ=request.POST.get('pollquetion')
        opt1=request.POST.get('option1')
        opt2=request.POST.get('option2')
        opt3=request.POST.get('option3')

        quetion=pollQuetions(pollquetion=pollQ,option1=opt1,option2=opt2,option3=opt3)
        quetion.save()

        return render(request,'poll_list.html')
    else:
        return render(request,'add_poll.html')
    pass

def list_poll(request):
    quetion_list=pollQuetions.objects.all()
    context={
        "list_quetion":quetion_list
    }
    print(context)
    return render(request,'poll_list.html',context)


def vote_poll(request):
    return render(request,'poll_vote.html')
    pass

def result_poll(request):
    return render(request,'poll_result.html')
    pass