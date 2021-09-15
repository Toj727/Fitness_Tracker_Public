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
  path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
  path('dashboard/create/', views.WeightCreate.as_view(), name='weight_create'),
  # path('regerror/', views.HomeError.as_view(), name='reg_error'),
  # path('posts/<int:pk>/', views.PostDetails.as_view(),  name='post_details')
]