from .models import ActivitySponsor, Contact


def get_rep_contact():
    c_dict = dict()
    for c in Contact.objects.all().filter(m__name="캐글뽀개기"):
        c_dict[c.get_contact_type_display().lower()] = c.info
    return c_dict

def footer(request):
    dia_sponsors = ActivitySponsor.objects\
        .values("s__picture", "s__name", "spon_level", "spon_type", "s__contact__info")\
        .filter(a__id=1).order_by('order_number').filter(spon_level=0)
    gold_sponsors = ActivitySponsor.objects\
        .values("s__picture", "s__name", "spon_level", "spon_type", "s__contact__info")\
        .filter(a__id=1).order_by('order_number').filter(spon_level=1)
    silver_sponsors = ActivitySponsor.objects\
        .values("s__picture", "s__name", "spon_level", "spon_type", "s__contact__info")\
        .filter(a__id=1).order_by('order_number').filter(spon_level=2)
    supporters = ActivitySponsor.objects\
        .values("s__picture", "s__name", "spon_level", "spon_type", "s__contact__info")\
        .filter(a__id=1).filter(spon_level=4)
    rep_contact = get_rep_contact()
    return {
        'dia_sponsors': dia_sponsors,
        'gold_sponsors': gold_sponsors,
        'silver_sponsors': silver_sponsors,
        'supporters': supporters,
        'rep_contact': rep_contact,
    }
