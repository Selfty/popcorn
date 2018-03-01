from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Serials, Topserials
from django.http import JsonResponse
from django.views.generic.base import View
from django_ajax.decorators import ajax

def post_list(request):
    posts = Post.objects.order_by('-created_date')[:12]
    toppost = Topserials.objects.first()
    return render(request, 'serials/post_list.html', {'posts' : posts, 'toppost' : toppost})

def post_detail(request, name, sn, en):

	#episode nebo 404

    post = get_object_or_404(Post, name=name, serie=sn, episode=en)
    toppost = Topserials.objects.first()
	#next episode

    next_ep = int(en)+1
    next_se = int(sn)+1

    if Post.objects.filter(name=name,serie=sn,episode=next_ep):
    	next = Post.objects.filter(name=name,serie=sn,episode=next_ep).first()
    elif Post.objects.filter(name=name,serie=next_se):
        next = Post.objects.filter(name=name,serie=next_se).order_by('episode').first()
    else:
    	next = None

	#prev episode

    prev_ep = int(en)-1
    prev_se = int(sn)-1

    if Post.objects.filter(name=name,serie=sn,episode=prev_ep):
    	prev = Post.objects.filter(name=name,serie=sn,episode=prev_ep).first()
    elif Post.objects.filter(name=name,serie=prev_se):
        prev = Post.objects.filter(name=name,serie=prev_se).order_by('episode').last()
    else:
    	prev = None
	
	#serial

    serial = get_object_or_404(Serials, name=name)
		
    return render(request, 'serials/post_detail.html', {'post' : post,'next' : next,'prev' : prev,'toppost' : toppost, 'serial' : serial})

def serials(request):

	#episode nebo 404

    serials = Serials.objects.all()
    #episodes = get_object_or_404(Post, name=name)
    toppost = Topserials.objects.first()
    return render(request, 'serials/serials.html', {'serials' : serials,'toppost' : toppost})

def serial(request, name):
    series = []
    serial = get_object_or_404(Serials, name=name)
    episodes = Post.objects.filter(name=name)
    episodes = episodes.values('serie').distinct()
    
    for ep in episodes:
        series.append(Post.objects.filter(name=name, serie=ep['serie']).order_by('episode'))

    return render(request, 'serials/serial.html', {'serial' : serial, 'series' : series})
    
@ajax
def get(request, uid):
    serial = Serials.objects.filter(name__contains=uid)
    if serial :
        return {'serial' : serial}
    else:
        return {'serial' : ''}

@ajax
def gett(request):
    return {'serial' : ''}

def googlebc7a06bd22316fbfhtml(request):
    return render(request, 'serials/googlebc7a06bd22316fbf.html',{})

