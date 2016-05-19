from django.conf.urls import patterns, url
from rango import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^login/$', views.user_login, name='login'),

    url(r'^$', views.index, name='index'),
    url(r'^add_stu/$', views.add_stu, name='add_stu'),
    url(r'^(?P<student_name_slug>[\w\-]+)/$', views.student, name='student'),


]