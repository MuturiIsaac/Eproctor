"""Nocturnal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.1/topics/http/urls/

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
from django.urls import include, path
from django.contrib import admin
from hacklympics.views import user, course, exam, problem, answer, message, proctor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/online', user.list_online),
    path('exam/ongoing', exam.list_ongoing),
    path('user', user.list),
    path('user/login', user.login),
    path('user/logout', user.logout),
    path('user/register', user.register),
    path('user/reset', user.reset),
    path('user/<str:username>', user.get),
    path('course', course.list),
    path('course/create', course.create),
    path('course/update', course.update),
    path('course/remove', course.remove),
    path('course/<str:c_id>', course.get),
    path('course/<int:c_id>/exam', exam.list),
    path('course/<int:c_id>/exam/create', exam.create),
    path('course/<int:c_id>/exam/update', exam.update),
    path('course/<int:c_id>/exam/remove', exam.remove),
    path('course/<int:c_id>/exam/launch', exam.launch),
    path('course/<int:c_id>/exam/halt', exam.halt),
    path('course/<int:c_id>/exam/attend', exam.attend),
    path('course/<int:c_id>/exam/leave', exam.leave),
    path('course/<int:c_id>/exam/<int:e_id>', exam.get),
    path('course/<int:c_id>/exam/<int:e_id>/owner', exam.get_owner),
    path('course/<int:c_id>/exam/<int:e_id>/remaining_time', exam.get_remaining_time),
    path('course/<int:c_id>/exam/<int:e_id>/message/create', message.create),
    path('course/<int:c_id>/exam/<int:e_id>/proctor/sync_snapshot', proctor.sync_snapshot),
    path('course/<int:c_id>/exam/<int:e_id>/proctor/sync_keystrokes', proctor.sync_keystrokes),
    path('course/<int:c_id>/exam/<int:e_id>/proctor/adjust_params', proctor.adjust_params),
    path('course/<int:c_id>/exam/<int:e_id>/problem', problem.list),
    path('course/<int:c_id>/exam/<int:e_id>/problem/create', problem.create),
    path('course/<int:c_id>/exam/<int:e_id>/problem/update', problem.update),
    path('course/<int:c_id>/exam/<int:e_id>/problem/remove', problem.remove),
    path('course/<int:c_id>/exam/<int:e_id>/problem/<int:p_id>', problem.get),
    path('course/<int:c_id>/exam/<int:e_id>/problem/<int:p_id>/answer', answer.list),
    path('course/<int:c_id>/exam/<int:e_id>/problem/<int:p_id>/answer/create', answer.create),
    path('course/<int:c_id>/exam/<int:e_id>/problem/<int:p_id>/answer/update', answer.update),
    path('course/<int:c_id>/exam/<int:e_id>/problem/<int:p_id>/answer/remove', answer.remove),
    path('course/<int:c_id>/exam/<int:e_id>/problem/<int:p_id>/answer/validate', answer.validate),
    path('course/<int:c_id>/exam/<int:e_id>/problem/<int:p_id>/answer/<int:a_id>', answer.get)
]