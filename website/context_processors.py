from .models import ActivitySponsor, Contact


def get_rep_contact():
    c_dict = dict()
    for c in Contact.objects.all().filter(m__name="캐글뽀개기"):
        c_dict[c.get_contact_type_display().lower()] = c.info
    return c_dict

def footer(request):
    sponsors = ActivitySponsor.objects\
        .values("s__picture", "s__name", "spon_level", "spon_type", "s__contact__info")\
        .filter(a__id=1).order_by('spon_level').exclude(spon_level=4)
    supporters = ActivitySponsor.objects\
        .values("s__picture", "s__name", "spon_level", "spon_type", "s__contact__info")\
        .filter(a__id=1).filter(spon_level=4)
    rep_contact = get_rep_contact()
    return {
        'sponsors': sponsors,
        'supporters': supporters,
        'rep_contact': rep_contact,
    }
