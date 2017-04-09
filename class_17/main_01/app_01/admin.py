from django.contrib import admin

# Register your models here.
from models import *

admin.site.register(MyUser)
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Answers)