from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
from bson import ObjectId


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes united in fitness'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League fitness warriors'
        )
        
        # Create Users (Superheroes)
        self.stdout.write('Creating superhero users...')
        
        # Marvel Heroes
        iron_man = User.objects.create(
            name='Tony Stark',
            email='ironman@marvel.com',
            password='stark123',
            team_id=str(team_marvel._id)
        )
        
        captain_america = User.objects.create(
            name='Steve Rogers',
            email='cap@marvel.com',
            password='shield123',
            team_id=str(team_marvel._id)
        )
        
        black_widow = User.objects.create(
            name='Natasha Romanoff',
            email='blackwidow@marvel.com',
            password='widow123',
            team_id=str(team_marvel._id)
        )
        
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@marvel.com',
            password='hammer123',
            team_id=str(team_marvel._id)
        )
        
        hulk = User.objects.create(
            name='Bruce Banner',
            email='hulk@marvel.com',
            password='smash123',
            team_id=str(team_marvel._id)
        )
        
        # DC Heroes
        batman = User.objects.create(
            name='Bruce Wayne',
            email='batman@dc.com',
            password='gotham123',
            team_id=str(team_dc._id)
        )
        
        superman = User.objects.create(
            name='Clark Kent',
            email='superman@dc.com',
            password='krypton123',
            team_id=str(team_dc._id)
        )
        
        wonder_woman = User.objects.create(
            name='Diana Prince',
            email='wonderwoman@dc.com',
            password='themyscira123',
            team_id=str(team_dc._id)
        )
        
        flash = User.objects.create(
            name='Barry Allen',
            email='flash@dc.com',
            password='speed123',
            team_id=str(team_dc._id)
        )
        
        aquaman = User.objects.create(
            name='Arthur Curry',
            email='aquaman@dc.com',
            password='atlantis123',
            team_id=str(team_dc._id)
        )
        
        # Create Activities
        self.stdout.write('Creating activities...')
        
        marvel_heroes = [iron_man, captain_america, black_widow, thor, hulk]
        dc_heroes = [batman, superman, wonder_woman, flash, aquaman]
        all_heroes = marvel_heroes + dc_heroes
        
        activity_types = ['Running', 'Swimming', 'Cycling', 'Weight Training', 'Boxing', 'Yoga']
        
        # Create activities for the past 7 days
        for day in range(7):
            date = datetime.now() - timedelta(days=day)
            for hero in all_heroes:
                # Each hero does 1-3 activities per day
                import random
                num_activities = random.randint(1, 3)
                for _ in range(num_activities):
                    activity_type = random.choice(activity_types)
                    duration = random.randint(30, 120)
                    distance = random.uniform(1.0, 10.0) if activity_type in ['Running', 'Swimming', 'Cycling'] else None
                    calories = duration * random.randint(5, 10)
                    
                    Activity.objects.create(
                        user_id=str(hero._id),
                        activity_type=activity_type,
                        duration=duration,
                        distance=round(distance, 2) if distance else None,
                        calories=calories,
                        date=date,
                        notes=f'{hero.name} crushing it with {activity_type}!'
                    )
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        
        for hero in all_heroes:
            activities = Activity.objects.filter(user_id=str(hero._id))
            total_activities = activities.count()
            total_calories = sum(a.calories for a in activities)
            total_points = total_calories // 10  # 1 point per 10 calories
            
            Leaderboard.objects.create(
                user_id=str(hero._id),
                team_id=hero.team_id,
                total_points=total_points,
                total_activities=total_activities,
                total_calories=total_calories
            )
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        
        workouts_data = [
            {
                'title': 'Superhero Strength Training',
                'description': 'Build strength like Thor with this intense weight training routine',
                'category': 'Strength',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories_estimate': 500
            },
            {
                'title': 'Speed Force Cardio',
                'description': 'Channel your inner Flash with high-intensity interval training',
                'category': 'Cardio',
                'difficulty': 'Advanced',
                'duration': 45,
                'calories_estimate': 600
            },
            {
                'title': 'Warrior Yoga Flow',
                'description': 'Find balance and flexibility like Wonder Woman',
                'category': 'Flexibility',
                'difficulty': 'Intermediate',
                'duration': 30,
                'calories_estimate': 200
            },
            {
                'title': 'Atlantean Swimming Challenge',
                'description': 'Master the waters with Aquaman\'s swimming workout',
                'category': 'Swimming',
                'difficulty': 'Intermediate',
                'duration': 40,
                'calories_estimate': 400
            },
            {
                'title': 'Avenger Endurance Run',
                'description': 'Build endurance like Captain America',
                'category': 'Cardio',
                'difficulty': 'Intermediate',
                'duration': 50,
                'calories_estimate': 550
            },
            {
                'title': 'Spider Agility Training',
                'description': 'Improve agility and quick reflexes',
                'category': 'Agility',
                'difficulty': 'Beginner',
                'duration': 25,
                'calories_estimate': 250
            },
            {
                'title': 'Kryptonian Core Workout',
                'description': 'Build a core of steel like Superman',
                'category': 'Core',
                'difficulty': 'Advanced',
                'duration': 35,
                'calories_estimate': 350
            },
            {
                'title': 'Gotham Night Patrol',
                'description': 'Stay alert and ready like Batman with this total body workout',
                'category': 'Full Body',
                'difficulty': 'Advanced',
                'duration': 70,
                'calories_estimate': 700
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
