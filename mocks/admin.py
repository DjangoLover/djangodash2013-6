from django.contrib import admin

from models import Blueprint, Action, Request


class ActionAdmin(admin.ModelAdmin):
    list_display = ('request_method', 'request_path', 'response_status_code', 'blueprint')


class ActionInline(admin.StackedInline):
    model = Action


class BlueprintAdmin(admin.ModelAdmin):
    inlines = [ActionInline]
    list_display = ('name', 'description', 'actions_count')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_method', 'request_path', 'response_status_code', 'requested')


admin.site.register(Blueprint, BlueprintAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Request, RequestAdmin)
