from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.main ),
    url(r'^test/$', views.test_main),
    url(r'^page/(\d+)/$', views.test_main),
    url(r'^form/$', views.form_view)
]
