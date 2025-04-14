from django.contrib import admin


from .models import Client, TelegramClient


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'email', 'created_at')
    search_fields = ('client__first_name', 'client__last_name', 'email', 'phone_number')


    def has_delete_permission(self, request, obj=None):
        # Disable the ability to delete clients from the admin
        return False


class TelegramClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'tg_id', 'username')

    def has_delete_permission(self, request, obj=None):
        # Disable the ability to delete telegram clients from the admin
        return False


admin.site.register(Client, ClientAdmin)
admin.site.register(TelegramClient, TelegramClientAdmin)
