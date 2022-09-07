from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views import View
import random
# Create your views here.

def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(request, username = username, password= password)

        if user is not None:
            login(request, user)
            print("loggedin................")
            return redirect("/test/")

        elif user is None and username != '':
            print("invalid..................")

    return render(request, "dispose\login.html")

    
def getemail(request):    
    return render(request, "dispose/get.html")

def sendotp(request):

    if request.method == "POST":
        emails = request.POST["email"]
        
        try:
            user = User.objects.get(email = emails)
            ids = user.id
            username = user.username
            mynum = ""
            for i in range(4):
                num = random.randint(0, 9)
                mynum += str(num)
            otp = int(mynum)
            print(otp)
            
            subject = 'OTP for Kodecamp-Dipoze'
            messages = f'Hi {username}, your generated OTP is {otp}, use this to proceed to your password reset page. NOTE:This is just a confirmation mail'
            email_from = settings.EMAIL_HOST_USER
            email = emails
            # email2 = 'iniememt@gmail.com'
            recipient_list = [email]
            send_mail( subject, messages, email_from, recipient_list )
            print("success")
            
        except User.DoesNotExist:
            print("not successful, probably user does not exist")
        
        context = {"id":ids,
                   "otp": otp}
    
    return render(request, "dispose/inputotp.html", context)
    
    

def resetpassword(request):
    if request.method == "POST":
        ids = request.POST["id"]
        otp = request.POST["otp"]
        yourotp =  request.POST["yourotp"]
        context = { "id":ids }
        
        if yourotp == otp:
            return render(request, "dispose/newpassword.html",context )
        
        
def newpassword(request):
     if request.method == "POST":
         
        username = request.POST["username"]
        ids = request.POST['id']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        try:
            if password == password2:
                user = User.objects.get(id = ids)
                user.set_password(password)
                user.save()
                print("successfully corrected")
                return redirect("/test/")

        except ValueError:
            print("Not corrected!")
            return redirect('/dispose/inputotp/')

   
def payment(request):
    return render(request, '')
   
# class myview(View):
    
#     def get(self, request, *args, **kwargs)

# class myview(
# class MODEL_NAMECreateView(CreateView):
#     model = MODEL_NAME
#     template_name = "TEMPLATE_NAME"
# )



        