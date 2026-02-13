from djongo import models


class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    team_id = models.CharField(max_length=24, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=24)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in km
    calories = models.IntegerField()
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'activities'
    
    def __str__(self):
        return f"{self.activity_type} - {self.duration} mins"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=24)
    team_id = models.CharField(max_length=24)
    total_points = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    total_calories = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
    
    def __str__(self):
        return f"User {self.user_id} - {self.total_points} points"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20)
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.title
