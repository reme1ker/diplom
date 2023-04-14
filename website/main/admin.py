from django.contrib import admin

from .models import Games


class GamesModelAdmin(admin.ModelAdmin):
    list_display = ["nazvanie", "data", "developer", "description", "os",
                    "processor", "ram", "video_card", "free_memory"]
    list_editable = []

    class Meta:
        model = Games


admin.site.register(Games, GamesModelAdmin)
