from django.shortcuts import render,redirect
from .forms import SignupForm,loginform,PostForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator
from .models import Post,User
def sign_up(request):
    if(request.method=="POST"):
        fm=SignupForm(request.POST,request.FILES)
        if(fm.is_valid()):
            fm.save()
            messages.success(request,"your acount is successfully create !!!")
    else:
        fm=SignupForm()
    return render(request,'enroll/sign.html',{'form':fm})

def Login(request):
    if not request.user.is_authenticated :
        if(request.method=='POST'):
            fm=loginform(request=request,data=request.POST)
            if(fm.is_valid()):
                uname=fm.cleaned_data['username']
                passw=fm.cleaned_data['password']
                user=authenticate(username=uname,password=passw)
                if user is not None:
                    login(request,user)
                    messages.success(request,"you are login !!!")
                    return redirect('/dashb/')
        else:
            fm=loginform()
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return redirect('/dashb/')

def Profile(request):
    if request.user.is_authenticated  :
        return render(request,'enroll/usr_profile.html',{'name':request.user})
    else :
        return redirect('/log/')
def Logout(request):
    logout(request)
    return redirect('/')

def A(request):
    return render(request,'enroll/base.html')

def aboutview(request):
    return render(request,'enroll/about.html')

def home_view(request):
    post=Post.objects.all().order_by('id')
    p=Paginator(post,2)
    p_num=request.GET.get('page')
    p_obj=p.get_page(p_num)
    return render(request,'enroll/home.html',{'pm':p_obj})


def dashboard(request):
    if request.user.is_authenticated :
        pst=Post.objects.all()
        return render(request,'enroll/dashboard.html',{'posts':pst})
    else:
        return redirect('/log/')

def add(request):
    if request.user.is_authenticated :
        if(request.method=='POST'):
            fm=PostForm(request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm=PostForm()
        return render(request,'enroll/Add.html',{'form':fm})
    else:
        return redirect('/log/')
def update(request,id):
    if request.user.is_authenticated :
        if(request.method=='POST'):
            x=Post.objects.get(pk=id)
            fm=PostForm(request.POST,instance=x)
            if fm.is_valid():
                fm.save()
        else:
            x=Post.objects.get(pk=id)
            fm=PostForm(instance=x)
        return render(request,'enroll/update.html',{'form':fm})
    else:
        return redirect('/log/')
    
def delete(request, id):
    if request.user.is_authenticated :
        if(request.method == "POST"):
            pi=Post.objects.get(id=id)
            print(pi)
            pi.delete()
            return redirect('/dashb/')
    else:
        return redirect('/log/')
