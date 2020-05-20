from django.contrib import admin
from .models import LikeCount,LikeRecord
# Register your models here.

@admin.register(LikeCount)
class LikeCountAdmin(admin.ModelAdmin):
    pass

@admin.register(LikeRecord)
class LikeRecordAdmin(admin.ModelAdmin):
    pass