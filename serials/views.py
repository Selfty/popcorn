from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Serials, Topserials
from django.http import JsonResponse
from django.views.generic.base import View
from django_ajax.decorators import ajax

from django.contrib.sitemaps import Sitemap

def post_list(request):
    posts = Post.objects.order_by('-created_date')[:12]
    toppost = Topserials.objects.first()
    return render(request, 'serials/post_list.html', {'posts' : posts, 'toppost' : toppost})

def post_detail(request, name, sn, en):

	#episode nebo 404

    post = get_object_or_404(Post, name=name, serie=sn, episode=en)
    toppost = Topserials.objects.first()
	#next episode


    if Post.objects.filter(name = name,serie=sn,episode__gt=en).order_by('episode').first():
        next = Post.objects.filter(name = name,serie=sn,episode__gt=en).order_by('episode').first()
        print(1)
    elif Post.objects.filter(name = name,serie__gt=sn,episode__gte=1).order_by('serie','episode').first():
        next = Post.objects.filter(name = name,serie__gt=sn,episode__gte=1).order_by('serie','episode').first()
        print(2)
    else:
        next = None
	#prev episode

    if Post.objects.filter(name = name,serie=sn,episode__lt=en).order_by('-episode').first():
        prev = Post.objects.filter(name = name,serie=sn,episode__lt=en).order_by('-episode').first()
        print(1.1)
    elif Post.objects.filter(name = name,serie__lt=sn).order_by('-serie','-episode').first():
        prev = Post.objects.filter(name=name,serie__lt=sn).order_by('-serie','-episode').first()
        print(2.2)
    else:
        next = None



	
	#serial

    serial = get_object_or_404(Serials, name=name)
		
    return render(request, 'serials/post_detail.html', {'post' : post,'next' : next,'prev' : prev,'toppost' : toppost, 'serial' : serial})

def serials(request):

	#episode nebo 404

    serials = Serials.objects.all().order_by('title')
    #episodes = get_object_or_404(Post, name=name)
    toppost = Topserials.objects.first()
    return render(request, 'serials/serials.html', {'serials' : serials,'toppost' : toppost})

def serial(request, name):
    series = []
    serial = get_object_or_404(Serials, name=name)
    episodes = Post.objects.filter(name=name)
    episodes = episodes.values('serie').distinct().order_by('serie')
    
    for ep in episodes:
        series.append(Post.objects.filter(name=name, serie=ep['serie']).order_by('episode'))

    return render(request, 'serials/serial.html', {'serial' : serial, 'series' : series})
    
def dmca(request):
    return render(request, 'serials/dmca.html',{})

@ajax
def get(request, uid):
    serial = Serials.objects.filter(title__contains=uid).order_by('title')[:3]
    serials_dict = []
    for serie in serial:
        serial_dict = {
             'name' : serie.name,
	     'title' : serie.title
	              }
        serials_dict.append(serial_dict)
    if serial :
        return JsonResponse(serials_dict, safe=False)
    else:
        return JsonResponse(None)

@ajax
def gett(request):
    return JsonResponse({'serial' : ''}, safe = False)

class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created_date

class SerialsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Serials.objects.all()

    def lastmod(self, obj):
        return timezone.now()
