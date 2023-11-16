from django.contrib import admin
from distribution.models import Client, Distribution, DistributionLogs, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'email', 'distribution_id', 'owner')
    list_filter = ('distribution_id',)
    search_fields = ('name', 'description',)


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_datetime', 'end_datetime', 'frequency', 'status', 'message_id', 'owner')
    list_filter = ('name', 'status', 'frequency',)
    search_fields = ('name', 'status', 'frequency',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_message', 'body_message')
    list_filter = ('title_message',)
    search_fields = ('title_message',)


@admin.register(DistributionLogs)
class DistributionLogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'distribution_id', 'start_datetime', 'status', 'server_response')
    list_filter = ('distribution_id', 'start_datetime', 'status',)
    search_fields = ('distribution_id',)
