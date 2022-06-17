from multiprocessing import context
from multiprocessing.connection import Client
from django.shortcuts import redirect, render
from .models import Reservations
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def reserveview(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fname = request.POST.get("fname")
            sname = request.POST.get("sname")
            lname = request.POST.get("lname")
            rumno = request.POST.get("roomnumber")
            amount = request.POST.get("amountpaid")
            email = request.POST.get("email")
            occupation = request.POST.get("occupation")
            res = request.POST.get("Reservation")
            start = request.POST.get("startdate")
            end = request.POST.get("enddate") 

            reserve = Reservations(
                First_name = fname,
                Second_name =sname,
                Last_name = lname,
                Room_number = rumno,
                Amount_paid = amount,
                Email =email,
                Occupation = occupation,
                Nights_of_stay = res,
                Starting_date =start,
                Ending_date = end,
                Client = request.user
            )      
            reserve.save()
            return redirect("/hotelxyz/myreservations")
            # print('saved................')

        return render(request, "reserving/reservepage.html")

    elif not request.user.is_authenticated:
        return redirect("/hotelxyz/login/")

def loginview(request):
    username = request.POST.get('username')
    password = request.POST.get("password")
    user = authenticate(request,username = username, password= password)

    if user is not None:
        login(request, user)
        print("loggedin................")
        return redirect("/hotelxyz/")

    elif user is None and username != '':
        print("invalid..................")

    return render(request, "reserving\login.html")

def logoutview(request):
    logout(request)
    return render(request, "reserving\logout.html")

def createuser(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        password2 = request.POST['password2']
        # email = request.POST['email']

        if password == password2:
            new_user = User.objects.create_user(
                # email=email,
                username=username,
                password=password,
            )
            new_user.save()
            print("new user added!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return redirect("/hotelxyz/logout/")

        else:
            print("Not added!!!!!!!!!!!!!!!!!!!!!!!!!")

    return render(request, "reserving\\register.html")


def myreservations(request):
    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.id
        res = Reservations.objects.filter(Client = current_user)
        # All = Reservations.objects.all()
        num = 0
        for ress in res:
            num += 1

        context = {
            'reservations' : res,
            "it" : num,
            "username" : username
        }
        return render(request, 'reserving\\myreservations.html', context)
    
    elif not request.user.is_authenticated:
        return redirect("/hotelxyz/login/")

    # print(username)



    
    # current_user = request.user.id
    # print(current_user)
    # print(User.objects.all()[current_user])

   