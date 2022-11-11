from django.contrib import admin
from .models import Post, Coach
from guardian.admin import GuardedModelAdmin

class CoachModelAdmin(GuardedModelAdmin):
    pass
    # exclude = ('maintainer',)
    #TODO: check if request.user is superadmin
    # def get_exclude(self, request, obj=None):
    #     if obj is not None and request.user.is_authenticated():  # In Django 1.10+ use request.user.is_authenticated
    #         if obj.creator == request.user:
    #             return ['status']
    #     else:
    #         return []
admin.site.register(Coach, CoachModelAdmin)

class CoachesEditorArea(admin.AdminSite):
    site_header = 'Coaches Editor Area'

coachesEditorArea = CoachesEditorArea(name='Coaches editor')

class CoachModelEditor(admin.ModelAdmin):
    exclude = ('maintainer',)
coachesEditorArea.register(Coach, CoachModelEditor)



