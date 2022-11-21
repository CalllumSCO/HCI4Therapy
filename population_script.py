import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "djangoProject.settings")

import django

django.setup()
from mental_health_diary.models import ActivityType, Activity, ActivityEntry, Entry, Article
from datetime import date


def populate(silent=False):
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


def add_activity_type(type):
    at = ActivityType.objects.create(type=type)
    return at

def add_activity(activity, type):
    act = Activity.objects.create(activity=activity, type=type)
    return act

if __name__ == '__main__':
    print("Starting Population")
    populate()
    print("Populated successfully")

