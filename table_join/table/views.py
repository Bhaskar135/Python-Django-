from django.http import HttpResponse
from django.shortcuts import redirect,render
from.models import Student,Std_mrk
from django.contrib.auth.models import User,auth

def index(request):
    if request.method=="GET":
        reg_no=request.GET.get('reg_no')
        name=request.GET.get('name')
        if request.GET.get('search'):
            if reg_no is not "":
                sm=Std_mrk.objects.filter(pk=reg_no)
            elif name is not "":
                sm=Std_mrk.objects.filter(mark_id__name__istartswith=name)
            else:
                sm=Std_mrk.objects.all()

        elif request.GET.get('show'):
            sm=Std_mrk.objects.order_by('mark_id__reg_no')
        else:
            sm=None
    else:
        if request.POST.get('insert'):
            reg_no=request.POST.get('reg_no1')
            name=request.POST.get('name1')
            marks=request.POST.get('marks1')
            if Student.objects.filter(reg_no=reg_no).exists():
                return HttpResponse("Registration Number already exist")
            else:
                std=Student(reg_no=reg_no,name=name)
                std.save()
                count=Std_mrk.objects.all().count()
                std1=Std_mrk(pk=count+1,mark=marks)
                std1.save()
                sm=Std_mrk.objects.all()
        elif request.POST.get('update'):
            reg_no=request.POST.get("reg_no2")
            name=request.POST.get('name2')
            marks=request.POST.get('marks2')
            std=Student(reg_no=reg_no,name=name)
            std.save()
            std1=Std_mrk(pk=reg_no,mark=marks)
            std1.save()
            sm=Std_mrk.objects.all()
        else :
            reg_no=request.POST.get("reg_no3")
            name=request.POST.get('name3')
            s=Student.objects.filter(reg_no=reg_no,name=name)
            s.delete()
            sm=Std_mrk.objects.all()
    return render(request,'student.html',{'sm':sm})


def register(request):
    if request.method=='POST' :
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                print("Username taken")
            elif User.objects.filter(email=email).exists():
                print("Email taken")
            else:
                user=User.objects.create_user(password=password1,username=user_name,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print("User created")
        else:
            print("Password not matching.")
        return redirect('/')
    else:
        return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return render(request,'student.html')
        else:
            return HttpResponse("Try Again")
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




    






