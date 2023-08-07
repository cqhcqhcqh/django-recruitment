from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from jobs.models import Job
from jobs.models import Job_citys, Job_types

from django.http import Http404

# Django 视图加载有好几种方法
# 1. 利用函数来定义
# 2. 利用视图的类来定义
def joblist(request):
    job_list = Job.objects.order_by('job_type')

    # job_list 拿到的应该不是 Job 对象数组？
    # 还说可以给 Job 对象动态添加 type_name 和 city_name 属性？
    # type_name 和 city_name 显然不是 Job 的属性
    for job in job_list:
        job.type_name = Job_types[job.job_type][1]
        job.city_name = Job_citys[job.job_city][1]

    template = loader.get_template('joblist.html')
    context = {'job_list': job_list}
    return HttpResponse(template.render(context, request))

def job(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.type_name = Job_types[job.job_type][1]
        job.city_name = Job_citys[job.job_city][1]

        # 1
        # context = {'job': job}
        # template = loader.get_template('job.html')
        # return HttpResponse(template.render(context))

        # 2
        return render(request, 'job.html', {'job': job})
    except Job.DoesNotExist:
        raise Http404('Job does not exist')
