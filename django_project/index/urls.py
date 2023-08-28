from django.urls import path
from .views import IndexView, OtherPageView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('other/', OtherPageView.as_view(), name='other_page'),

    # path('update_cache/', IndexView.as_view(), name='update_cache'),  # Update Cache URL yapılandırması


]
