from django.urls import path
from. import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('contact',views.contact,name='contact'),
    path('save',views.save,name='save'),
    path('login',views.login,name='login'),
    path('login_logic',views.login_logic,name='login_logic'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    path('change-password',views.change,name='change'),
    path('update',views.update,name='update'),
    path('apply',views.apply,name='apply'),
    path('save_course',views.save_course,name='save_course'),
    path('admin_register',views.admin_register,name='admin_register'),
    path('admin_save',views.admin_save,name='admin_save'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_login_logic',views.admin_login_logic,name='admin_login_logic'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('students_list',views.students_list,name='students_list'),
    path('courses_list',views.courses_list,name='courses_list'),
    path('delete_student',views.delete_student,name='delete_student'),
    path('delete_course',views.delete_course,name='delete_course'),
]