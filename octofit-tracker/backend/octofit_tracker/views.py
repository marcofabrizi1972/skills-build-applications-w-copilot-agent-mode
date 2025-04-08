from django.views import View
from django.http import JsonResponse
from django.conf import settings
from .models import User, Team, Activity, Leaderboard, Workout

#create a root endpoint that returns the available endpoints
def api_root(request):
    base_url = "https://solid-zebra-6996vqv59x94c4544-8000.app.github.dev"
    return JsonResponse({
        "users": f"{base_url}/users/",
        "teams": f"{base_url}/teams/",
        "activities": f"{base_url}/activities/",
        "leaderboard": f"{base_url}/leaderboard/",
        "workouts": f"{base_url}/workouts/",
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
