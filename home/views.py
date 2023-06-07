from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from home import models,forms
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import ServiceProvider
from .filters import JobFilter
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
import pdfkit
import os
from InvoiceGenerator import settings
  




def asc_login(request):
    asc_login_form=forms.ASCLoginForm()
    return render(request,"asc_login.html",{"form":asc_login_form})
def asc_logout(request):
    pass
def job_render_pdf_view(request,job_id):
    
    job_sel = models.Job.objects.get(id = job_id)
    adminuser=models.User.objects.get(username="admin")
    
    asc=models.ServiceProvider.objects.get(user=request.user)
    owner=models.ServiceProvider.objects.get(user=adminuser)
    
    
    template_path = 'job_invoice.html'
    context = {'job':job_sel,'current_user':request.user,'asc':asc,'owner':owner}
    
    filename=str(job_sel.id)+"_"+str(job_sel.customerName)+".pdf"
    template = get_template(template_path)
    html = template.render(context)
    #pdf_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'pdf', filename)
    pdf = pdfkit.from_string(html,False,options={"enable-local-file-access": ""})
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response
    

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

'''def showjobs(request):
    jobs=models.Job.objects.all()
    context={
        "jobs": jobs
    }
    return render(request, 'jobs.html',context)
'''
def create_job(request):
    jobform=forms.JobForm()
    if request.method=="POST":
        jobdata=forms.JobForm(request.POST)
        if jobdata.is_valid():
            jobdata.instance.author=request.user
            jobdata.save()
            return redirect('showjobs')
        else:
            print("this path")
            return render(request,"create_job.html",{"jobform":jobdata})
           
         #jobform=forms.JobForm()
    context={
    "jobform":jobform
    }
    return render(request,"create_job.html",context)
def update_job(request, job_id):
    job_id = int(job_id)
    try:
        job_sel = models.Job.objects.get(id = job_id)
    except job.DoesNotExist:
        return redirect('showjobs')
    jobForm = forms.JobForm(request.POST or None, instance = job_sel)
    comment=request.POST.get('comment')
    
    curr_status=job_sel.jobStatus
    new_status=request.POST.get('jobStatus')
    
   
    
    if jobForm.is_valid():    
       jobForm.save()
       if curr_status != new_status: 
            hisdata=forms.HistoryForm() 
            hisdata.instance.author=request.user
            hisdata.instance.job=job_sel 
            hisdata.instance.comment="status changed from "+curr_status+" to "+new_status+". Comment from Author: "+ comment 
            hisdata.instance.save()
       return redirect('showjobs')
    return render(request, 'create_job.html', {'jobform':jobForm,'update':True})
def show_all_jobs_page(request):
    context={}
    
    filtered_jobs=JobFilter(request.GET,queryset=models.Job.objects.filter(author=request.user))
    #print(filtered_jobs.qs)
    context['filtered_jobs']=filtered_jobs
    paginator = Paginator(filtered_jobs.qs.order_by('-CreatedTime'), 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    #allJobs=models.Job.objects.values('jobStatus').annotate(status_count=Count('jobStatus'))
    
    #StatusDict=[i['jobStatus']+"-"+str(i['status_count']) for i in allJobs]
    #context['StatusDict']=StatusDict
    #print(StatusDict)  
    #print(allJobs)
    
    context["registered_jobs_count"]=models.Job.objects.filter(jobStatus='REGISTERED',author=request.user).count()
    context["inprogress_jobs_count"]=models.Job.objects.filter(jobStatus='IN_PROGRESS',author=request.user).count()
    context["closed_jobs_count"]=models.Job.objects.filter(jobStatus='CLOSED',author=request.user).count()
    context["delivered_jobs_count"]=models.Job.objects.filter(jobStatus='DELIVERED',author=request.user).count()
    #print(registered_jobs_count,inprogress_jobs_count,closed_jobs_count,delivered_jobs_count)
    
    #print(registered_count)
    return render(request,'jobs.html',context=context)

class UserLogin(LoginView):
    
    template_name = 'login.html'
    
class UserLogout(LogoutView):
    
    template_name = 'logout.html'



    
# class ViewJob(DetailView):
#     model=models.Job
#     template_name="view_job.html"
#     context_object='job'

def viewjob(request,pk):
    job_sel=models.Job.objects.get(id=pk)
    
    if job_sel is not None:
        h=list(models.History.objects.filter(job=job_sel).order_by('-updated_time'))
        
        
        if h:
            # print("yes")
            context={
                "job":job_sel,
                "history":h
                }
        else:
            # print("No")
            context={
                "job":job_sel,
                "history":None
                }
        
    return render(request, 'view_job.html',context)
        
# class ViewHistory(ListView):
#     model=models.History
#     template_name="view_job.html"
#     context_object="history"
#     def get_queryset(self,*args):
#         return models.History.objects.filter(job=models.Job.objects.filter(job_id=self.args[0]))
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)    
#         context['History'] = Vechile.objects.all()
#         return context
    
    

    
    '''def get_object(self, queryset=None):
        return models.Job.objects.get(id=self.kwargs.get("pk"))'''
    
    
class ASCCreateView(CreateView):
    model=models.ServiceProvider
    fields="__all__"
    template_name="create_asc.html"
    success_url="/"
    
    
class ASCListView(ListView):
    model=models.ServiceProvider
    template_name="show_asc.html"
    

class ASCDetailView(DetailView):
    model=models.ServiceProvider
    template_name="view_asc.html"
   
    
    
class ASCUpdateView(UpdateView):
    model=models.ServiceProvider
    template_name="update_asc.html"
    fields="__all__"
    success_url="/"
    
class ASCDeleteView(DeleteView):
    model=models.ServiceProvider
    template_name="delete_asc.html"
    success_url="/"
    
    


'''class ServiceProviderListView(ListView):
    model=ServiceProvider
    template_name="sp.html"
    
def sp_render_pdf_view(request,*args,**kwargs):
    pk=kwargs.get('pk')
    sp=get_object_or_404(ServiceProvider,pk=pk)
    template_path = 'invoice.html'
    context = {'sp':sp}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    '''

'''def render_pdf_view(request):
    template_path = 'invoice.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    '''
