from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.About.as_view(), name="about"),
  path('profile/', views.ProfileView.as_view(), name="profile"),
  path('profile/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
  path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile_update"),
  path('accounts/signup/', views.Signup.as_view(), name='signup'),
  path('dashboard/<int:pk>/', views.Dashboard.as_view(), name="dashboard"),
  path('dashboard/weightcreate/', views.WeightCreate.as_view(), name='weight_create'),
  path('dashboard/<int:pk>/weight_delete/', views.WeightDelete.as_view(), name="weight_delete"),
  path('dashboard/createsleep/', views.SleepCreate.as_view(), name='sleep_create'),
  path('dashboard/<int:pk>/sleep_delete/', views.SleepDelete.as_view(), name="sleep_delete")
  # path('regerror/', views.HomeError.as_view(), name='reg_error'),
  # path('posts/<int:pk>/', views.PostDetails.as_view(),  name='post_details')
]