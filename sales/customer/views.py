from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'customer/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    return render(request, 'customer/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Here you would typically save the user to the database
        # For example:
        # User.objects.create_user(username=username, password=password, email=email)
        
        return render(request, 'customer/register_success.html', {'username': username})
    return render(request, 'customer/register.html')

