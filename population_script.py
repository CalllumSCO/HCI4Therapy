import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "djangoProject.settings")

import django

django.setup()
from django.contrib.auth.models import User
from mental_health_diary.models import ActivityType, Activity, ActivityEntry, Entry, Article
from mental_health_diary.views import generate_random_slug
from datetime import date


def populate(silent=False):
    user = User.objects.create(username="Test_User",
                               email='test.user@testing.com',
                               password='testing123')

    ActivityTypes = [
        {"type": "Physical"},
        {"type": "Social"},
        {"type": "Academic"},
        {"type": "Career"},
        {"type": "Mindfulness"},
        {"type": "Hobbies"},
        {"type": "Creative"},
        {"type": "Family"},
    ]

    for t in ActivityTypes:
        print(t)
        a = add_activity_type(t["type"])

    Activities = [
        {"activity": "Going to the Gym",
         "type": ActivityType.objects.get(type="Physical")},
        {"activity": "Running",
         "type": ActivityType.objects.get(type="Physical")},
        {"activity": "Hiking",
         "type": ActivityType.objects.get(type="Physical")},
        {"activity": "Partying",
         "type": ActivityType.objects.get(type="Social")},
        {"activity": "Hanging out with Friends",
         "type": ActivityType.objects.get(type="Social")},
        {"activity": "Studying",
         "type": ActivityType.objects.get(type="Academic")},
        {"activity": "Attending Classes",
         "type": ActivityType.objects.get(type="Academic")},
        {"activity": "Working Overtime",
         "type": ActivityType.objects.get(type="Career")},
        {"activity": "Training",
         "type": ActivityType.objects.get(type="Career")},
        {"activity": "Meditation",
         "type": ActivityType.objects.get(type="Mindfulness")},
        {"activity": "Mental Health Coaching",
         "type": ActivityType.objects.get(type="Mindfulness")},
        {"activity": "Playing Video Games",
         "type": ActivityType.objects.get(type="Hobbies")},
        {"activity": "Hobbies",
         'type': ActivityType.objects.get(type="Hobbies")},
        {"activity": "Playing an Instrument",
         'type': ActivityType.objects.get(type="Creative")},
        {'activity': 'Creating Art',
         'type': ActivityType.objects.get(type="Creative")},
        {'activity': 'Family Time',
         'type': ActivityType.objects.get(type="Family")},
        {'activity': 'Caring for Children',
         'type': ActivityType.objects.get(type="Family")}
    ]

    for activity in Activities:
        a = add_activity(activity["activity"], activity["type"])

    ActivityEntries = [
        {'time': 60,
         'activity': Activity.objects.get(activity='Going to the Gym'),
         'date': date(2022, 11, 23),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 20,
         'activity': Activity.objects.get(activity='Playing an Instrument'),
         'date': date(2022, 11, 23),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 120,
         'activity': Activity.objects.get(activity='Playing Video Games'),
         'date': date(2022, 11, 23),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 30,
         'activity': Activity.objects.get(activity='Working Overtime'),
         'date': date(2022, 11, 23),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 30,
         'activity': Activity.objects.get(activity='Mental Health Coaching'),
         'date': date(2022, 11, 23),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 20,
         'activity': Activity.objects.get(activity='Running'),
         'date': date(2022, 11, 22),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 180,
         'activity': Activity.objects.get(activity='Training'),
         'date': date(2022, 11, 22),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 10,
         'activity': Activity.objects.get(activity='Meditation'),
         'date': date(2022, 11, 22),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 60,
         'activity': Activity.objects.get(activity='Playing Video Games'),
         'date': date(2022, 11, 22),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 30,
         'activity': Activity.objects.get(activity='Working Overtime'),
         'date': date(2022, 11, 22),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 10,
         'activity': Activity.objects.get(activity='Playing an Instrument'),
         'date': date(2022, 11, 22),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 10,
         'activity': Activity.objects.get(activity='Meditation'),
         'date': date(2022, 11, 21),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 120,
         'activity': Activity.objects.get(activity='Playing Video Games'),
         'date': date(2022, 11, 21),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 30,
         'activity': Activity.objects.get(activity='Playing an Instrument'),
         'date': date(2022, 11, 21),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 45,
         'activity': Activity.objects.get(activity='Hobbies'),
         'date': date(2022, 11, 21),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 20,
         'activity': Activity.objects.get(activity='Working Overtime'),
         'date': date(2022, 11, 21),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 300,
         'activity': Activity.objects.get(activity='Hiking'),
         'date': date(2022, 11, 20),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 30,
         'activity': Activity.objects.get(activity='Hobbies'),
         'date': date(2022, 11, 20),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 10,
         'activity': Activity.objects.get(activity='Meditation'),
         'date': date(2022, 11, 20),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 180,
         'activity': Activity.objects.get(activity='Partying'),
         'date': date(2022, 11, 19),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 180,
         'activity': Activity.objects.get(activity='Playing Video Games'),
         'date': date(2022, 11, 19),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 120,
         'activity': Activity.objects.get(activity='Working Overtime'),
         'date': date(2022, 11, 18),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 180,
         'activity': Activity.objects.get(activity='Training'),
         'date': date(2022, 11, 18),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 30,
         'activity': Activity.objects.get(activity='Studying'),
         'date': date(2022, 11, 18),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 30,
         'activity': Activity.objects.get(activity='Hobbies'),
         'date': date(2022, 11, 18),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 120,
         'activity': Activity.objects.get(activity='Working Overtime'),
         'date': date(2022, 11, 17),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 120,
         'activity': Activity.objects.get(activity='Playing Video Games'),
         'date': date(2022, 11, 17),
         'creator': user,
         'url': generate_random_slug()},
        {'time': 45,
         'activity': Activity.objects.get(activity='Hanging out with Friends'),
         'date': date(2022, 11, 17),
         'creator': user,
         'url': generate_random_slug()},

    ]

    for e in ActivityEntries:
        entries = add_activity_entry(e['time'], e['activity'], e['date'], e['creator'], e['url'])

    Entries = [
        {'date': date(2022, 11, 23),
         'creator': user,
         'happiness': 4,
         'anger': -2,
         'disgust': -4,
         'fear': -3,
         'power': 3,
         'peace': 4,
         'url': generate_random_slug()},
        {'date': date(2022, 11, 22),
         'creator': user,
         'happiness': 2,
         'anger': -1,
         'disgust': -2,
         'fear': -2,
         'power': 0,
         'peace': 3,
         'url': generate_random_slug()},
        {'date': date(2022, 11, 21),
         'creator': user,
         'happiness': 0,
         'anger': 0,
         'disgust': 0,
         'fear': -2,
         'power': 1,
         'peace': 2,
         'url': generate_random_slug()},
        {'date': date(2022, 11, 20),
         'creator': user,
         'happiness': -1,
         'anger': 0,
         'disgust': 0,
         'fear': 1,
         'power': -2,
         'peace': 0,
         'url': generate_random_slug()},
        {'date': date(2022, 11, 19),
         'creator': user,
         'happiness': 1,
         'anger': 4,
         'disgust': 3,
         'fear': 0,
         'power': -1,
         'peace': -2,
         'url': generate_random_slug()},
        {'date': date(2022, 11, 18),
         'creator': user,
         'happiness': -3,
         'anger': 2,
         'disgust': 2,
         'fear': 0,
         'power': -1,
         'peace': -2,
         'url': generate_random_slug()},
        {'date': date(2022, 11, 17),
         'creator': user,
         'happiness': -4,
         'anger': 2,
         'disgust': 1,
         'fear': 0,
         'power': -3,
         'peace': -3,
         'url': generate_random_slug()},
    ]

    for e in Entries:
        entries = add_entry(e['date'], e['creator'], e['happiness'], e['anger'],
                            e['disgust'], e['fear'], e['power'], e['peace'], e['url'])

    Articles = [
        {'title': 'How to be Happy',
         'category': 'Mental Health Advice',
         'url': 'https://www.nhs.uk/mental-health/self-help/tips-and-support/how-to-be-happier/'},
        {'title': 'NHS Mental Health Services',
         'category': 'Mental Health Advice',
         'url': 'https://www.nhs.uk/nhs-services/mental-health-services/'},
        {'title': 'University of Glasgow Counseling',
         'category': 'Mental Health Advice',
         'url': 'https://www.gla.ac.uk/myglasgow/counselling/'},
        {'title': 'How to Meditate',
         'category': 'Meditation',
         'url': 'https://www.mindful.org/how-to-meditate/'},
        {'title': 'Daily Mind - 10 Minute Reputation',
         'category': 'Meditation',
         'url': 'https://www.youtube.com/watch?v=ZToicYcHIOU'},
        {'title': 'What type of Meditation is Best for You?',
         'category': 'Meditation',
         'url': 'https://www.healthline.com/health/mental-health/types-of-meditation'},
        {'title': 'Mindfulness - Getting Started',
         'category': 'Mindfulness',
         'url': 'https://www.mindful.org/meditation/mindfulness-getting-started/'},
        {'title': 'NHS Mindfulness',
         'category': 'Mindfulness',
         'url': 'https://www.nhs.uk/mental-health/self-help/tips-and-support/mindfulness/'},
        {'title': 'Harvard News - Mindfulness and Life',
         'category': 'Mindfulness',
         'url': 'https://news.harvard.edu/gazette/story/2018/04/less-stress-clearer-thoughts-with-mindfulness-meditation/'},
        {'title': 'NHS - Sleep and Tiredness',
         'category': 'Sleep',
         'url': 'https://www.nhs.uk/live-well/sleep-and-tiredness/'},
        {'title': 'Sleep Foundation - Healthy Sleep Tips',
         'category': 'Sleep',
         'url': 'https://www.sleepfoundation.org/sleep-hygiene/healthy-sleep-tips'},
        {'title': 'CDC - Tips for Healthy Sleep',
         'category': 'Sleep',
         'url': 'https://www.cdc.gov/sleep/about_sleep/sleep_hygiene.html'},
        {'title': 'What is Stress?',
         'category': 'Stress',
         'url': 'https://www.mind.org.uk/information-support/types-of-mental-health-problems/stress/what-is-stress/#:~:text=Stress%20is%20how%20we%20react,you%20are%20struggling%20to%20manage'},
        {'title': 'NHS - Get Help with Stress',
         'category': 'Stress',
         'url': 'https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/stress/'},
        {'title': 'Stress | Mental Health Foundation',
         'category': 'Stress',
         'url': 'https://www.mentalhealth.org.uk/explore-mental-health/a-z-topics/stress'}
    ]

    for art in Articles:
        article = add_article(art['title'], art['category'], art['url'])


def add_activity_type(type):
    at = ActivityType.objects.create(type=type)
    return at


def add_activity(activity, type):
    act = Activity.objects.create(activity=activity, type=type)
    return act


def add_activity_entry(time, activity, date, creator, url):
    entry = ActivityEntry.objects.create(time=time, activity=activity,
                                         date=date, creator=creator, url=url)
    return entry


def add_entry(date, creator, happiness, anger, disgust, fear, power, peace, url):
    entry = Entry.objects.create(date=date, creator=creator, happiness=happiness, anger=anger,
                                 disgust=disgust, fear=fear, power=power, peace=peace, url=url)
    return entry


def add_article(title, category, url):
    article = Article.objects.create(title=title, category=category, url=url)
    return article

if __name__ == '__main__':
    print("Starting Population")
    populate()
    print("Populated successfully")
