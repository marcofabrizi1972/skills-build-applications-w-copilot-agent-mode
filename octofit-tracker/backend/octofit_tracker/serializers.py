from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class ObjectIdField:
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer:
    def __init__(self, many=False):
        self.many = many

    _id = ObjectIdField()

    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer:
    _id = ObjectIdField()
    members = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer:
    _id = ObjectIdField()
    user = ObjectIdField()

    class Meta:
        model = Activity
        fields = '__all__'

class LeaderboardSerializer:
    _id = ObjectIdField()
    user = UserSerializer()  # Expand the user object

    class Meta:
        model = Leaderboard
        fields = '__all__'

class WorkoutSerializer:
    _id = ObjectIdField()

    class Meta:
        model = Workout
        fields = '__all__'
