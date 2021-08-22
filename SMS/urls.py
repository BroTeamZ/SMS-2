"""SMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from SMS import settings
from SMS_app import views,HostView, StudentView, Subjectview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('broteam/',views.Broteam),
    path('',views.ShowMainPage,name="show_main"),
    path('SMS/login',views.ShowLoginPage,name="show_login"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home',HostView.admin_home,name="admin_home"),
    path('add_teacher',HostView.add_teacher,name="add_teacher"),
    path('add_teacher_save',HostView.add_teacher_save,name="add_teacher_save"),
    path('check_email_exist', HostView.check_email_exist,name="check_email_exist"),
    path('check_username_exist', HostView.check_username_exist,name="check_username_exist"),
    path('manage_teacher', HostView.manage_teacher,name="manage_teacher"),
    path('add_student', HostView.add_student,name="add_student"),
    path('add_student_save', HostView.add_student_save,name="add_student_save"),
    path('add_class', HostView.add_class,name="add_class"),
    path('add_class_save', HostView.add_class_save,name="add_class_save"),
    path('manage_student', HostView.manage_student,name="manage_student"),
    path('manage_class', HostView.manage_class,name="manage_class"),
    path('manage_session', HostView.manage_session,name="manage_session"),
    path('add_session_save', HostView.add_session_save,name="add_session_save"),
    path('edit_student/<str:student_id>', HostView.edit_student,name="edit_student"),
    path('edit_student_save', HostView.edit_student_save,name="edit_student_save"),
    path('edit_teacher/<str:teacher_id>', HostView.edit_teacher,name="edit_teacher"),
    path('edit_teacher_save', HostView.edit_teacher_save,name="edit_teacher_save"),
    path('home_student/', StudentView.home, name="student_home"),
    path('hk<str:term>/<str:student_id>/<str:Class>', StudentView.hk1, name="hk1"),
    path('add_physics/', Subjectview.add_update_physics, name='physics'),
    path('add_math/', Subjectview.add_update_math, name="math"),
    path('add_chemistry/', Subjectview.add_update_chemistry, name="chemistry"),
    path('add_language/', Subjectview.add_update_language, name="language"),
    path('add_literature/', Subjectview.add_update_literature, name="literature"),
    path('add_bio/', Subjectview.add_update_bilogy, name="bio"),
    path('add_history/', Subjectview.add_update_history, name="history"),
    path('add_geography/', Subjectview.add_update_geography, name="geo"),
    path('add_IT/', Subjectview.add_update_IT, name="IT"),
    path('add_edu/', Subjectview.add_update_edu, name="edu"),
    path('add_profession/', Subjectview.add_update_profession, name="profession",),
    path('add_defence/', Subjectview.add_update_defence, name="defence"),
    path('add_technology/', Subjectview.add_update_technology, name="technology"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

