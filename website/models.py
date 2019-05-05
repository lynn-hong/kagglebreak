# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django import utils
from django.db import models

DAYS_OF_WEEK = (
    (0, '월'),
    (1, '화'),
    (2, '수'),
    (3, '목'),
    (4, '금'),
    (5, '토'),
    (6, '일'),
)

DATE_INTERVAL = (
    (0, '주간'),
    (1, '격주간'),
    (2, '월간'),
    (3, '1회성'),
    (4, '일간'),
    (5, '비정기'),
    (6, '연간'),
)

LEVEL = (
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
)

ACTIVITY_TYPE = (
    ('study', 'Study'),
    ('workshop', 'Workshop'),
    ('staff', 'Staff meeting'),
    ('open', 'Open meeting'),
    ('mentoring', 'Mentoring'),
    ('external event', 'External event'),
)

CONTACT_TYPE = (
    (0, 'Facebook'),
    (1, 'Email'),
    (2, 'Phone'),
    (3, 'Linkedin'),
    (4, 'Instagram'),
    (5, 'Twitter'),
    (6, 'Youtube'),
    (7, 'Github'),
    (8, 'Website'),
    (9, 'Address'),
    (10, 'Slack')
)

DIRECTION = (
    (0, 'left'),
    (1, 'right'),
)

MEMBER_CATEGORY = (
    (0, 'person'),
    (1, 'organization'),
)

MEMBER_TYPE = (
    (0, 'Admin'),
    (1, 'Magager'),
    (2, 'General'),
    (3, 'Sponsor'),
    (4, 'Supporter'),
)

STAFF_TYPE = (
    (0, 'None'),
    (1, 'top'),
    (2, 'Creator'),
    (3, 'Operator'),
    (4, 'Organizer'),
)

SPON_LEVEL = (
    (0, 'Diamond'),
    (1, 'Gold'),
    (2, 'Silver'),
    (3, 'Bronze'),
    (4, 'Heart'),
    (5, 'Personal'),
)

URL_TYPE = (
    (0, 'register'),
    (1, 'apply_speech'),
    (2, 'review'),
    (3, 'picture'),
)

class Home(models.Model):
    order = models.IntegerField(default=None)
    top = models.CharField(max_length=255, blank=True, null=True)
    middle = models.CharField(max_length=255, blank=True, null=True)
    bottom = models.CharField(max_length=255, blank=True, null=True)
    button_title = models.CharField(max_length=255, blank=True, null=True)
    button_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HOME'


class About(models.Model):
    sub_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255, blank=True, null=True)
    image_file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ABOUT'


class Coc(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255, blank=True, null=True)
    direction = models.IntegerField(choices=DIRECTION, default=None)
    icon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'COC'


class Activity(models.Model):
    act_type = models.CharField(max_length=45, choices=ACTIVITY_TYPE, default=0)
    day = models.IntegerField(choices=DAYS_OF_WEEK, blank=True, null=True)
    interval = models.IntegerField(choices=DATE_INTERVAL, default=0)
    title = models.CharField(unique=True, max_length=45)
    goal = models.CharField(max_length=255, blank=True, null=True)
    num_of_people = models.CharField(max_length=45, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    level = models.IntegerField(choices=LEVEL, blank=True, null=True)
    textbook = models.TextField(blank=True, null=True)
    curriculum = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ACTIVITY'

    def __str__(self):
        return self.title


class ActivityKeyword(models.Model):
    a = models.ForeignKey('Activity', on_delete=models.PROTECT)
    k = models.ForeignKey('Keyword', on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'ACTIVITY_KEYWORD'

    def __str__(self):
        return self.k


class ActivityLeader(models.Model):
    a = models.ForeignKey('Activity', on_delete=models.PROTECT)
    m = models.ForeignKey('Member', on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'ACTIVITY_LEADER'


class ActivitySponsor(models.Model):
    a = models.ForeignKey('Activity', on_delete=models.PROTECT)
    s = models.ForeignKey('Member', on_delete=models.PROTECT)
    spon_type = models.CharField(max_length=45, blank=True, null=True)
    spon_level = models.IntegerField(choices=SPON_LEVEL, default=0)
    order_number = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'ACTIVITY_SPONSOR'


class Attendance(models.Model):
    m = models.ForeignKey('Member', on_delete=models.PROTECT)
    e = models.ForeignKey('Event', on_delete=models.PROTECT)
    real_attendance = models.IntegerField(blank=True, null=True)
    lateness = models.IntegerField(blank=True, null=True)
    early_leave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ATTENDANCE'


class Competition(models.Model):
    title = models.CharField(unique=True, max_length=255)
    url = models.CharField(unique=True, max_length=255)
    github_url = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'COMPETITION'


class Contact(models.Model):
    m = models.ForeignKey('Member', on_delete=models.PROTECT)
    contact_type = models.IntegerField(choices=CONTACT_TYPE, default=0)
    info = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'CONTACT'


class Event(models.Model):
    a = models.ForeignKey(Activity, on_delete=models.PROTECT)
    s_datetime = models.DateTimeField()
    e_datetime = models.DateTimeField()
    location = models.CharField(max_length=255)
    e_title_kor = models.CharField(max_length=255, default="")
    e_title_eng = models.CharField(max_length=255, blank=True, null=True)
    e_desc_kor = models.TextField(blank=True, null=True)
    e_desc_eng = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    location_map = models.TextField(blank=True, null=True)
    welcome_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'EVENT'

    def __str__(self):
        return self.e_title_kor


class EventKeyword(models.Model):
    event = models.ForeignKey('Event', on_delete=models.PROTECT)
    is_main = models.NullBooleanField(default=False)
    k = models.ForeignKey('Keyword', on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'EVENT_KEYWORD'

    def __str__(self):
        return '{} - {}'.format(self.event, self.k)


class EventPicture(models.Model):
    e = models.ForeignKey(Event, on_delete=models.PROTECT)
    pic_link = models.TextField(default=None)

    class Meta:
        managed = True
        db_table = 'EVENT_PICTURE'


class EventSponsor(models.Model):
    e = models.ForeignKey(Event, on_delete=models.PROTECT)
    s = models.ForeignKey('Member', on_delete=models.PROTECT)
    spon_type = models.CharField(max_length=45, blank=True, null=True)
    spon_level = models.IntegerField(choices=SPON_LEVEL, default=0)
    order_number = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'EVENT_SPONSOR'

    def __str__(self):
        return "{} - {}".format(self.e.a, self.e)


class EventUrl(models.Model):
    e = models.ForeignKey(Event, on_delete=models.PROTECT)
    url_type = models.IntegerField(choices=URL_TYPE, default=0)
    url_desc = models.CharField(max_length=60, default=None)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'EVENT_URL'

    def __str__(self):
        return "{} - {}".format(self.url_type, self.url)


class Keyword(models.Model):
    keyword = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = True
        db_table = 'KEYWORD'

    def __str__(self):
        return self.keyword


class Material(models.Model):
    p = models.ForeignKey('Presentation', on_delete=models.PROTECT)
    material_link = models.TextField(default=None)

    class Meta:
        managed = True
        db_table = 'MATERIAL'

    def __str__(self):
        return "{} 발표자료".format(self.p)


class Member(models.Model):
    category = models.IntegerField(choices=MEMBER_CATEGORY, default=None)
    type = models.IntegerField(choices=MEMBER_TYPE, default=1)
    staff_type = models.IntegerField(choices=STAFF_TYPE, default=None)
    is_staff_leader = models.NullBooleanField(blank=True, null=True)
    name = models.CharField(max_length=45)
    nickname_eng = models.CharField(max_length=45)
    affiliation = models.CharField(max_length=45, blank=True, null=True)
    interest = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    picture = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'MEMBER'

    def __str__(self):
        return self.name


class Presentation(models.Model):
    e = models.ForeignKey(Event, on_delete=models.PROTECT)
    m = models.ForeignKey(Member, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, blank=True, null=True)
    specific_location = models.CharField(max_length=255, blank=True, null=True)
    s_time = models.TimeField()
    e_time = models.TimeField()

    class Meta:
        managed = True
        db_table = 'PRESENTATION'

    def __str__(self):
        return "{}-{}-{}".format(self.e, self.title, self.m)


class ActivityNotification(models.Model):
    a = models.ForeignKey(Activity, on_delete=models.PROTECT)
    notification = models.CharField(max_length=1000)
    upload_time = models.DateTimeField(default=utils.timezone.now)

    class Meta:
        managed = True
        db_table = 'ACTIVITY_NOTIFICATION'

    def __str__(self):
        return self.notification


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete=models.PROTECT)
    permission = models.ForeignKey('AuthPermission', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.PROTECT)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.PROTECT)
    group = models.ForeignKey(AuthGroup, on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.PROTECT)
    permission = models.ForeignKey(AuthPermission, on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True, on_delete=models.PROTECT)
    user = models.ForeignKey(AuthUser, on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
