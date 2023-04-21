from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import redirect, render


def login(request):
    if request.method != 'POST':
        return render(request, 'login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)

    if not user:
        messages.error(request, 'Username or password incorrect')
        return render(request, 'login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login successful')
        return redirect('dashboard')


@login_required(redirect_field_name='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        user = __validate_user(request)

        if (user['valid']):
            User.objects.create_user(**user['data']).save()
            messages.success(request, 'User registered')
            return redirect('login')

    return render(request, 'register.html')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def __validate_user(request):
    users = User.objects
    valid = True

    name = request.POST.get('name')
    username = request.POST.get('username')
    surname = request.POST.get('surname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    if not name or not surname or not password or not password2:
        valid = False
        messages.error(request, 'Please enter all required fields')

    try:
        validate_email(email)
    except Exception:
        valid = False
        messages.error(request, 'Please enter valid email address')

    if len(password) < 6:
        valid = False
        messages.error(
            request, 'Please enter password with at least 6 characters')

    if password != password2:
        valid = False
        messages.error(request, 'The passwords must be equal')

    if users.filter(email=email).exists():
        valid = False
        messages.error(request, 'Email already exists')

    if users.filter(username=username).exists():
        valid = False
        messages.error(request, 'Username already exists')

    return {
        'valid': valid,
        'data': {
            'first_name': name,
            'last_name': surname,
            'username': username,
            'email': email,
            'password': password,
        }
    }
