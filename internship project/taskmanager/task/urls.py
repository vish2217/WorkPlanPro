from django.contrib import admin
from django.urls import path
from task import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create-task', views.createTask, name='create-task'),
    path('register/', views.register, name='register'),
    path('viewtask/', views.viewtask, name='viewtask'),
    path('updatetask/<int:id>/', views.updatetask, name='updatetask'),
    path('deletetask/<int:id>/', views.deletetask, name='deletetask'),
    path('product',views.product,name='product'),
    path('solutions',views.solutions,name='solutions'),
    path('resources',views.resources,name='resources'),
    path('pricing',views.pricing,name='pricing'),
    path('enterprise',views.enterprise,name='enterprise'),
    path('customercare',views.customercare,name='customercare'),
    path('guide',views.guide,name='guide'),
    path('blog/', views.blog, name='blog'),
    path('faq/', views.faq, name='faq'),





]
