from django.contrib import admin
from home import models



# Register your models here.
admin.site.register([
    models.Job,
    models.ServiceProvider,
    models.History
])
