from django.conf.urls.defaults import *

from rst_viewer.apps.forms import ViewerForm
from rst_viewer.apps.views import ViewerFormPreview

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^$', include('rst_viewer.foo.urls')),
    url(r'^$', ViewerFormPreview(ViewerForm), name='viewer-form'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
