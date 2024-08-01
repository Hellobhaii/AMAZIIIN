from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

# from .views import logout_view
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/',views.logout_view, name = 'logout'),
    path('core/profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    # path('profile/updated/', views.updated_profile, name='updated_profile'),
]