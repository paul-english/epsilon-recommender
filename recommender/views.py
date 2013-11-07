from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q

from recommender.models import VideoGame

def home(request):
    title = "Home"

    video_games = VideoGame.objects.filter(~Q(name='') &
                                            ~Q(description='') &
                                            Q(ign_image__isnull=False))[:8]

    return render_to_response('home.html',
                              locals(),
                              context_instance=RequestContext(request))

def recommendations(request):
    title = "Recommendations"

    video_games = VideoGame.objects.filter(~Q(name='') &
                                            ~Q(description='') &
                                            Q(ign_image__isnull=False))[:8]

    return render_to_response('recommendations.html',
                              locals(),
                              context_instance=RequestContext(request))

def search_and_rate(request):
    title = "Search and Rate"

    video_games = VideoGame.objects.filter(~Q(name='') &
                                            ~Q(description='') &
                                            Q(ign_image__isnull=False))[:5]

    return render_to_response('search_and_rate.html',
                              locals(),
                              context_instance=RequestContext(request))
