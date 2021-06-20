from django.contrib import admin
from .models import Profile, Plant, GrowingZone, GrowingSchedule, LightNeeded



admin.site.register(Profile)
admin.site.register(Plant)
admin.site.register(GrowingZone)
admin.site.register(GrowingSchedule)
admin.site.register(LightNeeded)



