
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from main.views import Tagdetail,Categorydetail
from main import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('signIn/', views.signIn_view),
    path('posts/', views.postlist_view, name="posts"),
    path('posts/<int:pk>/', views.postdetail_view, name='postdetail'),
    path('register/', views.register, name='register'),
    path('report/', views.report, name='report'),
    path('CategoryCreating/', views.category, name='categoryCreating'),
    path('tagCreating/', views.tag, name='tagCreating'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('tags/<int:tag_id>', Tagdetail.as_view(), name='tagdetail'),
    path('categories/<int:category_id>', Categorydetail.as_view(), name='categorydetail'),
    path('posts/<int:pk>/preference/<int:userpreference>/', views.postpreference, name='postpreference'),

]


