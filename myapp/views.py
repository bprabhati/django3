from django.shortcuts import redirect, render
from django.http import JsonResponse
from myapp.forms import LoginForm, RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home_func(request):
    # if request.method=='GET':
        cookie=request.COOKIES.get('username')
        return render(request, 'home.html', {'username':cookie})
    # return JsonResponse({"msg":" Invalid request method"},status=405)

def register_view(request):
    if request.method=='POST':
       form=RegisterForm(request.POST)
       if form.is_valid():
           res=form.save()
           return JsonResponse({"msg":f"user with {res.username} registred successfully"})
       err=form.errors
       return JsonResponse(err,status=400)

    
    elif request.method=='GET':
        form=RegisterForm()
        return render(request,'register.html',{"form":form})
    
def login_view(request):
        if request.method=='POST':
            form=LoginForm(request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    res=redirect("home_name")
                    res.set_cookie('username',username)
                    return res
                return JsonResponse({"msg":"provide valid creds"})
            err=form.errors
            return JsonResponse(err)
        elif request.method=='GET':
            form=LoginForm()
            return render(request, 'login.html', {"form":form})
def logout_view(request):
     logout(request) 
     return JsonResponse({"msg":"user logged out successfully"})      
            
