from django.contrib import admin
from .models import Movie,Myrating,MovieBulkUpload

admin.site.register(Movie)
admin.site.register(Myrating)
admin.site.register(MovieBulkUpload)
# Register your models here.
