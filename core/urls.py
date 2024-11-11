from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assignment/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),  # Updated this line
    path('my-assignments/', views.my_assignments, name='my_assignments'),
    path('create-assignment/', views.create_assignment, name='create_assignment'),
    path('deactivate-assignment/<int:assignment_id>/', views.deactivate_assignment, name='deactivate_assignment'),
    path('delete-assignment/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
    path('request-meeting/<int:assignment_id>/', views.request_meeting, name='request_meeting'), # added this line
]