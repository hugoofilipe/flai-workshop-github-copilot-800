from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'team_id', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'date', 'notes']
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'team_id', 'total_points', 'total_activities', 'total_calories', 'last_updated']
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'category', 'difficulty', 'duration', 'calories_estimate']
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None
