from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Course, Admin

# Create your views here.
def home(request):
    return render(request,"home.html")
def register(request):
    return render(request,"register.html")
def contact(request):
    return render(request,"contact.html")
def save(request):
    n1 = request.POST['n1']
    e1 = request.POST['e1']
    m1 = request.POST['m1']
    p1 = request.POST['p1']
    
    #logic for save
    obj = Student(name=n1, email=e1, password=p1, phone=m1)
    obj.save()
    
    return redirect(login)
def login(request):
    return render(request,"login.html")
def login_logic(request):
    #form data fetched
    n1 = request.POST['n1']
    e1 = request.POST['e1']
    p1 = request.POST['p1']
    
    #abb data ko match karna haii
    
    z = Student.objects.filter(name=n1,email=e1,password=p1)
    if(z.count()==0):
        return HttpResponse("Invalid login")
    else:
        #store user data in login session
        request.session['mysession'] = e1
        return redirect(dashboard)

def dashboard(request):
    e1 = request.session['mysession'] 
    return render(request,"dashboard.html",{'e1':e1})

def profile(request):
    e1 = request.session['mysession'] 
    
    #select * from student where email=e1
    
    student_data = Student.objects.filter(email=e1)
    return render(request,"profile.html",{'student_data':student_data})


def logout(request):
      del request.session['mysession']
      return redirect(login)  
  
def change(request):
     e1 = request.session['mysession'] 
     return render(request,"change.html",{'e1':e1}) 
 
def update(request):
    e1 = request.POST['e1'] 
    old = request.POST['old']
    new = request.POST['new']
    z = Student.objects.filter(email=e1,password=old)
    if(z.count()==0):
        return HttpResponse("old Password is Incorrect")
    else:
        # logic for update
        obj = Student.objects.get(email=e1)
        obj.password = new
        obj.save()
        return redirect(profile)
def apply(request):
    e1 = request.session['mysession']
    return render(request,"apply.html",{'e1':e1})


def save_course(request):
    email = request.POST['e1']
    course = request.POST['course']
    
    #save
    obj = Course(course_name=course, course_fees=6000, student_email=email)
    obj.save()
    
    return redirect(dashboard)

def admin_register(request):
    return render(request,"admin_register.html")


def admin_save(request):
    n1 = request.POST['name']
    e1 = request.POST['email']
    p1 = request.POST['password']
    m1 = request.POST['phone']
    
    #save
    obj = Admin(name=n1,email=e1, password=p1, phone=m1)
    obj.save()
    
    return redirect(admin_login)


def admin_login(request):
    return render(request,"admin_login.html")



def admin_login_logic(request):
    # form data fetch
    e1 = request.POST['e1']
    p1 = request.POST['p1']
    
    z = Admin.objects.filter(email=e1,password=p1)
    if(z.count()==0):
        return HttpResponse("Invalid Login")
    else:
        # storing user data in session
        request.session['mysession'] = e1
        return redirect(admin_dashboard)
    
def admin_dashboard(request):
    e1 = request.session['mysession']
    return render(request,"admin_dashboard.html",{'e1':e1})


def students_list(request):
    data = Student.objects.all() # select * from students
    return render(request,"students_list.html",{"data":data})

def courses_list(request):
    data = Course.objects.all() # select * from students
    return render(request,"courses_list.html",{"data":data}) 

def delete_student(request):
    #fetch "id"
    id = Student.objects.get(pk=request.GET['q'])
    id.delete()
    return redirect(students_list)
       
def delete_course(request):
    #fetch "id"
    id = Course.objects.get(pk=request.GET['q'])
    id.delete()
    return redirect(courses_list)
              