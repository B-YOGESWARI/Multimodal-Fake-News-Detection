from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RegisterForm
from .models import RegisteredUser, PredictionHistory
from .ml_model import predict_fake_news
import os

# =========================
# INDEX
# =========================
def index(request):
    if request.session.get('user'):
        return redirect('home')
    return render(request, 'index.html')

# =========================
# USER REGISTRATION
# =========================
def register(request):
    if request.session.get('user'):
        return redirect('home')

    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'register.html', {'form': form})

# =========================
# USER LOGIN
# =========================
def login(request):
    if request.session.get('user'):
        return redirect('home')

    error = None

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = RegisteredUser.objects.filter(
            username=username,
            password=password,
            is_active=True
        ).first()

        if user:
            request.session['user'] = user.username
            return redirect('home')
        else:
            error = "Invalid credentials or account not activated"

    return render(request, 'login.html', {'error': error})

# =========================
# USER HOME
# =========================
def home(request):
    if not request.session.get('user'):
        return redirect('login')
    return render(request, 'home.html')

# =========================
# TRAINING PAGE
# =========================
def training(request):
    if not request.session.get('user'):
        return redirect('login')
    return render(request, 'training.html')

# =========================
# PREDICTION PAGE
# =========================
def predict(request):
    if not request.session.get('user'):
        return redirect('login')

    result = None

    if request.method == "POST":
        text = request.POST['news_text']
        image = request.FILES['news_image']

        image_path = os.path.join(settings.MEDIA_ROOT, image.name)

        with open(image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        result = predict_fake_news(text, image_path)

        PredictionHistory.objects.create(
            username=request.session['user'],
            text=text,
            image=image.name,
            result=result
        )

    return render(request, 'predict.html', {'result': result})

# =========================
# HISTORY
# =========================
def history(request):
    if not request.session.get('user'):
        return redirect('login')

    records = PredictionHistory.objects.filter(
        username=request.session['user']
    )
    return render(request, 'history.html', {'records': records})

# =========================
# USER LOGOUT
# =========================
def logout(request):
    request.session.flush()
    return redirect('login')

# =========================
# ADMIN LOGIN
# =========================
def admin_login(request):
    error = None

    if request.method == "POST":
        if request.POST['username'] == "admin" and request.POST['password'] == "admin123":
            request.session['admin'] = True
            return redirect('admin_dashboard')
        else:
            error = "Invalid admin credentials"

    return render(request, 'admin_login.html', {'error': error})

# =========================
# ADMIN DASHBOARD
# =========================
def admin_dashboard(request):
    if not request.session.get('admin'):
        return redirect('admin_login')

    users = RegisteredUser.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users})

# =========================
# ACTIVATE / DEACTIVATE USER
# =========================
def toggle_user_status(request, user_id):
    if not request.session.get('admin'):
        return redirect('admin_login')

    user = RegisteredUser.objects.get(id=user_id)
    user.is_active = not user.is_active
    user.save()
    return redirect('admin_dashboard')

# =========================
# ADMIN LOGOUT
# =========================
def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')