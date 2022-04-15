
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()

    d={'ts':topics}
    return render(request,'display_topic.html',d)



def display_webpage(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(topic_name='Foot Ball')
    #webpages=Webpage.objects.exclude(topic_name='Foot Ball')
    #webpages=Webpage.objects.all()[0:2:]
    #webpages=Webpage.objects.all()[-3]
    webpages=Webpage.objects.all().order_by('name')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())
    d={'ws':webpages}
    return render(request,'display_webpage.html',d)

def display_access(request):
    access=AccessRecords.objects.all()
    d={'ac':access}
    return render(request,'display_access.html',d)
