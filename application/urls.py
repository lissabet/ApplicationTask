from django.conf.urls import url, include
from .views import CategoryList, MainView, ItemDetail, CreateItem, CategotyView, CategoryViewSet, ItemViewSet, \
    DetailView, CreateItemView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'^detail-item', DetailView)
router.register(r'^create-new', CreateItemView)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^categories/$', CategoryList.as_view()),
    url(r'^main-page/$', MainView.as_view(), name='main-page'),
    url(r'^item-page/(?P<pk>[0-9]+)/$', ItemDetail.as_view(), name='item-page'),
    url(r'^create-item/$', CreateItem.as_view(), name='create-item'),
    url(r'^category-view/(?P<pk>[0-9]+)/$', CategotyView.as_view(), name='category-view'),
]

