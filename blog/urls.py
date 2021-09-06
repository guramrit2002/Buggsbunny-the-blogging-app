from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('about/', include('blogs.urls')),
    path('register/', user_views.register, name= 'Blog-register'),
    path('profile/', user_views.profile, name= 'Blog-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name= 'Blog-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name= 'Blog-logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name= 'blog-password-reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='blog_password_reset_done'),   
    # path('password_reset/confirm/<>uidb64/token/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name= 'blog-password-reset-confirm'),
    path('', include('blogs.urls')),
]
if settings.DEBUG :
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)