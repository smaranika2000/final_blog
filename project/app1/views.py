from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from app1.models import Post,UserProfile,confApt
from .forms import Appointment



def index(request):
    return render(request,'index.html')

def upload(request):
    if request.method=="POST":
        title=request.POST['title']
        category=request.POST['category']
        summary=request.POST['summary']
        content =request.POST['content']
        author = request.POST['author']
        slug = request.POST['slug']
        draft =request.POST['draft']
        if len(request.FILES)!=0:
            image=request.FILES['image']
        post=Post(
            title=title,
            category=category,
            summary=summary, 
            content=content,
            author=author,
            slug=slug,
            draft=draft,
            image=image,
        )
        post.save()
        messages.success(request, "Your post has been successfully sent")
    return render(request,'upload.html')

def about(request):
    return render(request,'about.html')

def about1(request):
    return render(request,'about1.html')


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        city = request.POST['city']
        state= request.POST['state']
        pincode=request.POST['pincode']
        option=request.POST['option']
        if len(request.FILES)!=0:
            image=request.FILES['image']
        

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/')
        if User.objects.filter(username=username).exists():
            messages.error(request, "user exists")
            return redirect('/')

        # Create the user
        else:
            if(option=="yes"):
                user = User(
                    username = username,
                    email = email,
                    first_name = fname,
                    last_name = lname,
                )
                user.set_password(pass1)
                user.is_superuser = True
                user.is_staff = True
                user.save()
                userprofile=UserProfile(image = image,city=city,state = state,pincode=pincode , user=user , option=option)
                userprofile.save()
                messages.success(request, " Your iCoder has been successfully created ! login to enter dashbord")
                return redirect('/')
            
            else:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name= fname
                myuser.last_name= lname
                userprofile=UserProfile(image = image,city=city,state = state,pincode=pincode , user=myuser , option=option)
                userprofile.save()
                myuser.save()
                messages.success(request, " Your iCoder has been successfully created ! login to enter dashbord")
                return redirect('/')
            

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            print(user)
            messages.success(request, "Successfully Logged In")
            if user.is_superuser:
                return redirect('about1')
            else:
                return redirect('about')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")



def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
# Create your views here.

def one(request):
    allPosts= Post.objects.filter(category="heart deases",draft="no")
    context = {'allPosts': allPosts}
    return render(request, "blog.html", context)

def two(request):
    allPosts= Post.objects.filter(category="immunization",draft="no")
    context = {'allPosts': allPosts}
    return render(request,"blog.html",context)


def three(request):
    allPosts= Post.objects.filter(category="covid-19",draft="no")
    context = {'allPosts': allPosts}
    return render(request,"blog.html",context)

def four(request):
    allPosts= Post.objects.filter(category="mental health",draft="no")
    context = {'allPosts': allPosts}
    return render(request,"blog.html",context)

def own(request):
    allPosts= Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,"blog1.html",context)

def appointment(request):
    all_users = UserProfile.objects.all()
    print(all_users)
    context = {'all_users': all_users}
    return render(request,"appointment.html",context)


