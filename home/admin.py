from django.contrib import admin
from home import models



# Register your models here.
admin.site.register([
    models.Job,
    models.ServiceProvider,
    models.History
])

admin.site.site_header  =  "Nice Private Limited Admin"
admin.site.site_title  =  "Nice Private Limited Admin Site"
admin.site.index_title  =  "Nice Private Ltd. Admin"
