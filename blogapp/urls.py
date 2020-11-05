from django.urls import path
from . import views
from .views import RegisterView, LoginView

app_name = 'blogapp'

urlpatterns = [
# 	path('<post>/', api_detail_post_view, name="detail"),
# 	path('<post>/update', api_update_post_view, name="update"),
# 	path('<post>/delete', api_delete_post_view, name="delete"),
	path('', views.apiOverview, name="api-overview"),
    path('post-list/', views.postList, name="post-list"),
    path('post-detail/<str:pk>/', views.postDetail, name="post-detail"),
    path('post-create/', views.postCreate, name="post-create"),
    path('post-update/<str:pk>/', views.postUpdate, name="post-update"),
    path('post-delete/<str:pk>/', views.postDelete, name="post-delete"),
    
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),


]