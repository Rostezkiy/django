from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', DevicesHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', DevicesCategory.as_view(), name='category'),
    path('contact/', ContactFormView.as_view(), name='contact'),

]
