from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

# Uncomment to enable app namespacing
# app_name = 'student'

urlpatterns = [
    path('studentclick', views.studentclick_view, name='studentclick'),
    path('studentlogin', LoginView.as_view(template_name='student/studentlogin.html'), name='studentlogin'),
    path('studentsignup', views.student_signup_view, name='studentsignup'),
    path('student-dashboard', views.student_dashboard_view, name='student-dashboard'),
    path('student-exam', views.student_exam_view, name='student-exam'),
    path('take-exam/<int:pk>', views.take_exam_view, name='take-exam'),
    path('start-exam/<int:pk>', views.start_exam_view, name='start-exam'),
    path('log-activity/', views.log_activity, name='log_activity'),
    path('calculate-marks', views.calculate_marks_view, name='calculate-marks'),
    path('view-result', views.view_result_view, name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view, name='check-marks'),
    path('student-marks', views.student_marks_view, name='student-marks'),
]
