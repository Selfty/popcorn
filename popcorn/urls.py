from django.conf.urls import include, url
from django.contrib import admin
app_name="popcorn"
urlpatterns = [
    # Examples:
    # url(r'^$', 'popcorn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('serials.urls')),
    

]


