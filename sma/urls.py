from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    # JGarza 12Apr2020 reset site
    path("change-password/", views.change_password, name="change_password"),
    path("staff-login/", views.staffLogin, name='staffLogin'),
    path("mentor-login/", views.mentorLogin, name='mentorLogin'),

    path("staff-signup/", views.staffSignup, name='staffSignup'),
    path("mentor-signup/", views.mentorSignup, name='mentorSignup'),

    path("logout/", views.user_logout, name='user_logout'),
    path('session_list', views.session_list, name='session_list'),
    path('session_details/<int:pk>/', views.session_details, name='session_details'),

    # Jgarza 3/27/2020
    # Created email urls
    path('email/', views.email_form, name='email'),
    path('success/', TemplateView.as_view(template_name='email_success.html'), name='success'),
    path('review/submit/<int:pk1>/<int:pk2>/',views.review_class_form,name='review'),
    path('review/<int:pk1>/<int:pk2>/',views.review_form,name='reviewform'),
    path('attendance/<int:pk1>/<int:pk2>/',views.submitattendance,name='submitAttendance'),

    # Jgarza 4/11/2020
    # added email class urls
    path('class_email/', views.email_class_form, name='class_email'),
    url(r'^class_email/(?P<grade>[^\n]+)/$', views.email_class_form, name='class_email'),
]
