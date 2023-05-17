from django.urls import path 
from .views import generate_pdf
from .views import generate_excel_file
from . import views
urlpatterns=[
    path('dashboard/',views.index,name='dashboardindex'),
    path('staff/',views.staff,name='dashboardstaff'),
    path('product/',views.product,name='dashboardproduct'),
    path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
    path('product/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
    path('staff/detail/<int:pk>/',views.staff_detail,name='dashboardstaffdetail'),
    path('issueditems/',views.issued_items,name='dashboardissueditems'),
    path('pdf/',views.generate_pdf, name='generate_pdf'),
    path('generate-excel/', views.generate_excel_file, name='generate_excel_file'),
    path('issueditems/<int:pk>/review/',views.item_review,name='item_review'),

]