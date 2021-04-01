from django.contrib import admin

# Register your models here.

# JAKostikov - gXu9+7+4FLQg@$Y
# AMRomanenkov - V.!x89gQM_tTv8!
# MIVasilev - 6*SSm+8SbbAUCrq

from .models import *

admin.site.register(ProfessorTypes)
admin.site.register(Groups)
admin.site.register(Students)
admin.site.register(Professors)
admin.site.register(Tests)
