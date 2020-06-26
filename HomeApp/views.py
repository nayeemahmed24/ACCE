from django.shortcuts import render
from .models import Carousel, Notice, Gallery


# Create your views here.


def index_view(request):
    carousels = Carousel.objects.all().order_by('-created_at')[:3]
    all_events = Notice.objects.all().order_by('-created_at')[:5]
    carousels = list(carousels)

    context = {
        "carousels": carousels,
        "events": all_events,
    }
    return render(request, 'HomeApp/index.html', context)


def events(request):
    current_event = Notice.objects.all()
    if current_event.count() > 0:
        current_event = current_event.order_by('-created_at')[:1].get()
    all_events = Notice.objects.all()
    if all_events.count() > 0:
        all_events = all_events.exclude(pk=current_event.pk).order_by('-created_at')[:5]
    context = {
        "events": all_events,
        "current_event": current_event
    }
    return render(request, 'HomeApp/UpcomingEventPage.html', context)


def upcoming_events(request, pk):
    try:
        current_event = Notice.objects.get(pk=pk)
    except Exception as e:
        print(e)
        current_event = None
    all_events = Notice.objects.all()
    if all_events.count() > 0:
        all_events = all_events.exclude(pk=pk).order_by('-created_at')[:5]
    context = {
        "events": all_events,
        "current_event": current_event
    }
    return render(request, 'HomeApp/UpcomingEventPage.html', context)


def gallery_view(request):
    notices = Notice.objects.all().order_by('-created_at')
    list_of_event = []
    for i in notices:
        gallery_by_event = Gallery.objects.filter(event=i)
        list_of_event.append((i, gallery_by_event))

    context = {
        "notices": notices,
        "list_of_event": list_of_event,
    }
    return render(request, 'HomeApp/GalleryPage.html', context)


def about_us_view(request):
    context = {

    }
    return render(request, 'HomeApp/AboutPage.html', context)


def contact_view(request):
    return render(request, 'HomeApp/ContactPage.html')
