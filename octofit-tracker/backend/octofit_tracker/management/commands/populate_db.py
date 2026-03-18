
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', first_name='Peter', last_name='Parker'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent'),
        ]

        # Activities
        Activity.objects.create(user='ironman', type='Running', duration=30)
        Activity.objects.create(user='spiderman', type='Cycling', duration=45)
        Activity.objects.create(user='batman', type='Swimming', duration=60)
        Activity.objects.create(user='superman', type='Yoga', duration=20)

        # Leaderboard
        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='spiderman', points=80)
        Leaderboard.objects.create(user='batman', points=90)
        Leaderboard.objects.create(user='superman', points=110)

        # Workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Pullups', difficulty='Medium')
        Workout.objects.create(name='Squats', difficulty='Easy')
        Workout.objects.create(name='Deadlift', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
