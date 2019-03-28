from django.shortcuts import render
from .models import Events, Notice, Faculty, Staff

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def homepage(request):
    notices = Notice.objects.all().order_by('date')
    events = Events.objects.all()
    return render(request, 'ict/index.html', {'notices': notices, 'events': events})

def notice(request):
    notices = Notice.objects.all().order_by('date')
    notice_list = {'notice_list': notices}
    return render(request, 'ict/notice-board.html', notice_list)

def achievements(request):
    return render(request, 'ict/achievements.html')

def resources(request):
    return render(request, 'ict/resources.html')

def downloads(request):
    return render(request, 'ict/downloads.html')

def programs(request):
    return render(request, 'ict/programs.html')

def admission(request):
    return render(request, 'ict/admission.html')

def curriculum(request):
    return render(request, 'ict/curriculum.html')

def academic_calendar(request):
    return render(request, 'ict/academic-calendar.html')

def research_groups(request):
    return render(request, 'ict/research_groups.html')

def publications(request):
    return render(request, 'ict/publications.html')

def announcement(request):
    return render(request, 'ict/announcement.html')

def notice_and_events(request):
    return render(request, 'ict/notice_and_events.html')

def alumni(request):
    return render(request, 'ict/alumni.html')

def sitemap(request):
    return render(request, 'ict/sitemap.html')

def faculty(request):
    faculties = Faculty.objects.all()
    faculty_list = {'faculty_list': faculties}
    return render(request, 'ict/faculty.html', faculty_list)

def stuff(request):
    stuffs = Staff.objects.all()
    stuffs_list = {'stuffs_list': stuffs}
    return render(request, 'ict/stuff.html', stuffs_list)
