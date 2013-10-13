from django.conf.urls import patterns, include, url
from tastypie.api import Api
from recommender.api import UserResource, VideoGameResource, ReviewResource, AttributeOptionResource, VideoGameAttributeResource
from recommender import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(VideoGameResource())
v1_api.register(ReviewResource())
v1_api.register(AttributeOptionResource())
v1_api.register(VideoGameAttributeResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recommender.views.home', name='home'),
    # url(r'^recommender/', include('recommender.foo.urls')),

    url(r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.HEROKU_PRODUCTION:
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve',
                                {'document_root': settings.STATIC_ROOT}),
                            )
