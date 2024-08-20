from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http  import HttpResponse 
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from.models import Feedback, FeedbackDetails,Student,Trainer
import crispy_forms
from .forms import MyModel
import datetime
from datetime import datetime,timedelta
from .forms import RegularUserSignupForm, AdminSignupForm
# from django.core.exceptions import ObjectDoesNotExist


     

def index(request):
    return render(request,'index.html')


def trainerlogin(request):
    try:
        usrname=request.POST.get('username')
        pwd1 = request.POST.get('password')
        user = authenticate(request,username=usrname,password=pwd1)
        if user is not None:
            login(request,user)
            userGroup = Group.objects.get(user=request.user).name 
            print(userGroup)
            if userGroup == 'Trainer': 
                return redirect('feedbacklistview')
            else:
                return redirect('trainerlogin')
        else:
            return render(request,"trainerlogin.html",{"msg":"invalid login"})
    except Exception as e:
        error_msg = f"An error occurred: {str(e)}"
        print(error_msg)
        # Handle the exception here (e.g., log the error, show an error message, etc.)
        return render(request, "trainerlogin.html", {"msg": "An error occurred"})

    


def loginview(request):
    uname=request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request,username=uname,password=pwd)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"invalid login"})



    





    
def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return redirect("login")


def sign_up(request):
    responseDic={}
    try:
        form = UserCreationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(request, username=username, password=password)
                login(request,user)
                return redirect('login')
        else:
            return render(request,'signup.html',{'form':userform,'msg':'Invalid login'})
        
    except Exception as e:
        print(e)
        userform = UserCreationForm()
        return render(request,'signup.html',{'form':userform,'msg':'Invalid login'})

    
def trainerhome(request):
    return render(request,'trainersignup.html')

def trainersign_up(request):
    responceDic={}
    try:
        username=request.POST['name']
        pwd=request.POST['password']
        user=User.objects.create_user(username,pwd)
        user.save()
        user=User.objects.get(username=user.username)
        my_group=Group.objects.get(name='Trainer')
        user.groups.add(my_group)
        user.save()
        return redirect('trainerlogin')
    except Exception as e:
        print(e)
        responceDic['msg1']='invalid' 
        return render(request, "trainersignup.html")
   # user=authenticate(request, username=username, password=pwd) 
    #login(request, user
    
    # else:
    #     return render(request, "trainersignup.html")






# def Resethome(request):
#     return render(request,"ResetPassword.html")

# def resetPassword(request):
#     responseDic={}
#     uname = request.POST['uname']
#     newpwd=request.POST['newpwd']


#     try:
#         user=User.objects.get(username=uname)
#         if user is not None:
#             user.set_password(newpwd)
#             user.save()
#             responseDic["errmsg"]="Password reset successfully"
#             return render(request,"ResetPassword.html",responseDic)
#     except Exception as e :
#         print(e)
#         responseDic["errmsg"]="password reset failed"
#         return render(request,"ResetPassword.html",responseDic)    
    
def feedback(request):
    feedbackform=MyModel()
    if request.method== 'POST':
        form = MyModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect("submit-form")
            
    else:
        form=MyModel()
        
    return render(request,'feedback.html',{'form':feedbackform})

# def submit_form(request):
#     if request.method== 'POST':
#         form = MyModel(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("feedbackdetail.html")
#     else:
#         form=MyModel()
#     return render(request,'feedback.html',{'form':form})
    



def detailfeedback(request):
    # today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    # today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    # date__range=(today_min, today_max)
    #Invoice.objects.get(user=user, date__range=(today_min, today_max))
    student=Student.objects.get(student_name=request.user)
    user_id=student.id
    data=FeedbackDetails.objects.filter(student_id=user_id)
    return render(request,'feedbackdetail.html',{"data":data})

def deletefeedback(request,fid):
    feed=FeedbackDetails.objects.get(id=fid)
    feed.delete()
    return redirect('home')


def feedbacklistview(request):
    print(request.user)
    trainer=Trainer.objects.get(trainer_name=request.user)
    print(trainer.trainer_name)
    list=FeedbackDetails.objects.filter(trainer_name=trainer)        
    return render(request,'feedbacklistview.html',{"list":list})



 