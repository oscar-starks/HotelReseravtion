from django.shortcuts import redirect, render
from .models import Reservations
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.decorators import login_required
from throttle.decorators import throttle

# Create your views here.
@login_required(login_url="accounts:login")
def reserveview(request):
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
    return render(request, "reserving/reservepage.html")

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
      
        if password == password2:
            new_user = User.objects.create_user(
                
                username=username,
                password=password,
            )
            new_user.save()
            print("new user added!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return redirect("/hotelxyz/logout/")

        else:
            print("Not added!!!!!!!!!!!!!!!!!!!!!!!!!")

    return render(request, "reserving\\register.html")

@login_required(login_url="accounts:login")
def myreservations(request):
    username = request.user.username
    current_user = request.user.id
    res = Reservations.objects.filter(Client = current_user)
    num = 0
    for ress in res:
        num += 1

    context = {
        'reservations' : res,
        "it" : num,
        "username" : username
    }
    return render(request, 'reserving\\myreservations.html', context)

@login_required(login_url="accounts:login")
def update(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        sname = request.POST["sname"]
        lname = request.POST["lname"]

        res = Reservations.objects.get(
            First_name = fname,
            Second_name = sname,
            Last_name = lname
        )

        context = {"res" : res}
        return render(request, "reserving\edit.html", context)
    return render(request, "reserving\get.html")

@login_required(login_url="accounts:login")
def updating(request):
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
        id = request.POST.get("id")

        Reservations.objects.filter(id = id).update(
                First_name = fname,
                Second_name =sname,
                Last_name = lname,
                Room_number = rumno,
                Amount_paid = amount,
                Email =email,
                Occupation = occupation,
                Nights_of_stay = res,
                Starting_date =start,
                Ending_date = end,)
        
        return redirect("/hotelxyz/")

def simple_upload(request):
    if request.method == 'POST' and request.FILES['images']:
        myfile = request.FILES['images']
        fs = FileSystemStorage()
        file = fs.save(myfile.name, myfile)
        file_url = fs.url(file)
        print(file_url, "          ", myfile.name)

    return render(request, "reserving/pictures.html" )