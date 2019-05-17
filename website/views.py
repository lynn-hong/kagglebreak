from datetime import datetime, time, date
import json
import random
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .models import Activity, ActivityKeyword, ActivityLeader, ActivitySponsor, Attendance, Contact, \
    Event, EventPicture, Keyword, Material, Member, Presentation, Home, About, Coc, ActivityNotification,\
    Competition, EventSponsor, EventUrl, EventKeyword, Operation

# Databreak2018
ROOM = {'A': 1, 'B': 2, 'C': 3, 'Hall': 4}

# Default homepage
STAFF_TYPES = {2: {'name': 'Creator', 'desc': '데이터 관련 유용한 컨텐츠 생산, 번역, 스터디 리딩 활동을 수행합니다',
                   'task':['데이터 (분석/엔지니어링) 스터디 진행', '데이터 관련 블로그 운영 (번역 및 논문 리뷰)',
                           '온라인 Slack 운영', '대학생 멘토링']},
               3: {'name': 'Operator', 'desc': '커뮤니티의 내부 자료, 예산 등을 관리하고 활동 내역을 기록합니다',
                   'task':['정관 및 회원명부 관리', 'CoC 및 스폰서 가이드 관리', '디자인 산출물(로고 등) 관리',
                           '홈페이지 기획 및 운영', '페이스북 운영', '월별 운영모임 준비']},
               4: {'name': 'Organizer', 'desc': '오프라인 밋업&행사 조직 등 외부와의 교류 활동을 수행합니다',
                   'task': ['행사 기획 (Ex. BootCamp, Meetup, Conference)', '오프라인 행사 진행',
                            '후원사&발표자 컨택', '행사 동영상 편집', '예산 관리']}
               }

def get_rep_contact():
    c_dict = dict()
    for c in Contact.objects.all().filter(m__name="데이터뽀개기"):
        c_dict[c.get_contact_type_display().lower()] = c.info
    return c_dict

def get_speaker():
    speakers = Presentation.objects.filter(e=6).exclude(m__type=0).order_by('s_time')\
        .values('id', 'm__picture', 'm__name', 'm__affiliation', 'm__interest', 'm__id',
                'title', 'summary', 's_time', 'e_time', 'specific_location')
    for sp in speakers:
        sp['material'] = Material.objects.all().filter(p=sp['id'])
        c_list = list()
        for c in Contact.objects.all().filter(m__id=sp['m__id']):
            contact_type = c.get_contact_type_display().lower()
            val = {'contact_type': contact_type, 'url': c.info}
            c_list.append(val)
        sp['contacts'] = c_list
    return speakers

def get_keynote():
    speakers = Presentation.objects.filter(e=6).exclude(m__type=0).order_by('s_time')\
        .values('id', 'm__picture', 'm__name', 'm__affiliation', 'm__interest', 'm__id',
                'title', 'summary', 's_time', 'e_time', 'specific_location', 'm__introduction')
    return_val = list()
    for sp in speakers:
        if not sp['title'].startswith('[keynote]'):
            continue
        c_list = list()
        for c in Contact.objects.all().filter(m__id=sp['m__id']):
            contact_type = c.get_contact_type_display().lower()
            val = {'contact_type': contact_type, 'url': c.info}
            c_list.append(val)
        sp['contacts'] = c_list
        return_val.append(sp)
    return return_val

def get_schedule():
    pts = Presentation.objects.all().filter(e=6)
    pts_list = list()
    for pt in pts:
        pt_dict = dict()
        pt_dict['roomId'] = ROOM[pt.specific_location.strip('+')]
        pt_dict['text'] = pt.title
        pt_dict['speaker'] = "" if pt.m.name == "데이터뽀개기" else pt.m.name
        pt_dict['managing'] = True if pt.m.name == "데이터뽀개기" else False
        pt_dict['startDate'] = datetime.combine(date(2018, 10, 7), pt.s_time).strftime("%Y-%m-%d %H:%M:%S")
        pt_dict['endDate'] = datetime.combine(date(2018, 10, 7), pt.e_time).strftime("%Y-%m-%d %H:%M:%S")
        pt_dict['isFull'] = True if pt.specific_location.endswith('+') else False
        pt_dict['summary'] = pt.summary
        pt_dict['pic'] = pt.m.picture
        pt_dict['id'] = pt.id
        pts_list.append(pt_dict)
    return json.dumps(pts_list, cls=DjangoJSONEncoder)

def get_default_sponsor():
    sponsors = Member.objects.all().filter(type=3).filter(affiliation="상시").values()
    for s in sponsors:
        for c in Contact.objects.all().filter(m__id=s['id']):
            if c.get_contact_type_display().lower() == 'website':
                s['website'] = c.info
    return sponsors

def get_coc():
    coc_left = list()
    coc_right = list()
    for coc in Coc.objects.all():
        if coc.direction == 0:  # LEFT
            coc_left.append(coc)
        else:   # RIGHT
            coc_right.append(coc)
    return coc_left, coc_right

def get_manager():
    managers = Member.objects.all().filter(type=1).values()
    for m in managers:
        c_list = list()
        for c in Contact.objects.all().filter(m__id=m['id']):
            contact_type = c.get_contact_type_display().lower()
            val = {'contact_type': contact_type, 'url': c.info}
            c_list.append(val)
        m['contacts'] = c_list
        m['staff_type'] = STAFF_TYPES[m['staff_type']]['name']  # title of team
    return managers

def get_page_info(name):
    return Operation.objects.filter(type_name=0).filter(key=name).values('value', 'value2')[0]


class Index(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context['homes'] = Home.objects.all().order_by('order')
        context['about'] = About.objects.first()
        context['rep_contact'] = get_rep_contact()
        context['sponsors'] = get_default_sponsor()
        context['page_info'] = get_page_info('index')
        return context

class IndexAbout(TemplateView):
    template_name = 'website/about_detail.html'

    def get_context_data(self, **kwargs):
        context = super(IndexAbout, self).get_context_data(**kwargs)
        context['coc_lefts'], context['coc_rights'] = get_coc()
        context['sponsors'] = get_default_sponsor()
        context['rep_contact'] = get_rep_contact()
        context['page_info'] = get_page_info('about')
        return context

class IndexPeople(TemplateView):
    template_name = 'website/people_detail.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPeople, self).get_context_data(**kwargs)
        context['manager_types'] = [x for x in STAFF_TYPES.values()]
        context['managers'] = get_manager()
        context['sponsors'] = get_default_sponsor()
        context['rep_contact'] = get_rep_contact()
        context['page_info'] = get_page_info('people')
        return context

class IndexActivity(TemplateView):
    template_name = 'website/activity_detail.html'

    def get_event(self):
        event_arr = []
        all_events = Event.objects.all()
        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = "[{}] {}: {}".format(i.a.act_type, i.a.title, i.e_title_kor)
            event_sub_arr['desc'] = i.e_desc_kor.replace("\n", "<br />")
            event_sub_arr['level'] = i.a.get_level_display()
            start_date = datetime.strftime(i.s_datetime, "%Y-%m-%d %H:%M:%S")
            end_date = datetime.strftime(i.e_datetime, "%Y-%m-%d %H:%M:%S")
            event_sub_arr['location'] = i.location
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_sub_arr['leaders'] = ActivityLeader.objects.all().filter(a=i.id)
            event_sub_arr['url'] = i.url
            event_arr.append(event_sub_arr)
        return event_arr

    def get_activities(self):
        activity_types = {'Meeting': [], 'Study & Blog': [], 'Meetup & Workshop': []}
        activities = Activity.objects.all()
        for a in activities:
            a.leaders = list()
            for l in ActivityLeader.objects.all().filter(a=a.id):
                fb = Contact.objects.values('info').filter(m__id=l.m.id).filter(contact_type=0) # facebook
                if len(fb) <= 0:
                    fb = '#'
                else:
                    fb = fb[0]['info']
                a.leaders.append({'name': "{}님".format(l.m.name), 'facebook': fb})
            from_date = Event.objects.values('s_datetime').filter(a__id=a.id).order_by('s_datetime')
            if len(from_date) <= 0:
                a.start_date = '예정'
            else:
                a.start_date = datetime.strftime(from_date[0]['s_datetime'], "%m/%d/%y") + '~'
            if 'meeting' in a.get_act_type_display():
                activity_types['Meeting'].append(a)
            elif a.get_act_type_display() in ['Workshop', 'External event']:
                activity_types['Meetup & Workshop'].append(a)
            else:
                activity_types['Study & Blog'].append(a)
        return activity_types

    def get_context_data(self, **kwargs):
        context = super(IndexActivity, self).get_context_data(**kwargs)
        context['competitions'] = Competition.objects.all()
        context['sponsors'] = get_default_sponsor()
        context['rep_contact'] = get_rep_contact()
        context['events'] = self.get_event()
        context['activity_types'] = self.get_activities()
        context['page_info'] = get_page_info('activity')
        return context

class IndexArchive(TemplateView):
    template_name = 'website/archive_detail.html'

    def get_context_data(self, **kwargs):
        context = super(IndexArchive, self).get_context_data(**kwargs)
        context['competitions'] = Competition.objects.all()
        context['sponsors'] = get_default_sponsor()
        context['rep_contact'] = get_rep_contact()
        context['page_info'] = get_page_info('archive')
        return context

class IndexSponsor(TemplateView):
    template_name = 'website/sponsor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(IndexSponsor, self).get_context_data(**kwargs)
        context['competitions'] = Competition.objects.all()
        context['sponsors'] = get_default_sponsor()
        context['rep_contact'] = get_rep_contact()
        context['page_info'] = get_page_info('sponsor')
        return context

class IndexMeetup(TemplateView):
    template_name = 'website/meetup_detail.html'

    def get_context_data(self, **kwargs):
        context = super(IndexMeetup, self).get_context_data(**kwargs)
        context['meetups'] = Event.objects.all().filter(a_id=10).order_by('-s_datetime')  # filtering meetup
        for meetup in context['meetups']:
            meetup.keyword = EventKeyword.objects.all().filter(event_id=meetup.id).filter(is_main=True)[0]
        context['apply_speech'] = EventUrl.objects.all().filter(e__a_id=10).filter(url_type=1).order_by('-e__s_datetime')[0]
        context['sponsors'] = get_default_sponsor()
        context['rep_contact'] = get_rep_contact()
        context['page_info'] = get_page_info('meetup')
        return context

def each_activity(request, a_id):
    context = dict()
    activity = get_object_or_404(Activity, pk=a_id)
    activity.leaders = []
    for l in ActivityLeader.objects.all().filter(a=activity.id):
        #activity.leaders = ["{}님".format(l.m.name) for l in
        #                    ActivityLeader.objects.all().filter(a=activity.id)]
        fb = Contact.objects.values('info').filter(m__id=l.m.id).filter(contact_type=0) # facebook
        activity.leaders.append({"name": "{}님".format(l.m.name), "fb": fb[0]['info']})
    context['activity'] = activity
    context['rep_contact'] = get_rep_contact()
    context['sponsors'] = get_default_sponsor()
    context['events'] = Event.objects.all().filter(a_id=a_id)
    context['page_info'] = get_page_info('activity_each')
    return render(request, 'website/activity_each.html', context)

def each_meetup(request, e_id):
    context = dict()
    event = get_object_or_404(Event, pk=e_id, a=10)
    # default information
    event.pts = []
    for p in Presentation.objects.all().filter(e_id=e_id).order_by('s_time'):
        material = Material.objects.all().filter(p=p.id).filter(material_type=0)
        video = Material.objects.all().filter(p=p.id).filter(material_type=1)
        if len(material) < 1:
            material = False
        else:
            material = material[0]
        event.pts.append({'pt': p, 'material': material, 'video': video})
    # event picture
    context['pic'] = EventPicture.objects.all().filter(e_id=e_id)
    if len(context['pic']) < 1:
        context['pic'] = False
    else:
        context['pic'] = context['pic'][0]
    # urls
    context['urls'] = EventUrl.objects.all().filter(e_id=e_id).filter(url_type=0)
    # date and time
    if event.s_datetime > datetime(9999,1,1):
        event.s_datetime = '날짜 미정'
    # description
    event.e_desc_kor = [x.split("\r\n") for x in event.e_desc_kor.split("\r\n\r\n")]
    # keywords
    context['keywords'] = EventKeyword.objects.all().filter(event=e_id).order_by('?')
    # event sponsor
    context['event_sponsors'] = EventSponsor.objects.all().filter(e=e_id).order_by('order_number')
    for es in context['event_sponsors']:
        url = Contact.objects.values('info').filter(m__id=es.s.id).filter(contact_type=8)[0]  # website
        es.url = url
    context['event'] = event
    context['rep_contact'] = get_rep_contact()
    context['sponsors'] = get_default_sponsor()
    context['page_info'] = get_page_info('meetup_each')
    if not context['pic'] is False:
        context['page_info']['value2'] = context['pic'].pic_link
    return render(request, 'website/meetup_each.html', context)




# this is for databreak2018 event
class IndexDatabreak2018(TemplateView):
    template_name = 'website/databreak2018/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexDatabreak2018, self).get_context_data(**kwargs)
        context['rep_contact'] = get_rep_contact()
        context['sponsors'] = ActivitySponsor.objects\
            .values("s__picture", "s__name", "spon_level", "spon_type", "s__contact__info")\
            .filter(a__id=1).order_by('spon_level').exclude(spon_level=4)
        context['supporters'] = ActivitySponsor.objects\
            .values("s__picture", "s__name", "spon_level", "spon_type", "s__contact__info")\
            .filter(a__id=1).filter(spon_level=4)
        context['speakers'] = sorted(get_speaker(), key=lambda x: random.random())
        context['schedule'] = get_schedule()
        context['pts'] = get_keynote()
        return context


class IndexCoC(TemplateView):
    template_name = 'website/databreak2018/coc.html'

    def get_context_data(self, **kwargs):
        context = super(IndexCoC, self).get_context_data(**kwargs)
        return context


class IndexSponsorship(TemplateView):
    template_name = 'website/databreak2018/sponsorship.html'

    def get_context_data(self, **kwargs):
        context = super(IndexSponsorship, self).get_context_data(**kwargs)
        return context


class IndexSpeakers(TemplateView):
    template_name = 'website/databreak2018/speakers.html'

    def get_context_data(self, **kwargs):
        context = super(IndexSpeakers, self).get_context_data(**kwargs)
        context['pts'] = get_speaker()
        return context


class IndexNotifications(TemplateView):
    template_name = 'website/databreak2018/notification.html'

    def get_context_data(self, **kwargs):
        context = super(IndexNotifications, self).get_context_data(**kwargs)
        context['notifications'] = ActivityNotification.objects\
            .filter(a__id=1).order_by('-upload_time')
        return context


class IndexSponTicket(TemplateView):
    template_name = 'website/databreak2018/spon_ticket.html'

    def get_context_data(self, **kwargs):
        context = super(IndexSponTicket, self).get_context_data(**kwargs)
        context['personal_sponsors'] = ActivitySponsor.objects \
            .values("s__picture", "s__name", "spon_level", "spon_type", "s__contact__info",
                    's__introduction') \
            .filter(a__id=1).filter(spon_level=5)
        return context


def get_specific_speaker(s_id):
    c_list = list()
    for c in Contact.objects.all().filter(m__id=s_id):
        contact_type = c.get_contact_type_display().lower()
        val = {'contact_type': contact_type, 'url': c.info}
        c_list.append(val)
    return c_list

def speech(request, pk):
    context = dict()
    pt = get_object_or_404(Presentation, pk=pk)
    context['pt'] = pt
    context['contacts'] = get_specific_speaker(pt.m.id)
    return render(request, 'website/databreak2018/speech.html', context,
                  context_instance=RequestContext(request))

def gallery(request):
    return render(request, 'website/databreak2018/gallery.html')

def not_found(request):
    return render(request, 'website/databreak2018/404.html')
