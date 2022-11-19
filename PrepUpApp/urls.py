from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage, name='LandingPage'),
    path('dashboard', views.Dashboard, name='Dashboard'),
    path('login', views.LoginPage, name='Loginpage'),
    path('logout', views.logoutUser, name='Logout'),
    path('signup', views.SignUp, name='Signup'),
    path('profile/<str:username>/', views.Profile, name='Profile'),
    path('interviewschedule', views.InterviewSchedule, name='InterviewSchedule'),
    path('uploadmaterial', views.Uploadmaterial, name='Uploadmaterial'),
    path('suggestamaterial', views.Suggestamaterial, name='Suggestamaterial'),
    path('successstories', views.SuccessStories, name='SuccessStories'),
    path('rooms', views.Rooms, name='Rooms'),
    path('createrooms', views.Createarooms, name='Createarooms'),
    path('insideroom/<str:pk>/', views.Insideroom, name='Insideroom'),
    path('updateroom/<str:pk>/', views.Updateroom, name='Updateroom'),
    path('deleteroom/<str:pk>/', views.DeleteRoom, name='DeleteRoom'),
    path('searchresult', views.Searchresult, name='Searchresult'),
    path('interviewresult', views.InterviewResult, name='InterviewResult'),
    path('successstory', views.Successstory, name='Successstory'),
]
