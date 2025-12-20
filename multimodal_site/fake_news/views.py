from .models import PredictionHistory
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import RegisteredUser
from .ml_model import predict_fake_news
from django.conf import settings
import os
def index(request):
    # If user already logged in → go to home
    if request.session.get('user'):
        return redirect('home')
    return render(request, 'index.html')
# =========================
# USER REGISTRATION
# =========================
def register(request):
    # 🔐 If already logged in, go to home
    if request.session.get('user'):
        return redirect('home')

    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})
# =========================
# USER LOGIN
# =========================
def login(request):
    # 🔐 If already logged in, go to home
    if request.session.get('user'):
        return redirect('home')

    error = None

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = RegisteredUser.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            if user.is_active:
                request.session['user'] = user.username
                return redirect('home')
            else:
                error = "Your account is not activated by admin"
        else:
            error = "Invalid username or password"

    return render(request, 'login.html', {'error': error})

# =========================
# USER HOME PAGE
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

        # 🔮 Prediction
        result = predict_fake_news(text, image_path)

        # ✅ SAVE HISTORY (THIS WAS MISSING)
        PredictionHistory.objects.create(
            username=request.session.get('user'),
            text=text,
            image=image.name,
            result=result
        )

    return render(request, 'predict.html', {'result': result})

def history(request):
    if not request.session.get('user'):
        return redirect('login')

    records = PredictionHistory.objects.filter(
        username=request.session.get('user')
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
        username = request.POST['username']
        password = request.POST['password']

        if username == "admin" and password == "admin123":
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
def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')
def training(request):
    if not request.session.get('user'):
        return redirect('login')

    return render(request, 'training.html')
def index(request):
    request.session.flush()  # 🔥 FORCE clear session
    return render(request, 'index.html')
def login(request):
    error = None

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = RegisteredUser.objects.filter(
            username=username,
            password=password,
            is_active=True
        ).first()

        if user:
            request.session['user'] = user.username
            return redirect('home')
        else:
            error = "Invalid credentials or user not activated"

    return render(request, 'login.html', {'error': error})
def training(request):
    if not request.session.get('user'):
        return redirect('login')
    return render(request, 'training.html')
def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')
# =========================
# ADMIN LOGOUT
# =========================
def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')