# Home/management/commands/seed_data.py

import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Home.models import StreamPlatform, WatchList, Review


class Command(BaseCommand):
    help = "Seeds the database with bulk sample data for testing pagination, filtering, and throttling."

    def add_arguments(self, parser):
        parser.add_argument('--flush', action='store_true', help='Delete existing data before seeding.')
        parser.add_argument('--users', type=int, default=15, help='Number of users to create.')
        parser.add_argument('--platforms', type=int, default=6, help='Number of stream platforms to create.')
        parser.add_argument('--watchlists', type=int, default=100, help='Number of watchlist entries to create.')
        parser.add_argument('--reviews', type=int, default=300, help='Number of reviews to create.')

    def handle(self, *args, **options):
        if options['flush']:
            self.stdout.write(self.style.WARNING('Flushing existing data...'))
            Review.objects.all().delete()
            WatchList.objects.all().delete()
            StreamPlatform.objects.all().delete()
            User.objects.filter(is_superuser=False).delete()

        self.seed_users(options['users'])
        self.seed_platforms(options['platforms'])
        self.seed_watchlists(options['watchlists'])
        self.seed_reviews(options['reviews'])

        self.stdout.write(self.style.SUCCESS(
            f"\nSeeded: {len(self.users)} users, {len(self.platforms)} platforms, "
            f"{len(self.watchlists)} watchlists, {Review.objects.count()} reviews."
        ))

    # ---------- Users ----------

    def seed_users(self, count):
        self.stdout.write(f'Seeding {count} users...')
        first_names = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi',
                        'Ivan', 'Judy', 'Karl', 'Liam', 'Mona', 'Nina', 'Omar', 'Priya',
                        'Quinn', 'Rosa', 'Sam', 'Tara']
        self.users = []
        for i in range(count):
            name = first_names[i % len(first_names)]
            username = f"{name.lower()}{i}"
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': f"{username}@example.com"},
            )
            if created:
                user.set_password('testpass123')
                user.save()
            self.users.append(user)
        self.stdout.write(f"  Done. {User.objects.count()} total users in DB.")

    # ---------- Stream Platforms ----------

    def seed_platforms(self, count):
        self.stdout.write(f'Seeding {count} platforms...')
        pool = [
            ('Netflix', 'Streaming platform for movies and shows', 'https://netflix.com'),
            ('Prime Video', "Amazon's streaming platform", 'https://primevideo.com'),
            ('Disney+', 'Home for Disney, Marvel, and Star Wars content', 'https://disneyplus.com'),
            ('Hulu', 'Current TV episodes and exclusive originals', 'https://hulu.com'),
            ('HBO Max', 'Premium movies, originals, and live sports', 'https://hbomax.com'),
            ('Apple TV+', "Apple's original streaming service", 'https://tv.apple.com'),
            ('Paramount+', 'Movies, shows, and live sports from Paramount', 'https://paramountplus.com'),
            ('Peacock', "NBCUniversal's streaming platform", 'https://peacocktv.com'),
        ]
        self.platforms = []
        for pname, about, website in pool[:count]:
            platform, _ = StreamPlatform.objects.get_or_create(
                pname=pname, defaults={'about': about, 'website': website},
            )
            self.platforms.append(platform)
        self.stdout.write(f"  Done. {StreamPlatform.objects.count()} total platforms in DB.")

    # ---------- WatchLists ----------

    def seed_watchlists(self, count):
        self.stdout.write(f'Seeding {count} watchlists...')
        adjectives = ['Dark', 'Lost', 'Silent', 'Hidden', 'Final', 'Last', 'Broken', 'Golden',
                      'Wild', 'Forgotten', 'Endless', 'Secret', 'Rising', 'Falling', 'Eternal']
        nouns = ['Kingdom', 'Shadows', 'Horizon', 'Empire', 'Legacy', 'Frontier', 'City',
                 'Ocean', 'Mountain', 'Crown', 'Storm', 'Garden', 'Republic', 'Signal', 'Dawn']
        storylines = [
            "A group of unlikely heroes must band together to stop an ancient evil.",
            "A detective uncovers a conspiracy that reaches the highest levels of power.",
            "Two estranged siblings inherit a mystery neither of them wanted.",
            "A small town hides a secret that threatens to tear it apart.",
            "An astronaut stranded far from home must find a way back against all odds.",
            "A family's quiet life unravels after a shocking discovery.",
            "Rival factions clash for control in a world on the brink of collapse.",
            "A young outsider discovers powers that change everything.",
        ]

        self.watchlists = []
        for i in range(count):
            title = f"{random.choice(adjectives)} {random.choice(nouns)}"
            # allow duplicate-looking titles (realistic), so use get_or_create on a unique suffix instead
            watchlist = WatchList.objects.create(
                title=f"{title} {i}",
                storyline=random.choice(storylines),
                active=random.choice([True, True, True, False]),  # ~75% active
                platform=random.choice(self.platforms),
            )
            self.watchlists.append(watchlist)
        self.stdout.write(f"  Done. {WatchList.objects.count()} total watchlists in DB.")

    # ---------- Reviews ----------

    def seed_reviews(self, count):
        self.stdout.write(f'Seeding {count} reviews...')
        descriptions = [
            "Absolutely loved the pacing and the soundtrack.",
            "Great premise but the ending fell flat.",
            "One of the best things I've watched all year.",
            "A bit slow to start, but worth sticking with.",
            "The acting carried what was otherwise a weak script.",
            "Visually stunning, story not so much.",
            "Could not stop watching, finished it in one sitting.",
            "Decent, but won't be rewatching.",
            "Underrated gem, more people should see this.",
            "Started strong, lost steam halfway through.",
        ]

        created_count = 0
        attempts = 0
        max_attempts = count * 3  # avoid infinite loop if unique pairs run out

        # Track (user, watchlist) pairs already used, since your earlier app logic
        # blocks a user reviewing the same watchlist twice
        used_pairs = set()

        while created_count < count and attempts < max_attempts:
            attempts += 1
            user = random.choice(self.users)
            watchlist = random.choice(self.watchlists)
            pair = (user.id, watchlist.id)
            if pair in used_pairs:
                continue
            used_pairs.add(pair)

            Review.objects.create(
                review_user=user,
                rating=random.randint(1, 5),
                description=random.choice(descriptions),
                watchlist=watchlist,
            )
            created_count += 1

        self.stdout.write(f"  Done. {Review.objects.count()} total reviews in DB.")