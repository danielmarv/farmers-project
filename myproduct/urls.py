from django.urls import path
from .import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('', views.landing, name='landing'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('order/', views.order, name='dashboard-order'),
    #path('farmer-board/', views.farmer_board, name='farmer-board'),
    path('farmer-board/', staff_member_required(views.farmer_board), name='farmer-board'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_success/', views.success_add, name='add_success'),
    path('products/', views.products, name='dashboard-products'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('product_update/<int:pk>/', views.product_update, name='product_update'),
    path('product_edit/', views.product_edit, name='product_edit'),
    path('sell_list/', views.sell_list, name='sell_list'),
    path('add_sell/', views.add_sell, name='add_sell'),
    path('sell_dash/', views.sell_dash, name='sell_dash'),
    path('add_sell_cattle/', views.add_sell_cattle, name='add_sell_cattle'),
    path('add_sell_cereals/', views.add_sell_cereals, name='add_sell_cereals'),
    path('add_sell_legumes/', views.add_sell_legumes, name='add_sell_legumes'),
    path('add_sell_roottubers/', views.add_sell_roottubers, name='add_sell_roottubers'),
    path('Sell_roottubers_delete/<int:pk>/', views.Sell_roottubers_delete, name='Sell_roottubers_delete'),
    path('Sell_poultry_delete/<int:pk>/', views.Sell_poultry_delete, name='Sell_poultry_delete'),
    path('Sell_legumes_delete/<int:pk>/', views.Sell_legumes_delete, name='Sell_legumes_delete'),
    path('Sell_cereals_delete/<int:pk>/', views.Sell_cereals_delete, name='Sell_cereals_delete'),
    path('Sell_cattle_delete/<int:pk>/', views.Sell_cattle_delete, name='Sell_cattle_delete'),
    path('sell_update/', views.sell_update, name='sell_update'),
    path('product/add-to-cart/<str:product>/<str:price>/', views.add_to_cart, name='add_to_cart'),
    path('product/cart/', views.cart_view, name='cart_view'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('remove_from_cart/<str:product>/', views.remove_from_cart, name='remove_from_cart'),

]