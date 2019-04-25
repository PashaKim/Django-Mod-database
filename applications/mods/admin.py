from django.contrib import admin
from django.utils.html import format_html

from .models import Mod, Tag, ModFile, ModImage, Language


class ModImageInline(admin.TabularInline):
    model = ModImage
    extra = 1


class ModFileInline(admin.TabularInline):
    model = ModFile
    extra = 1


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    fields = ('name', 'code')
    list_display = ('name', 'code')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'created', 'updated', 'is_visible')
    list_display = ('id', 'name', 'description', 'created', 'updated', 'is_visible')
    list_display_links = ('id', 'name')
    readonly_fields = ('created', 'updated',)
    list_filter = ('is_visible', 'created', 'updated')
    search_fields = ('name',)


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    fields = ('name', 'author', 'url', 'title_image', 'rating', 'tag', 'compatibility_mod', 'incompatibility_mod',
              'description', 'order_index', 'created', 'updated', 'is_visible')
    list_display = ('id', 'name', 'author', 'url_link', 'rating', 'order_index', 'created', 'updated',
                    'is_visible', 'tags_name', 'compatibility', 'incompatibility')
    list_filter = ('rating', 'created', 'updated', 'is_visible', 'tag')
    search_fields = ('name', 'author',)
    readonly_fields = ('created', 'updated',)
    list_display_links = ('id', 'name')
    filter_horizontal = ('tag', 'compatibility_mod', 'incompatibility_mod')
    inlines = (ModFileInline, ModImageInline)

    def url_link(self, obj):
        # return '<a href="%s">%s</a>' % (obj.url, obj.url)
        return format_html(u'<a href="%s">%s</a>' % (obj.url, obj.url))

    url_link.allow_tags = True

@admin.register(ModFile)
class ModFileAdmin(admin.ModelAdmin):
    fields = ('mod', 'file', 'description', 'created', 'updated', 'is_visible')
    list_display = ('id', 'mod', 'file', 'created', 'updated', 'is_visible')
    list_display_links = ('id', 'mod')
    readonly_fields = ('created', 'updated',)
    search_fields = ('mod__name', 'mod__author')
    raw_id_fields = ('mod', )


@admin.register(ModImage)
class ModImageAdmin(admin.ModelAdmin):
    fields = ('mod', 'image', 'description', 'created', 'updated', 'is_visible')
    list_display = ('id', 'mod', 'image', 'created', 'updated', 'is_visible')
    list_display_links = ('id', 'mod')
    readonly_fields = ('created', 'updated',)
    search_fields = ('mod__name', 'mod__author')
    raw_id_fields = ('mod', )
