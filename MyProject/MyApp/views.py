from django.shortcuts import render,redirect
from django.http import HttpResponse
from MyApp.models import Student
# Create your views here.
def sample(request):
	return HttpResponse("Hai guys welcome to django session")

def hlo(request):
	return HttpResponse("<h2 style=background-color:blue;color:red;font-size:70px;font-style:italic>Hai..guys..</h2>")

def dynamic(request,id):
	return HttpResponse("<h2 style=background-color:blue;color:red;font-size:70px;font-style:italic>My Roll number is:{}</h2>".format(id))

def task(request,name):
	return HttpResponse("My name is:{}".format(name))

def home(request,id,name):
	return HttpResponse(" <h2 style=background-color:green;color:blue;font-size:50px;font-style:italic>My rollnumber is :{},<br> My name is:{} </h2>".format(id,name))

def temp(request):
	return render(request,'MyApp/temp.html')


def table(request):
	return render(request,'MyApp/table.html')

def inline(request):
	return render(request,'MyApp/inline.html')

def internal(request):
	return render(request,'MyApp/internal.html')

def external(request):
	return render(request,'MyApp/external.html')

def boot(request):
	return render(request,'MyApp/boot.html')

def register(request):
	return render(request,'MyApp/register.html')

def offline(request):
	return render(request,'MyApp/offline.html')


def reg(request):
	if request.method=="POST":
		na=request.POST['name']
		roll=request.POST['rollnum']
		age=request.POST['age']
		mbl=request.POST['mbl']
		em=request.POST['email']
		add=request.POST['addr']

		Student.objects.create(name=na,rollnum=roll,age=age
			,mobile=mbl,email=em,address=add)

		# return HttpResponse("your data is added successfully")
		return redirect('/display')



	return render(request,'MyApp/reg.html')


def display(request):
	data=Student.objects.all()
	return render(request,'MyApp/display.html',{'data':data})


def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data.name=request.POST['name']
		data.rollnum=request.POST['rollnum']
		data.age=request.POST['age']
		data.mobile=request.POST['mbl']
		data.email=request.POST['email']
		data.address=request.POST['addr']
		data.save()
		return redirect('/display') 

	return render(request,'MyApp/update.html',{'data':data})


def delete(request,id):
	ob=Student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/display')
	return render(request,'MyApp/delete.html',{'info':ob})