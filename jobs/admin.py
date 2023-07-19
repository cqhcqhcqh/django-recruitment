from django.contrib import admin
from jobs.models import Job
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    # 指定了在编辑（添加）页面哪些字段不需要展示
    # 让其自动生成字段对应的值
    exclude = ("creator", "created_date", "modified_date")
    # 列表也需要展示哪些字段
    list_display = ("job_type", "job_name", "creator", "job_city", "created_date", "modified_date")

    # 如果不重写 `save_model` 的话 creator 字段是没有值的，它也没有默认值
    # 而 created_date 和 modified_date 是有默认值的
    # 保存一个模型到数据库之前，做一个操作
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Job, JobAdmin)