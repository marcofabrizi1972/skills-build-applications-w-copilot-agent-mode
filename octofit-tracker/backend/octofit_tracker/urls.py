from django.contrib import admin
from django.urls import path, include
from .views import UserView, TeamView, ActivityView, LeaderboardView, WorkoutView, api_root

urlpatterns = [
    path('', api_root, name='api-root'),  # Root endpoint
    path('users/', UserView.as_view(), name='user-list'),
    path('teams/', TeamView.as_view(), name='team-list'),
    path('activities/', ActivityView.as_view(), name='activity-list'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard-list'),
    path('workouts/', WorkoutView.as_view(), name='workout-list'),
    path('admin/', admin.site.urls),  # Admin endpoint
]
