from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Create teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')

        # Add users to teams (example, adjust as needed)
        team1.members = [user1, user2]
        team2.members = [user3]
        team1.save()
        team2.save()

        # Create activities
        Activity.objects.create(user=user1, activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=user2, activity_type='walk', duration=45, date=timezone.now())
        Activity.objects.create(user=user3, activity_type='cycle', duration=60, date=timezone.now())

        # Create leaderboard
        Leaderboard.objects.create(team=team1, points=150)
        Leaderboard.objects.create(team=team2, points=100)

        # Create workouts
        Workout.objects.create(user=user1, workout_type='cardio', details='30 min run', date=timezone.now())
        Workout.objects.create(user=user2, workout_type='strength', details='45 min weights', date=timezone.now())
        Workout.objects.create(user=user3, workout_type='yoga', details='60 min yoga', date=timezone.now())

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
