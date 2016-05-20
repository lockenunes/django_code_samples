from django.contrib import admin
from .models import *
# Register your models here.


class MembershipInlineAdmin(admin.TabularInline):
    model = Membership

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        if obj:
            return obj.membership_set.count() - 1
        return extra


class PersonAdmin(admin.ModelAdmin):
    inlines = [ MembershipInlineAdmin ]


admin.site.register(Person, PersonAdmin)
admin.site.register(Group)
admin.site.register(Membership)