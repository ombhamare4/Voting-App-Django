from django.shortcuts import render,HttpResponse,redirect
# from django.http import HttpResponse
# Create your views here.
from .forms import CreatePollForm
from .models import pollQuetions

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
        form=CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_poll')
            # print(form.cleaned_data['pollquetion'])
    else:

        form =  CreatePollForm()
    context={
        'form':form
    }

    return render(request,'add_poll.html',context)
    pass
    # if request.method=="POST":
    #     pollQ=request.POST.get('pollquetion')
    #     opt1=request.POST.get('option1')
    #     opt2=request.POST.get('option2')
    #     opt3=request.POST.get('option3')

    #     quetion=pollQuetions(pollquetion=pollQ,option1=opt1,option2=opt2,option3=opt3)
    #     quetion.save()

    #     return render(request,'poll_list.html')
    # else:
    #     return render(request,'add_poll.html')
    # pass

def list_poll(request):
    quetion_list=pollQuetions.objects.all()
    # quetion_list=pollQuetions.objects.get(pk=poll_id)
    # quetion_list=pollQuetions.objects.get(pk=poll_id)
    context={
        "list_quetion":quetion_list
    }
    print(context)
    return render(request,'poll_list.html',context)


def vote_poll(request,poll_id):
    quetion_list=pollQuetions.objects.get(pk=poll_id)
    
    if request.method == 'POST':
        # selected_option=
        print(request.POST['poll'])
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            quetion_list.option1_count += 1
        elif selected_option == 'option2':
            quetion_list.option2_count += 1
        elif selected_option == 'option3':
            quetion_list.option3_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        quetion_list.save()

        return redirect('result_poll', quetion_list.id)
    context={
        "list_quetion":quetion_list
    }
    # context['list_quetion']=quetion_list
    return render(request,'vote_poll.html',context)
    pass

def result_poll(request,poll_id):
    quetion_list=pollQuetions.objects.get(pk=poll_id)
    context={
        "list_quetion":quetion_list
    }
    return render(request,'result_poll.html',context)
    pass