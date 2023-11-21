from django.contrib import admin
from django.urls import path
from staff import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.views_staff, name='view_all'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('add_position/', views.add_position, name='add_position'),
    path('positions/', views.positions_list, name='positions_list'),
    path('edit_position/<int:position_id>/', views.edit_position, name='edit_position'),
    path('delete_position/<int:position_id>/', views.delete_position, name='delete_position'),
    path('search/', views.search, name='search'),
]
