from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('out/', views.user_logout_view.as_view(), name='user_logout'),
    path('profile/', views.profileupdate, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/edit/pass_change/', views.password_change, name='pass_change'),
    path('details/<int:pk>/', views.CarDetailsView.as_view(), name='car_details_view'),
    path("buy/<int:id>", views.buy_now, name="buy_car")
    

]