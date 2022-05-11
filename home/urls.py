from django.urls import path
from home import views
from .views import UserLogin,UserLogout,ASCCreateView,ASCListView,ASCDetailView,ASCUpdateView,ASCDeleteView

#from .views import ServiceProviderListView,UserLogin,UserLogout


urlpatterns = [
    path('',views.index,name="index"),
    path('login/',UserLogin.as_view(),name="login"),
    path('logout/',UserLogout.as_view(),name="logout"),
    path('create_job/',views.create_job,name="create_job"),
    path('showjobs/',views.show_all_jobs_page,name="showjobs"),
    path('update_job/<int:job_id>',views.update_job,name="update_job"),
    path('printreceipt/<int:job_id>',views.job_render_pdf_view,name="printreceipt"),
    # path('view_job/<int:pk>',ViewJob.as_view(),name="view_job"),
    path('view_job/<int:pk>',views.viewjob,name="view_job"),
    path('create_asc/',ASCCreateView.as_view(),name="create_asc"),
    path('show_asc/',ASCListView.as_view(),name="show_asc"),
    path('show_asc/<int:pk>',ASCDetailView.as_view(),name="view_asc_detail"),
    path('update_asc/<int:pk>',ASCUpdateView.as_view(),name="update_asc"),
    path('delete_asc/<int:pk>',ASCDeleteView.as_view(),name="delete_asc"),
    # path('ASC_login/',views.asc_login,name="ASC_login"),
    # path('ASC_logout/',views.asc_logout,name="ASC_logout"),
    
    
    
   
    
    
    
    #path('downloadinvoice/',views.render_pdf_view,name="downloadinvoice"),
    #path('showserviceprovidesppdfrs/',ServiceProviderListView.as_view(),name="splist"),
    #path('downloadinvoice/<pk>',views.sp_render_pdf_view,name="sppdf"),
    
]
