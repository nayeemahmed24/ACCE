from django.contrib import admin
from HomeApp.models import Notice, Carousel, Gallery
from django import forms
from django.utils.html import format_html
# Register your models here.


class StateNoticeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'cols': 50}), required=True)


class StateNotice(admin.ModelAdmin):
    form = StateNoticeForm
    sortable_by = ('created_at',)
    search_fields = ('title',)
    list_display = ('title', 'created_at')


admin.site.register(Notice, StateNotice)


class StateCarousel(admin.ModelAdmin):
    list_display = ('title', 'carousel_pic', 'image_tag', 'created_at')
    image_tag = 'Image'

    def image_tag(self, obj):
        if obj.carousel_pic:
            return format_html('<img style="width:40px;height:40px" src="{}" />'.format(obj.carousel_pic.url))


admin.site.register(Carousel, StateCarousel)


class StateGallery(admin.ModelAdmin):
    image_tag = 'Image'
    list_display = ('image_name', 'image_field', 'image_tag', 'event', 'created_at')
    search_fields = ('image_field',)

    def image_tag(self, obj):
        if obj.image_field:
            return format_html('<img style="width:40px;height:40px" src="{}" />'.format(obj.image_field.url))


admin.site.register(Gallery, StateGallery)


