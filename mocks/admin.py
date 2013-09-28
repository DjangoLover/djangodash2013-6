from django.contrib import admin

from models import Blueprint, Resource, Action, Request


class RequestResponseInline(admin.StackedInline):
    model = Action


class ResourceAdmin(admin.ModelAdmin):
    inlines = [RequestResponseInline]
    list_display = ('name', 'blueprint', 'actions_count')


class ResourceInline(admin.TabularInline):
    model = Resource


class BlueprintAdmin(admin.ModelAdmin):
    inlines = [ResourceInline]
    list_display = ('name', 'description')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_method', 'request_path', 'response_status_code', 'requested')


admin.site.register(Blueprint, BlueprintAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Action)
admin.site.register(Request, RequestAdmin)
