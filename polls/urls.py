from django.urls import path
from . import views

# URLconf에 이름공간(namespace)을 추가하여 같은 name이라도 앱마다 구분하기 위해!!!
app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
