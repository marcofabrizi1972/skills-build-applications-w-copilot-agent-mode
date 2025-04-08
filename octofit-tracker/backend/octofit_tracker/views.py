from django.views import View
from django.http import JsonResponse
from .models import User, Team, Activity, Leaderboard, Workout

#create a root endpoint that returns the available endpoints
def api_root(request):
    return JsonResponse({
        "users": "/users/",
        "teams": "/teams/",
        "activities": "/activities/",
        "leaderboard": "/leaderboard/",
        "workouts": "/workouts/",
    })

class UserView(View):
    def get(self, request):
        users = list(User.objects.values())
        return JsonResponse(users, safe=False)

class TeamView(View):
    def get(self, request):
        teams = list(Team.objects.values())
        return JsonResponse(teams, safe=False)

class ActivityView(View):
    def get(self, request):
        activities = list(Activity.objects.values())
        return JsonResponse(activities, safe=False)

class LeaderboardView(View):
    def get(self, request):
        leaderboard = list(Leaderboard.objects.values())
        return JsonResponse(leaderboard, safe=False)

class WorkoutView(View):
    def get(self, request):
        workouts = list(Workout.objects.values())
        return JsonResponse(workouts, safe=False)
