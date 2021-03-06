from django.contrib import admin
from models import Lobbyist, LobbyistCorporation
from django.contrib.contenttypes import generic
from links.models import Link


class LinksInline(generic.GenericTabularInline):
    model = Link
    ct_fk_field = 'object_pk'
    extra = 1


class LobbyistAdmin(admin.ModelAdmin):
    fields = ('person', 'description', 'image_url', 'large_image_url',)
    readonly_fields = ('person',)
    inlines = (LinksInline,)


class LobbyistCorporationAdmin(admin.ModelAdmin):
    fields = ('name', 'description',)
    readonly_fields = ('name',)
    inlines = (LinksInline,)


admin.site.register(Lobbyist, LobbyistAdmin)
admin.site.register(LobbyistCorporation, LobbyistCorporationAdmin)

