from collection.backends import MyRegistrationView 

from django.contrib.auth.views import (
  password_reset,
  password_reset_done,
  password_reset_confirm,
  password_reset_complete,
  password_change,
  password_change_done,
)

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import (TemplateView, RedirectView,)
from collection import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$', 
      TemplateView.as_view(template_name='about.html'), 
      name='about'),
    url(r'^contact/$', 
      TemplateView.as_view(template_name='contact.html'), 
      name='contact'),

    # verse URLs 
    url(r'^verses/$',
      RedirectView.as_view(pattern_name='browse', permanent=True)),
    url(r'^verses/(?P<slug>[-\w]+)/$', 
      views.verse_detail,
      name='verse_detail'),
    url(r'^verses/(?P<slug>[-\w]+)/edit/$', 
      views.edit_verse,
      name='edit_verse'),
    
    # user registration URLs
    url(r'^accounts/register/$',
      MyRegistrationView.as_view(),
      name='registration_register'),
    url(r'^accounts/create_verse/$', 
      views.create_verse,
      name='registration_create_verse'),

    # browse views
    url(r'^browse/$',
      RedirectView.as_view(pattern_name='browse', permanent=True)),
    url(r'^browse/ref/$',
      views.browse_by_ref, name='browse'),
    url(r'^browse/ref/(?P<initial>[-\w]+)/$',
      views.browse_by_ref, name='browse_by_ref'),

    # password reset urls
    url(r'^accounts/password/reset/$',
      password_reset,
      {'template_name': 
      'registration/password_reset_form.html'},
      name="password_reset"),
    url(r'^accounts/password/reset/done/$',
      password_reset_done,
      {'template_name': 
      'registration/password_reset_done.html'},
      name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
      password_reset_confirm,
      {'template_name': 
      'registration/password_reset_confirm.html'},
      name="password_reset_confirm"),
    url(r'^accounts/password/done/$',
      password_reset_complete,
      {'template_name': 
      'registration/password_reset_complete.html'},
      name="password_reset_complete"),

    # password change urls
    url(r'^accounts/password/change/$',
      password_change,
      {'template_name': 
      'registration/password_change_form.html'},
      name="password_change"),
    url(r'^accounts/password/change/done/$',
      password_change_done,
      {'template_name': 
      'registration/password_change_done.html'},
      name="password_change_done"),

    url(r'^accounts/', 
      include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]
