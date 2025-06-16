from django.contrib import admin

from clients_app.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "name",
        "surname",
        "second_name",
        "comment",
    )
    list_filter = ("email",)
    search_fields = (
        "name",
        "surname",
    )
