from django.contrib import admin
from django.urls import path, re_path
from . import views
app_name='Restapp'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login_view/', views.login_view, name='login_view'),
    path(' logout_view /', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('department/<str:department>/', views.department_view, name='department_view'),
    path('new_page/',views.new_page,name='new_page'),
    path('form_page/', views.form_page, name='form_page'),
    path('form_confirm/', views.form_confirm, name='form_confirm'),
    path('submit_form/',views.submit_form, name='submit_form'),
    # # path('single_template/', views.single_template_view, name='single_template'),
    # path('get_courses/', views.get_courses, name='get_courses'),
]


