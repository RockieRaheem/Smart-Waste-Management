from django.urls import path
from .views import CollectionRouteListCreateView, CollectionRouteUpdateView

urlpatterns = [
    path('collection-routes/', CollectionRouteListCreateView.as_view(), name='collection-route-list'),
    path('collection-routes/<int:pk>/', CollectionRouteUpdateView.as_view(), name='collection-route-update'),
]
