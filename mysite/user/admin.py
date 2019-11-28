from django.contrib import admin
from .models import UserDetail,UserPersonal,ExtraInfo

admin.site.register(UserPersonal)
admin.site.register(UserDetail)
admin.site.register(ExtraInfo)

