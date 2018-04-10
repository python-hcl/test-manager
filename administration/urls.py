from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('test/section/edit/<int:id>/', views.sectionedit, name='section_edit'),
     path('test/section/add', views.addsection, name='add_section'),
     path('test/section', views.testsectionlist, name='test_section_list'),
     path('test/edit/<int:id>/', views.testedit, name='test_edit'),
     path('test/add', views.addtest, name='add_test'),
     path('test', views.testlist, name='test_list'),
     path('login', views.custom_login, name='custom_login'),
     path('logout', views.logout_function, name='logout_function'),
     path('user', views.user_list, name='user_list'),
     path('user/add', views.user_add, name='user_add'),
     path('user/edit/<int:id>/', views.user_edit, name='user_edit'),
]