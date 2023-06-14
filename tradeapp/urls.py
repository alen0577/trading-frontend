from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('aboutus/',views.about,name='about'),
    path('help/',views.contact,name='contact'),
    path('demataccount/',views.demat,name='demat'),
    path('solution/',views.solution,name='solution'),
    path('xlearn/',views.xlearn,name='xlearn'),
    path('tutorials/',views.tutorials,name='tutorials'),
]
