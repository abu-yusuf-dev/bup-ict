from django.urls import path
from ict import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('notice/', views.notice, name='notice'),
    path('achievements/', views.achievements, name='achievements'),
    path('resources/', views.resources, name='resources'),
    path('downloads/', views.downloads, name='downloads'),
    path('programs/', views.programs, name='programs'),
    path('admission/', views.admission, name='admission'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('academic_calendar/', views.academic_calendar, name='academic_calendar'),
    path('research_groups/', views.research_groups, name='research_groups'),
    path('publications/', views.publications, name='publications'),
    path('announcement/', views.announcement, name='announcement'),
    path('notice_and_events/', views.notice_and_events, name='notice_and_events'),
    path('alumni/', views.alumni, name='alumni'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('faculty/', views.faculty, name='faculty'),
    path('staff/', views.stuff, name='stuff'),
]
