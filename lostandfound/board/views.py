from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import FoundItem
from .forms import FoundItemForm, RegisterForm

def homepage(request):
    items = FoundItem.objects.all().order_by('-created_at')
    return render(request, 'homepage.html', {'items': items})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('homepage')
    else:
        form = FoundItemForm()
    return render(request, 'add_item.html', {'form': form})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id, user=request.user)
    item.delete()
    return redirect('homepage')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id, user=request.user)
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = FoundItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})