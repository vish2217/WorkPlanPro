from django.shortcuts import render,HttpResponse,redirect
from .forms import CreateUserForm,LoginForm,CreateTaskForm

from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import CustomerMessageForm





def index(request):
    return render(request,'index.html')
    
def login(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')


def createTask(request):
    form = CreateTaskForm() 
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'create_task.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            return redirect('login')  # redirect after successful signup
    context = {'form': form}
    return render(request, 'register.html', context)

from .models import Task


def viewtask(request):
    tasks = Task.objects.all()
    return render(request, 'viewtask.html', {'tasks': tasks})

def updatetask(request, id):  
    task = get_object_or_404(Task, id=id)  

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('viewtask')
    else:
        form = CreateTaskForm(instance=task)  

    context = {'form': form, 'task': task}
    return render(request, 'updatetask.html', context)


def deletetask(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('viewtask')  # Redirect after deletion
    return render(request, 'deletetask.html', {'task': task})

def product(request):
    return render(request,'product.html')

def solutions(request):
    return render(request,'solutions.html')

def resources(request):
    return render(request,'resources.html')

def pricing (request):
    return render(request,'pricing.html')

def enterprise(request):
    return render(request,'enterprise.html')

def customercare(request):
    return render(request,'customercare.html')


def customer_care(request):
    if request.method == 'POST':
        form = CustomerMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')  # Optional thank-you page
    else:
        form = CustomerMessageForm()
    return render(request, 'customer_care.html', {'form': form})

def guide(request):
    return render(request,'guide.html')

def blog(request):
    return render(request, 'blog.html')

def faq(request):
    return render(request, 'faq.html')
