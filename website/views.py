import json
from django.views.generic import TemplateView
from .models import Activity, ActivityKeyword, ActivityLeader, ActivitySponsor, Attendance, Contact, \
    Event, EventPicture, Keyword, Material, Member, Presentation, Home, About, Coc


def get_rep_contact():
    c_dict = dict()
    for c in Contact.objects.all().filter(m__name="캐글뽀개기"):
        c_dict[c.get_contact_type_display().lower()] = c.info
    return c_dict

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
        context['sponsors'] = Member.objects.all().filter(type=3)
        return context


class IndexDatabreak2018(TemplateView):
    template_name = 'website/databreak2018/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexDatabreak2018, self).get_context_data(**kwargs)
        context['rep_contact'] = get_rep_contact()
        #context['schedule'] = json.dumps(Presentation.objects.all().filter(e=6))
        #print(context['schedule'])
        return context
