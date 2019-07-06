from django.contrib import admin
from .models import Volunteer, Interest, Language, Training, Event, Role, OrganizationAffiliation, VolEmgtCtct

admin.site.register(Volunteer)
admin.site.register(Interest)
admin.site.register(Language)
admin.site.register(Event)
admin.site.register(OrganizationAffiliation)
admin.site.register(Role)
admin.site.register(VolEmgtCtct)
