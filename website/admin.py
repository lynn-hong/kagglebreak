from django.contrib import admin
from .models import Activity, ActivityKeyword, ActivityLeader, ActivitySponsor, Attendance, Contact, \
    Event, EventPicture, Keyword, Material, Member, Presentation, Home, About, Coc


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['act_type', 'title', 'goal', 'summary', 'level', 'textbook', 'curriculum']

@admin.register(ActivityKeyword)
class ActivityKeywordAdmin(admin.ModelAdmin):
    pass

@admin.register(ActivityLeader)
class ActivityLeaderAdmin(admin.ModelAdmin):
    list_display = ['a', 'm']

@admin.register(ActivitySponsor)
class ActivitySponsorAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['m', 'contact_type', 'info']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['a', 's_datetime', 'e_datetime', 'location']

@admin.register(EventPicture)
class EventPictureAdmin(admin.ModelAdmin):
    pass

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ['keyword']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['category', 'type', 'name', 'nickname_eng',
                    'affiliation', 'interest', 'introduction', 'picture']

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ['e', 'm', 'title', 'summary', 'specific_location', 's_time', 'e_time']

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['top', 'middle', 'bottom', 'button_title', 'button_url']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['sub_title', 'title', 'content', 'image_file']

@admin.register(Coc)
class CocAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'direction', 'icon']

