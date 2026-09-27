from django.http import HttpResponseRedirect
from django.template.defaultfilters import title
from events.forms import EventForm
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from . import data

def index(request: HttpRequest) -> HttpResponse:
    all_events = data.list_events()
    total_events = len(all_events)
    closed_events = len([e for e in all_events if e.get('status') in ('completed', 'cancelled')])
    active_events = total_events - closed_events

    events = all_events
    query = request.GET.get('query', '').lower()
    category = request.GET.get('category', '').lower()
    status = request.GET.get('status', '').lower()
    
    if query:
        events = [event for event in events if query in event['title'].lower() or query in event['description'].lower()]

    if category:
        events = [event for event in events if category in event['category'].lower()]

    if status:
        events = [event for event in events if status in event['status'].lower()]
        
    return render(
        request, 
        'events/index.html', 
        {
            'events': events, 
            'query': query, 
            'category': category, 
            'status': status,
            'total_events': total_events,
            'active_events': active_events,
            'closed_events': closed_events,
            'total_count': total_events,
            'active_count': active_events,
            'closed_count': closed_events,
        }
    )


def event_detail(request: HttpRequest, event_id: int) -> HttpResponse:
    event = data.get_event(event_id)
    if event is None:
        return HttpResponseNotFound("Событие не найдено")
    return render(request, 'events/detail.html', {'event': event})


def event_update(request: HttpRequest, event_id: int) -> HttpResponse:
    event = data.get_event(event_id)
    if event is None:
        return HttpResponseNotFound("Событие не найдено")
    if request.method == 'POST':
        form = EventForm(request.POST, initial=event)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            location = form.cleaned_data['location']
            status = form.cleaned_data['status']
            data.update_event(event_id, title=title, description=description, category=category, location=location, status=status)
            return HttpResponseRedirect(f'/events/{event_id}/')
    else:
        form = EventForm(initial=event)
    return render(request, 'events/edit.html', {'form': form, 'event': event})


def event_delete(request: HttpRequest, event_id: int) -> HttpResponse:
    event = data.get_event(event_id)
    if event is None:
        return HttpResponseNotFound("Событие не найдено")
    if request.method == 'POST':
        data.delete_event(event_id)
        return render(request, 'events/delete.html', {'deleted': True, 'event': event})

    return render(request, 'events/delete.html', {'event': event})


def event_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            location = form.cleaned_data['location']
            status = form.cleaned_data['status']
            data.create_event(title=title, description=description, category=category, location=location, status=status)
            return HttpResponseRedirect(f'/events/')
    else:
        form = EventForm()
    return render(request, 'events/create.html', {'form': form})