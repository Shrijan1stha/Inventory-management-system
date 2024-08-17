from django.urls import path
from .views import login, group_listing, register, ProductApiView, ProductCategoryApiView, DepartmentApiView, SupplierApiView, PurchaseApiView, ProductCategoryApiView2, DepartmentApiView2, SupplierApiView2, PurchaseApiView2

urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('roles/',group_listing),



    path('product/',ProductApiView.as_view({'get':'list','post':'create'}),name='product'),
    path('product/<int:pk>/',ProductApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='product-detail'),

    path('product/category/',ProductCategoryApiView.as_view({'get':'list','post':'create'}),name='productCategory'),
    path('product/category/<int:pk>/',ProductCategoryApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='product-category-detail'),
    
    path('department/',DepartmentApiView.as_view({'get':'list','post':'create'}),name='department'),
    path('department/<int:pk>',DepartmentApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='department-detail'),
    
    path('supplier/',SupplierApiView.as_view({'get':'list','post':'create'}),name='supplier'),
    path('supplier/<int:pk>',SupplierApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='supplier-detail'),
    
    path('purchase/',PurchaseApiView.as_view({'get':'list','post':'create'}),name='purchase'),
    path('purchase/<int:pk>',PurchaseApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='purchase-detail'),

    path('product-category2/',ProductCategoryApiView2.as_view(),name='product-category'),
    path('department2/',DepartmentApiView2.as_view(),name='depart'),
    path('supplier2/',SupplierApiView2.as_view(),name='supp'),
    path('purchase2/',PurchaseApiView2.as_view(),name='purch')
]