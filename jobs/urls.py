from django.urls import re_path
from jobs import views

urlpatterns = [
    re_path(r"^joblist/", views.joblist, name="joblist"),
    # \d+ 匹配数字
    # /$ 以 `/`结尾
    # (?P<job_id>\d+) 中的 (?P<job_id> 部分是一个命名捕获组，用于在 URL 模式中捕获特定的值，并将其传递给视图函数作为参数
    # 给 job(request, job_id) 函数来获取 render 的结果
    re_path(r"^job/(?P<job_id>\d+)/$", views.job, name="job"),

    # 首页自动跳转到 职位列表
    # 职业列表页现在作为我们的首页
    re_path(r"$", views.joblist, name="name")
]