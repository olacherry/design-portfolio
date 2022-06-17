from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),

    path('works', views.works, name = 'works'),
    path('type', views.type, name = 'type'),
    path('network', views.network, name='network'),
    path('vk', views.vk, name='vk'),
    path('vk_a', views.vk_a, name='vk_a'),
    path('vk_c', views.vk_c, name='vk_c'),
    path('inst', views.inst, name='inst'),
    path('inst_p', views.inst_p, name='inst_p'),
    path('inst_s', views.inst_s, name='inst_s'),
    path('product', views.product, name='product'),
    path('product_m', views.product_m, name='product_m'),
    path('product_p', views.product_pr, name='product_p'),
    path('contact', views.contact, name='contact'),
]
