from django.shortcuts import render
from django.http import JsonResponse
from myapp.forms import RegisterForm


# Create your views here.
def home_func(request):
    if request.method=='GET':
        return JsonResponse( {"msg":" Home page"},status=200)
    return JsonResponse({"msg":" Invalid request method"},status=405)

def register_view(request):
    if request.method=='POST':
        pass
    elif request.method=='GET':
        form=RegisterForm()
        return render(request,)