from django.forms import TextInput, Textarea, widgets, ModelChoiceField
from django.db import models
from django.contrib import admin
from .models import Activity, ActivityKeyword, ActivityLeader, ActivitySponsor, Attendance, Contact, \
    Event, EventPicture, Keyword, Material, Member, Presentation, Home, About, Coc, ActivityNotification,\
    Competition, EventSponsor, EventUrl, EventKeyword

textinput_width = '100'

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'act_type', 'title', 'interval', 'day', 'num_of_people',
                    'goal', 'summary', 'level', 'textbook', 'curriculum']
    list_display_links = ['title']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(ActivityKeyword)
class ActivityKeywordAdmin(admin.ModelAdmin):
    pass

@admin.register(ActivityLeader)
class ActivityLeaderAdmin(admin.ModelAdmin):
    list_display = ['a', 'm']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(ActivitySponsor)
class ActivitySponsorAdmin(admin.ModelAdmin):
    list_display = ['id', 'a', 's', 'spon_level', 'spon_type', 'order_number']
    list_display_links = ['s']
    ordering = ['spon_level', 'order_number']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(ActivityNotification)
class ActivityNotificationAdmin(admin.ModelAdmin):
    list_display = ['a', 'notification', 'upload_time']
    list_display_links = ['notification']
    ordering = ['-upload_time']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'github_url']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['m', 'contact_type', 'info']
    ordering = ['m__type', 'm__name', 'contact_type']
    list_filter = ['contact_type']
    search_fields = ['m__name', 'info']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'a', 's_datetime', 'e_datetime', 'location', 'e_title_kor', 'e_title_eng',
                    'e_desc_kor', 'e_desc_eng', 'url']
    list_display_links = ['a']
    list_filter = ['a']
    search_fields = ['a', 'location', 'e_title_kor', 'e_desc_kor']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(EventKeyword)
class EventKeywordAdmin(admin.ModelAdmin):
    list_display = ['event', 'is_main', 'k']

@admin.register(EventPicture)
class EventPictureAdmin(admin.ModelAdmin):
    list_display = ['e', 'pic_link']

@admin.register(EventSponsor)
class EventSponsorAdmin(admin.ModelAdmin):
    list_display = ['id', 'e', 's', 'spon_level', 'spon_type', 'order_number']
    list_display_links = ['s']
    ordering = ['spon_level', 'order_number']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(EventUrl)
class EventUrlAdmin(admin.ModelAdmin):
    list_display = ['e', 'url_type', 'url_desc', 'url']

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ['keyword']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['p', 'material_link']
    formfield_overrides = {
        ModelChoiceField: {'widget': widgets.Select(attrs={'size': textinput_width})},
    }

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['category', 'type', 'staff_type', 'is_staff_leader', 'name', 'nickname_eng',
                    'affiliation', 'interest', 'introduction', 'picture']
    list_display_links = ['name']
    list_filter = ['type']
    ordering = ['type', 'name']
    search_fields = ['name', 'affiliation', 'interest', 'interest']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ['e', 'm', 'title', 'summary', 'specific_location', 's_time', 'e_time']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['order', 'top', 'middle', 'bottom', 'button_title', 'button_url']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['sub_title', 'title', 'content', 'image_file']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

@admin.register(Coc)
class CocAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'direction', 'icon']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': textinput_width})},
    }

