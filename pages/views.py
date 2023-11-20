from django.shortcuts import render, redirect, get_object_or_404
from students.models import students, enrolledcourses
from counsellors.models import counsellors
from django.contrib import messages, auth
from django.contrib.auth.models import User
from courses.models import courses, CourseUnits


# Create your views here.
def index(request):
    return render(request, "pages/index.html")


def dashboard1(request):
    ALLcourses = courses.objects.all()
    ALLenrolled = enrolledcourses.objects.filter(student_id=request.user.id)

    context = {
        "ALLcourses": ALLcourses,
        "ALLenrolled": ALLenrolled,
    }
    print(ALLenrolled)
    return render(request, "pages/dashboard1.html", context)


def dashboard2(request):
    return render(request, "pages/dashboard2.html")


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")


def login(request):
    return render(request, "pages/login.html")


def register(request):
    return render(request, "pages/register.html")


# here is logic behind student registeration in the database
def studentregister(request):
    if request.method == "POST":
        # Get form values into string then post it into the database
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        checkbox = request.POST["checkbox"]
        if password1 == password2:
            # check username and email so that no duplicacy occur
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is already taken")
                redirect("studentregister")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is already registered")
                    redirect("studentregister")
                else:
                    # ALL validation complete now
                    user = User.objects.create_user(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password1,
                    )
                    user.save()
                    messages.success(
                        request,
                        "You are successfully registered with us And ready to log in",
                    )
                    return redirect(studentlogin)
        else:
            # return Message Password did not match
            messages.error(request, "Password did not match")
            return redirect("studentregister")

    return render(request, "pages/studentregister.html")


# here is logic behind counsellor registeration in the database
def counsellorregister(request):
    if request.method == "POST":
        # Get form values into string then post it into the database
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        checkbox = request.POST["checkbox"]
        if password1 == password2:
            # check username and email so that no duplicacy occur
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is already taken")
                redirect("counsellorregister")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is already registered")
                    redirect("counsellorregister")
                else:
                    # ALL validation complete now
                    user = User.objects.create_user(
                        first_name=firstname,
                        last_name=lastname,
                        username=username,
                        email=email,
                        password=password1,
                    )
                    user.save()
                    messages.success(
                        request,
                        "You are successfully registered with us And ready to log in",
                    )
                    return redirect("counsellorlogin")
        else:
            # return Message Password did not match
            messages.error(request, "Password did not match")
            return redirect("counsellorregister")

    return render(request, "pages/counsellorregister.html")


# here is logic behind verifying student and then logging into the database in the database
def studentlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard1")
        else:
            messages.error(request, "Wrong Credentials")
            return redirect("studentlogin")
    return render(request, "pages/studentlogin.html")


# here is logic behind verifying counsellor and then logging into the database in the database
def counsellorlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        checkbox = request.POST["checkbox"]
        user = auth.authenticate(username=username, password=password)
        if checkbox == "checkboxvalue":
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You are now logged in")
                return redirect("dashboard2")
            else:
                messages.error(request, "Wrong Credentials")
                return redirect("counsellorlogin")
    return render(request, "pages/counsellorlogin.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now successfully logged out")
        return redirect("index")
    


def enrolledcourse(request, course_id):
    course = get_object_or_404(CourseUnits, pk=course_id)
    context = {"courseunitskey": course}
    return render(request, "pages/EnrolledCourse.html", context)


def viewCourse(request, course_id):
    course = get_object_or_404(courses, pk=course_id)
    context = {"coursekey": course}
    return render(request, "pages/viewCourse.html", context)


def browseCourses(request):
    course=courses.objects.all()
    context={
        "allcourses":course
    }
    return render(request, "pages/browseCourses.html",context)


def browseCounsellor(request):
    teachers=counsellors.objects.all()
    context={
        "allcounsellorkey":teachers,
    }
    return render(request, "pages/browseCounsellor.html",context)

