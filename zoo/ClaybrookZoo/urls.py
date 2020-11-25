from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.home),
    path('site/<str:location>',views.site),
    path('animal',views.animal),
    path('message',views.message),
    path('adminpanel/<str:display>/<str:action>/<int:id>',views.adminpanel),
    path('visitorpanel/<str:display>/<str:action>/<int:id>',views.visitorpanel),
    path('password',auth_views.PasswordChangeView.as_view(template_name='signup.html')),
    path('signup/<str:action>',views.signup,name='signup'),
    path('payment/<str:action>', views.payment),    
]
