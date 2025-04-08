from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson import ObjectId
from datetime import timedelta
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connetti a MongoDB
        client = MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
        db = client[settings.MONGO_DB_NAME]

        # Cancella i dati esistenti
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Crea utenti
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Crea team
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[2]["_id"], users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Crea attività
        activities = [
            {"_id": ObjectId(), "activity_id": 1, "user": users[0]["_id"], "activity_type": "Cycling", "duration": timedelta(hours=1).total_seconds()},
            {"_id": ObjectId(), "activity_id": 2, "user": users[1]["_id"], "activity_type": "Crossfit", "duration": timedelta(hours=2).total_seconds()},
            {"_id": ObjectId(), "activity_id": 3, "user": users[2]["_id"], "activity_type": "Running", "duration": timedelta(hours=1, minutes=30).total_seconds()},
            {"_id": ObjectId(), "activity_id": 4, "user": users[3]["_id"], "activity_type": "Strength", "duration": timedelta(minutes=30).total_seconds()},
            {"_id": ObjectId(), "activity_id": 5, "user": users[4]["_id"], "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15).total_seconds()},
        ]
        db.activity.insert_many(activities)

        # Crea leaderboard
        leaderboard = [
            {"_id": ObjectId(), "leaderboard_id": 1, "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "leaderboard_id": 2, "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "leaderboard_id": 3, "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "leaderboard_id": 4, "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "leaderboard_id": 5, "user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Crea allenamenti
        workouts = [
            {"_id": ObjectId(), "workout_id": 1, "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "workout_id": 2, "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "workout_id": 3, "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "workout_id": 4, "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "workout_id": 5, "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
