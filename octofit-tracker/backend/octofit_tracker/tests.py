from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserAPITestCase(APITestCase):
    """Test cases for User API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            password="testpass123"
        )
    
    def test_list_users(self):
        """Test retrieving list of users"""
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_create_user(self):
        """Test creating a new user"""
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(reverse('user-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITestCase(APITestCase):
    """Test cases for Team API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )
    
    def test_list_teams(self):
        """Test retrieving list of teams"""
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_create_team(self):
        """Test creating a new team"""
        data = {
            'name': 'New Team',
            'description': 'A new team'
        }
        response = self.client.post(reverse('team-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITestCase(APITestCase):
    """Test cases for Activity API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name="Test User",
            email="activity@example.com",
            password="testpass123"
        )
        self.activity = Activity.objects.create(
            user_id=str(self.user._id),
            activity_type="Running",
            duration=30,
            distance=5.0,
            calories=300,
            date=datetime.now(),
            notes="Morning run"
        )
    
    def test_list_activities(self):
        """Test retrieving list of activities"""
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_create_activity(self):
        """Test creating a new activity"""
        data = {
            'user_id': str(self.user._id),
            'activity_type': 'Cycling',
            'duration': 45,
            'distance': 10.0,
            'calories': 400,
            'date': datetime.now().isoformat(),
            'notes': 'Evening ride'
        }
        response = self.client.post(reverse('activity-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITestCase(APITestCase):
    """Test cases for Leaderboard API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name="Test User",
            email="leader@example.com",
            password="testpass123"
        )
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )
        self.leaderboard = Leaderboard.objects.create(
            user_id=str(self.user._id),
            team_id=str(self.team._id),
            total_points=100,
            total_activities=5,
            total_calories=1500
        )
    
    def test_list_leaderboard(self):
        """Test retrieving leaderboard"""
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class WorkoutAPITestCase(APITestCase):
    """Test cases for Workout API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            title="Morning Cardio",
            description="Start your day with high energy cardio",
            category="Cardio",
            difficulty="Intermediate",
            duration=30,
            calories_estimate=250
        )
    
    def test_list_workouts(self):
        """Test retrieving list of workouts"""
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_create_workout(self):
        """Test creating a new workout"""
        data = {
            'title': 'Evening Yoga',
            'description': 'Relaxing yoga session',
            'category': 'Flexibility',
            'difficulty': 'Beginner',
            'duration': 20,
            'calories_estimate': 100
        }
        response = self.client.post(reverse('workout-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_filter_workouts_by_category(self):
        """Test filtering workouts by category"""
        response = self.client.get(reverse('workout-list'), {'category': 'Cardio'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTestCase(APITestCase):
    """Test cases for API root endpoint"""
    
    def test_api_root(self):
        """Test that API root returns all endpoints"""
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
