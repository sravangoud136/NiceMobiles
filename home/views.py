from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from home import models,forms
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView,DetailView
from .models import ServiceProvider
from .filters import JobFilter
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView


def job_render_pdf_view(request,job_id):
    job_sel = models.Job.objects.get(id = job_id)
    template_path = 'job_invoice.html'
    context = {'job':job_sel}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+job_sel.jobReferenceNumber+'.pdf"'
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

    

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def showjobs(request):
    jobs=models.Job.objects.all()
    context={
        "jobs": jobs
    }
    return render(request, 'jobs.html',context)
def create_job(request):
    jobform=forms.JobForm()
    if request.method=="POST":
        jobdata=forms.JobForm(request.POST)
        if jobdata.is_valid():
            jobdata.save()
        return redirect('showjobs')
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
    if jobForm.is_valid():
       jobForm.save()
       return redirect('showjobs')
    return render(request, 'create_job.html', {'jobform':jobForm,'update':True})
def show_all_jobs_page(request):
    context={}
    
    filtered_jobs=JobFilter(request.GET,queryset=models.Job.objects.all())
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
    
    context["registered_jobs_count"]=models.Job.objects.filter(jobStatus='REGISTERED').count()
    context["inprogress_jobs_count"]=models.Job.objects.filter(jobStatus='IN_PROGRESS').count()
    context["closed_jobs_count"]=models.Job.objects.filter(jobStatus='CLOSED').count()
    context["delivered_jobs_count"]=models.Job.objects.filter(jobStatus='DELIVERED').count()
    #print(registered_jobs_count,inprogress_jobs_count,closed_jobs_count,delivered_jobs_count)
    
    #print(registered_count)
    return render(request,'jobs.html',context=context)

class UserLogin(LoginView):
    
    template_name = 'login.html'
    
class UserLogout(LogoutView):
    
    template_name = 'logout.html'
    
class ViewJob(DetailView):
    model=models.Job
    template_name="view_job.html"
    context_object="job"
    
    '''def get_object(self, queryset=None):
        return models.Job.objects.get(id=self.kwargs.get("pk"))'''
    
    


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
