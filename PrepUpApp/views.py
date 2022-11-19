from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
# Create your views here.


def Dashboard(request):
    userData = SignupForm.objects.all()
    suggestors = RecommendMaterial.objects.all()
    interviews = InterviewDetails.objects.all()
    successstories = SuccessStory.objects.all()
    if request.user.is_authenticated:
        data = SignupForm.objects.filter(username=request.user.username).first()
        context = {'userData':userData, 'data':data, 'suggestors':suggestors, 'interviews':interviews, 'successstories':successstories}
    return render(request, 'PrepUpApp/Dashboard.html', context)



def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Login Failed: User Does Not Exit')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('Dashboard')

        else:
            messages.error(request, 'Login Failed: Please Try Again')
            return render(request, 'PrepUpApp/Login.html')
    return render(request, 'PrepUpApp/Login.html')

def SignUp(request):
    if request.method == 'POST':
        # form = SignupForm(request.POST, request.FILES)
        fullname = request.POST['fullname']
        username = request.POST['username']
        profession = request.POST['profession']
        email = request.POST['email']
        portfolio = request.POST['link']
        years_of_experience = request.POST['years_of_experience']
        profilepicture = request.FILES.get('profileimage', False)
        password = request.POST['password']
        retypepassword = request.POST['repassword']
        
        if password != retypepassword:
            messages.error(request, 'Passwords Are Not Same')
            return redirect('Signup')

        data = SignupForm.objects.filter(username=username)
        if data:
            messages.error(request, 'Sorry, Username Is Already Taken')
            return redirect('Loginpage')
        else:
            messages.success(request, 'Registration Successful')
            form = SignupForm(fullname=fullname, username=username, email=email, profession=profession, years_of_experience= years_of_experience,
                            portfolio=portfolio, password=password, repassword=retypepassword, profileimage=profilepicture)

            user = User.objects.create_user(
                first_name=fullname, email=email, password=password, username=username)
            login(request, user)
            user.save()
            form.save()
            return redirect('Signup')
            messages.success(request, 'Registration Successful')
        # messages.success(request, 'Registration Failed')
    return render(request, 'PrepUpApp/Signup.html')



def logoutUser(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return render(request, 'PrepUpApp/Logoutpage.html')


def InterviewSchedule(request):
    if request.method == 'POST':
        user = request.user
        interviewer = request.POST['name']
        form = InterviewDetails(user = user, interviewer = interviewer)
        form.save()
        return redirect('Dashboard')
    userData = SignupForm.objects.exclude(username=request.user.username)
    if request.user.is_authenticated:
        data = SignupForm.objects.filter(username=request.user.username).first()
        context = {'userData':userData, 'data':data}
    return render(request, 'PrepUpApp/Interviewschedule.html', context)



def LandingPage(request):
    return render(request, 'PrepUpApp/landingpage.html')


def Profile(request, username):
    allusers = SignupForm.objects.get(username = username)
    suggestors = RecommendMaterial.objects.all()
    if request.user.is_authenticated:
        data = SignupForm.objects.filter(username=request.user.username).first()
        context = {'allusers':allusers, 'data':data, 'suggestors':suggestors}
    return render(request, 'PrepUpApp/profile.html', context)



def Uploadmaterial(request):
    if request.method == 'POST':
        user = request.user
        Title = request.POST['title']
        Material_type = request.POST['Material_type']
        Description = request.POST['description']
        benefits_of_use = request.POST['benefits']
        Material_URL = request.POST['materialLink']
        Meant_for = request.POST['Meant_for']
        
        messages.success(request, 'Suggested Material Has Been Uploaded!')
        form = RecommendMaterial(user = user, Title=Title, Material_type=Material_type, Description=Description, 
                                 benefits_of_use=benefits_of_use, Material_URL=Material_URL, Meant_for=Meant_for)
        
        form.save()
        messages.success(request, 'Suggested Material Has Been Uploaded!')
        return redirect('Suggestamaterial')
    return render(request, 'PrepUpApp/Uploadmaterials.html')


def Suggestamaterial(request):
    allmaterials = RecommendMaterial.objects.all()
    context = {'allmaterials':allmaterials}
    return render(request, 'PrepUpApp/Suggestedmaterials.html', context)



def SuccessStories(request):
    return render(request, 'PrepUpApp/Successstory.html')


def Rooms(request):
    rooms = CreateRooms.objects.all()
    
    context = {'rooms':rooms}
    return render(request, 'PrepUpApp/Rooms.html', context)


def Createarooms(request):
    if request.method == 'POST':
        host = request.user
        topic = request.POST['topic']
        description = request.POST['description']
        form = CreateRooms(host = host, topic = topic, description=description)
        form.save()
        messages.success(request, 'Room Successfully Created!')
        return redirect('Rooms')
    return render(request, 'PrepUpApp/Create-room.html')



def Updateroom(request, pk):
    rooms = CreateRooms.objects.get(id = pk)
    # form = CreateRooms()
    if request.method == 'POST':
        form = CreateRooms()
        form.save()
        messages.success(request, 'Room Successfully Updated!')
        return redirect('Rooms')
    # context= {}
    return render(request, 'PrepUpApp/Create-room.html')


def DeleteRoom(request, pk):
    room = CreateRooms.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Room Successfully Deleted!')
        return redirect('Rooms')
    context = {'thisroom': room}
    return render(request, 'PrepUpApp/Deleteroom.html', context)


def Insideroom(request, pk):
    rooms = CreateRooms.objects.get(id = pk)
    room_messages = rooms.message_set.all().order_by('-created_at')
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = rooms,
            body = request.POST['body']
        )
        return redirect('Insideroom', pk = rooms.id)
    context = {'rooms': rooms, 'room_messages': room_messages}
    return render(request, 'PrepUpApp/InsideRoom.html', context)


def Searchresult(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    material = RecommendMaterial.objects.filter(
        Q(Title__icontains = q) |
        Q(Description__icontains = q)
    )
    roomresult = CreateRooms.objects.filter(
        Q(topic__icontains = q) | 
        Q(description__icontains = q)
    )
    usersearch = SignupForm.objects.filter(
        Q(fullname__icontains = q) | 
        Q(username__icontains = q) |
        Q(profession__icontains = q)
    )
    context = {'material': material, 'roomresult': roomresult, 'usersearch' : usersearch}
    return render(request, 'PrepUpApp/Searchresult.html', context)


def InterviewResult(request):
    return render(request, 'PrepUpApp/Interviewresult.html')


def Successstory(request):
    if request.method == 'POST':
        user = request.user
        testimony = request.POST['testimony']
        video = request.POST['videolink']
        form = SuccessStory(user = user, testimony = testimony, Video = video)
        form.save()
        return redirect('Dashboard')
    return render(request, 'PrepUpApp/Successstory.html')