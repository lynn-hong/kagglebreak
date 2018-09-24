from datetime import datetime, time, date
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, RequestContext
from .models import Activity, ActivityKeyword, ActivityLeader, ActivitySponsor, Attendance, Contact, \
    Event, EventPicture, Keyword, Material, Member, Presentation, Home, About, Coc


ROOM = {'A': 1, 'B': 2, 'C': 3, 'Hall': 4}

def get_rep_contact():
    c_dict = dict()
    for c in Contact.objects.all().filter(m__name="캐글뽀개기"):
        c_dict[c.get_contact_type_display().lower()] = c.info
    return c_dict

def get_speaker():
    speakers = Presentation.objects.filter(e=6).exclude(m__type=0).order_by('?')\
        .values('id', 'm__picture', 'm__name', 'm__affiliation', 'm__interest', 'm__id',
                'title', 'summary')
    for sp in speakers:
        c_list = list()
        for c in Contact.objects.all().filter(m__id=sp['m__id']):
            contact_type = c.get_contact_type_display().lower()
            val = {'contact_type': contact_type, 'url': c.info}
            c_list.append(val)
        sp['contacts'] = c_list
    return speakers

def get_schedule():
    pts = Presentation.objects.all().filter(e=6)
    pts_list = list()
    for pt in pts:
        pt_dict = dict()
        pt_dict['roomId'] = ROOM[pt.specific_location.strip('+')]
        pt_dict['text'] = pt.title
        pt_dict['speaker'] = "" if pt.m.name == "캐글뽀개기" else pt.m.name
        pt_dict['managing'] = True if pt.m.name == "캐글뽀개기" else False
        pt_dict['startDate'] = datetime.combine(date(2018, 10, 7), pt.s_time).strftime("%Y-%m-%d %H:%M:%S")
        pt_dict['endDate'] = datetime.combine(date(2018, 10, 7), pt.e_time).strftime("%Y-%m-%d %H:%M:%S")
        pt_dict['isFull'] = True if pt.specific_location.endswith('+') else False
        pt_dict['summary'] = pt.summary
        pt_dict['pic'] = pt.m.picture
        pt_dict['id'] = pt.id
        pts_list.append(pt_dict)
    return json.dumps(pts_list, cls=DjangoJSONEncoder)


class Index(TemplateView):
    template_name = 'website/index-studio.html'

    def get_coc(self):
        coc_left = list()
        coc_right = list()
        for coc in Coc.objects.all():
            if coc.direction == 0:  # LEFT
                coc_left.append(coc)
            else:   # RIGHT
                coc_right.append(coc)
        return coc_left, coc_right

    def get_manager(self):
        managers = Member.objects.all().filter(type=1).values()
        for m in managers:
            c_list = list()
            for c in Contact.objects.all().filter(m__id=m['id']):
                contact_type = c.get_contact_type_display().lower()
                val = {'contact_type': contact_type, 'url': c.info}
                c_list.append(val)
            m['contacts'] = c_list
        return managers

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context['homes'] = Home.objects.all()
        context['about'] = About.objects.first()
        context['coc_lefts'], context['coc_rights'] = self.get_coc()
        context['managers'] = self.get_manager()
        context['rep_contact'] = get_rep_contact()
        context['sponsors'] = Member.objects.all().filter(type=3).filter(affiliation="상시")
        return context


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
        context['speakers'] = get_speaker()
        context['schedule'] = get_schedule()
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
