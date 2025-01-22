from django import render

# Create your views here.
def home(request):
    context = {
        'greeting': 'hello world',
        'name': 'John Doe',
    }
    return render(request, 'culturalapp/index.html', context )