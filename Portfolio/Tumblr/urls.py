from django.conf.urls.defaults import *

urlpatterns = patterns("tumblr.views",
    url(r"^auth/$", "auth", name="tumblr_auth"),
    url(r"^callback/$", "callback", name="tumblr_auth_callback"),
    url(r"^post/$", "post", name="tumblr_post"),
)
