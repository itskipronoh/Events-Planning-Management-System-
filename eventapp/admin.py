from django.contrib import admin
from .models import Event,Booking,Contact,Feedback
# Register your models here.
admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Feedback)