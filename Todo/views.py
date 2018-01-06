

# Create your views here.
# def index(request):
#     MyToDos=Todo.objects.all()
#
#     return render(request,'Todo/base.html',{'MyToDos':MyToDos})
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.template import RequestContext
from  django.views import generic
from django.views.generic import View, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse, request
from django.contrib.auth import login,logout,authenticate
from  django.http import request

from Todo.forms import SignUpForm
from .models import MyList, UserForm, UserProfileForm
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from django.contrib.auth .views import auth_login











class Index(generic.ListView):

    template_name = 'Todo/index.html'
    context_object_name = 'Todos'
    queryset=MyList.objects.filter(title__icontains='Dev')

    def get_queryset(self):


        return MyList.objects.all()
    # def get(self,request):
    #     Todo=MyList.objects.all()
    #     query=request.GET.get("q")
    #     if query:
    #         Todo=Todo.filter(title__icontains=query)
    #     return render(request,'Todo/index.html',{'Todo':Todo})






def TodoDetails(request,Todo_id):

        Todo=get_object_or_404(MyList,pk=Todo_id)
        if Todo:
            return render(request,'Todo/details.html',{'Todo':Todo})
        else:
            return HttpResponse("No entries found")
def register(request):
    context=RequestContext(request)
    registered=False
    if request.method=='POST':
            uform=UserForm(data=request.POST)
            pform=UserProfileForm(data=request.POST)
            if uform.is_valid() and pform.is_valid():
                user=uform.save()
                pw=user.password
                user.set_password(pw)
                user.save()
                profile=pform.save(commit=False)
                profile.user=user
                profile.save()
                registered=True
            else:
                print uform.errors, pform.errors
    else:
        uform=UserForm()
        pform=UserProfileForm()
    return render_to_response('Todo/register.html',{'uform':uform,'pform':pform,
                                                    'registered':registered},context)
def user_login(request):
    context=RequestContext(request)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("Todo/register.html")
        else:
            return HttpResponse("sorry your account is disabled")
    else:
        print "invalid credentials specified"
        return render_to_response('Todo/login.html',{},context)



def signup(request):

    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('/')
        else:
            form=SignUpForm()
            return render_to_response('registration/signup.html',{'form':form})

def Search(request):
    myTodo = MyList.objects.all()

    if request.method=='GET':
        search_query=request.GET.get("q",None)

        query_list=myTodo.filter(title__icontains=search_query)
        return render_to_response('Todo/searchPost.html',{'query_list':query_list})

class Todocreate(CreateView):
    model = MyList
    success_url = reverse_lazy('todo_list')
    fields=['title','text_preview','Date','logo','Body']


