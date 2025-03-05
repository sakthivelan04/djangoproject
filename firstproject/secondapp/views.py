from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from .models import Student
from firstapp.models import cultural


# Create your views here.

def h(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = Student.objects.get(id=user_id)
        cultural_data = cultural.objects.all()  # Collecting data from models
        context = {'user': user, 'cul_list': cultural_data}  # Dictionary
        return render(request, 'firstapp/cultural.html', context)
    else:
        return redirect('secondapp:login')

def logout_view(request):
    request.session.flush()
    return redirect('secondapp:login')

def login_view(request):
    if request.method == 'POST':
        register_no = request.POST.get('register_no')
        password = request.POST.get('password')
        try:
            user = Student.objects.get(register_no=register_no)
            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('secondapp:home')
            else:
                messages.error(request, "Invalid Password")
        except Student.DoesNotExist:
            messages.error(request, "Invalid Register number")
    return render(request, 'secondapp/login.html')



def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('secondapp:login')
    else:
        form = UserForm()
    return render(request, 'secondapp/register.html', {'form': form})



