"""jobMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from core.views import index,login,signup,jobpost,profile,jobdetails,logout_view,post_search,delete_post,upload_document,job_cv,fetch_document
from core.forms import LoginForm, SendEmail, ConfirmPassword,PasswordChange

urlpatterns = [
    # Basic Routes
    path('',index,name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/',signup,name='signup'),
    path('jobs/',jobpost,name='jobpost'),
    path('profile/',profile,name='profile'),
    path('job/<int:pk>/',jobdetails,name='jobdetails'),
    path('admin/', admin.site.urls),
    # Reset and Change Password
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='core/password_reset_form.html',form_class=SendEmail),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html',form_class=ConfirmPassword,success_url ='/login'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'),name='password_reset_complete'),
    path('change/password/',auth_views.PasswordChangeView.as_view(template_name='core/change_password.html',form_class=PasswordChange,success_url ='/'),name='change_password'),
    # Search Password
    path('search/', post_search, name='post_search'),
    # Delete Post
    path('post/delete/<int:post_id>/', delete_post, name='delete_post'),
    # Post Cv
    path('upload/', upload_document, name='upload_document'),
    # Get Cv
    path('cv/<int:pk>', job_cv, name='job_cv'),
    path('fetch/', fetch_document, name='fetch_document'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
