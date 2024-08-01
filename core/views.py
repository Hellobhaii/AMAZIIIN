from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm


from .forms import UpdateProfileForm
from django.contrib import messages

from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required
def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
    
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "core/logout.html", {})



@login_required
def profile(request):
    return render(request, 'core/profile.html')

from django.contrib.auth.hashers import make_password
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_new_password')
        if form.is_valid():
            if password and confirm_password:
                if password == confirm_password:
                    request.user.password = make_password(password)
                    request.user.save()
                    messages.success(request, 'Password changed successfully!')
                else:
                    messages.error(request, 'New passwords do not match!')
            form.save()
            return redirect('/core/profile/')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'core/update_profile.html', {'form': form})