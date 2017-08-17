from django.conf.urls import url
from .views import OrganizationList, OrganizationLinkList, OrganizationLinkRetrieve

urlpatterns = [
    url(r'^$', OrganizationList.as_view(), name="organizations_list"),
    url(r'^links/$', OrganizationLinkList.as_view(), name="organizations_link_list"),
    url(r'^links/(?P<pk>[0-9]+)/$', OrganizationLinkRetrieve.as_view(),
        name="organizations_link_detail"),
]
