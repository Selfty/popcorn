from django.conf.urls import include, url
from django.contrib import admin
app_name="popcorn"
urlpatterns = [
    # Examples:
    # url(r'^$', 'popcorn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^googlebc7a06bd22316fbf\.html$', lambda r: HttpResponse("google-site-verification: googlebc7a06bd22316fbf.html", mimetype="text/plain")),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", mimetype="text/plain")),
    url(r'', include('serials.urls')),

]
