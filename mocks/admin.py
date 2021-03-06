from django.contrib import admin

from models import Blueprint, Action, Request


class ActionInline(admin.StackedInline):
    model = Action


class BlueprintAdmin(admin.ModelAdmin):
    inlines = [ActionInline]
    list_display = ('name', 'description', 'actions_count')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_method', 'request_path', 'response_status_code', 'requested')
    readonly_fields = ('request_method', 'request_path', 'request_accept', 'request_body',
                       'response_status_code', 'response_content', 'response_content_type', 'requested')

admin.site.register(Blueprint, BlueprintAdmin)
admin.site.register(Request, RequestAdmin)
