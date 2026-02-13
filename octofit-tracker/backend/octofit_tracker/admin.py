from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ['name', 'email', 'team_id', 'created_at']
    list_filter = ['created_at', 'team_id']
    search_fields = ['name', 'email']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ['name', 'description', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ['user_id', 'activity_type', 'duration', 'distance', 'calories', 'date']
    list_filter = ['activity_type', 'date']
    search_fields = ['user_id', 'activity_type', 'notes']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ['user_id', 'team_id', 'total_points', 'total_activities', 'total_calories', 'last_updated']
    list_filter = ['team_id', 'last_updated']
    search_fields = ['user_id', 'team_id']
    ordering = ['-total_points']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ['title', 'category', 'difficulty', 'duration', 'calories_estimate']
    list_filter = ['category', 'difficulty']
    search_fields = ['title', 'description', 'category']
    ordering = ['title']
