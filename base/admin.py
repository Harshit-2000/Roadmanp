from django.contrib import admin

from base.models import Link, Subject, Tag, Topic

# Register your models here.

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Link)
admin.site.register(Tag)
