"""
Root level URLs to apply.

This file is a root level url file, intended to include app url files and 
errors.

TODO: Handle error pages.
"""

from django.conf.urls import include, patterns, url

urlpatterns = patterns(
    '',
    url(r'^', include('willmoggridge.urls')),
)
