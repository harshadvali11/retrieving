
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()

    d={'ts':topics}
    return render(request,'display_topic.html',d)



def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='Foot Ball')
    #webpages=Webpage.objects.exclude(topic_name='Foot Ball')
    #webpages=Webpage.objects.all()[0:2:]
    #webpages=Webpage.objects.all()[-3]
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.all().order_by('-name')
    #webpages=Webpage.objects.all().order_by(Length('name'))
    #webpages=Webpage.objects.all().order_by(Length('name').desc())
    #webpages=Webpage.objects.filter(name__startswith='Jes')
    #webpages=Webpage.objects.filter(name__endswith='l')
    #webpages=Webpage.objects.filter(name__contains='t')
    #webpages=Webpage.objects.filter(name__in=('Stacy','Tony'))
    #webpages=Webpage.objects.filter(name__regex=r'^[a-zA-Z]{2}r')
    #webpages=Webpage.objects.filter(Q(topic_name='Foot Ball') & Q(name='Carol'))
    webpages=Webpage.objects.filter(Q(topic_name='Foot Ball') & Q(url__startswith='https') & Q(name__endswith='n'))
    d={'ws':webpages}
    return render(request,'display_webpage.html',d)

def display_access(request):
    access=AccessRecords.objects.all()
    #access=AccessRecords.objects.filter(date='1990-03-30')
    #access=AccessRecords.objects.filter(date__gte='1990-03-30')
    #access=AccessRecords.objects.filter(date__lt='1990-03-30')
    #access=AccessRecords.objects.filter(date__year='2000')
    #access=AccessRecords.objects.filter(date__year__gt='2000')
    access=AccessRecords.objects.filter(date__month='11')
    access=AccessRecords.objects.filter(date__day='9')
    d={'ac':access}
    return render(request,'display_access.html',d)
