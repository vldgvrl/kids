from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Item
from .forms import GetTime

# Create your views here.
def index(request):
    form = GetTime()
    return render (request, 'activity/index.html', {'form': form})

"""
def get_alternatives(request, start_time):
    show_all = Item.objects.all()
    items = []
    count = 0
    start_at = start_time
    plus_half_hour = start_time + 30
    for item in show_all
       if count < 4
           if item.duaration < end_time - start_time
            items.add(item)
            count++
"""
        
def showlist(request):
    
    
    show_all = Item.objects.all()
    #test = " ,".join([i.title for i in show_all])
    template = loader.get_template('activity/activitylist.html')
    context = {
        'show_all': show_all,
    }
    #return HttpResponse(test)
    #return HttpResponse (template.render(context, request))
    return render(request, 'activity/activitylist.html', context)

def detail(request, item_id):
    get_item = Item.objects.get(pk=item_id)
    context = {
        'get_item': get_item,
    }
    return render(request, 'activity/detail.html', context)


def timeinfo(requst, item_id):
    time = "Time duration of activity: "
    return HttpResponse(time % item_id)


