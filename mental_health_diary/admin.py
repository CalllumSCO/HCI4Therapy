from django.contrib import admin
from .models import Entry, Article, Activity, ActivityType, ActivityEntry

# Register your models here.
admin.site.register(Entry)
admin.site.register(Article)
admin.site.register(Activity)
admin.site.register(ActivityType)
admin.site.register(ActivityEntry)
