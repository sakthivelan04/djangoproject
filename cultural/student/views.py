from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from .models import Student
from events.models import cultural



# Create your views here.
def u(request):
    cultural_data = cultural.objects.all()  # Collecting data from models
    v_dict = {'cul_list': cultural_data}
    return render(request, 'events/event.html', context = v_dict)
def h(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = Student.objects.get(id=user_id)
        cultural_data = cultural.objects.all()  # Collecting data from models
        context = {'user': user, 'cul_list': cultural_data}  # Dictionary
        return render(request, 'events/cultural.html', context)
    else:
        return redirect('student:login')

def logout_view(request):
    request.session.flush()
    return redirect('student:login')

def login_view(request):
    if request.method == 'POST':
        register_no = request.POST.get('register_no')
        password = request.POST.get('password')
        try:
            user = Student.objects.get(register_no=register_no)
            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('student:home')
            else:
                messages.error(request, "Invalid Password")
        except Student.DoesNotExist:
            messages.error(request, "Invalid Register number")
    return render(request, 'student/login.html')



def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('student:login')
    else:
        form = UserForm()
    return render(request, 'student/register.html', {'form': form})



