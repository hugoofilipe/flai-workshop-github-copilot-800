from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users.
    Supports list, create, retrieve, update, and delete operations.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get all activities for a specific user"""
        user = self.get_object()
        activities = Activity.objects.filter(user_id=str(user._id))
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams.
    Supports list, create, retrieve, update, and delete operations.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        """Get all members of a specific team"""
        team = self.get_object()
        members = User.objects.filter(team_id=str(team._id))
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities.
    Supports list, create, retrieve, update, and delete operations.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
    def get_queryset(self):
        """Allow filtering activities by user_id via query parameter"""
        queryset = Activity.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for leaderboard.
    Supports list, create, retrieve, update, and delete operations.
    """
    queryset = Leaderboard.objects.all().order_by('-total_points')
    serializer_class = LeaderboardSerializer
    
    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get leaderboard grouped by team"""
        team_id = request.query_params.get('team_id', None)
        if team_id:
            leaderboard = Leaderboard.objects.filter(team_id=team_id).order_by('-total_points')
        else:
            leaderboard = Leaderboard.objects.all().order_by('-total_points')
        serializer = self.get_serializer(leaderboard, many=True)
        return Response(serializer.data)


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workouts.
    Supports list, create, retrieve, update, and delete operations.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    
    def get_queryset(self):
        """Allow filtering workouts by category and difficulty"""
        queryset = Workout.objects.all()
        category = self.request.query_params.get('category', None)
        difficulty = self.request.query_params.get('difficulty', None)
        
        if category is not None:
            queryset = queryset.filter(category=category)
        if difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty)
        
        return queryset
