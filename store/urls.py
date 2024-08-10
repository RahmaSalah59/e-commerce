from django.urls import path
from . import views
app_name = 'store'

urlpatterns = [
    path('',views.home,name='home'),
    path('review/<int:pk>/', views.Get_item.as_view(),name='review'),
    path('signup', views.sign_up,name='signup'),
    path('login', views.log_in,name='login'),
    path('logot',views.log_out,name='logout'),
    path('about',views.about.as_view(),name='about'),
    path('category/<slug:slug>/',views.category ,name='category'),
    

]
