# 장고 메소드와 blog 어플리케이션에서 사용할 모든 views들을 불러옴

from django.conf.urls import url
from . import views

# 첫 번째 URL 패턴 추가
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]
