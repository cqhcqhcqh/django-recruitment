from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

# 定义单选的 Job_types
Job_types = [(0, "技术类"),
             (1, "测试类"),
             (2, "运营类"),
             (3, "产品类"),
             (4, "iOS 开发工程师"),
             (5, "安卓开发工程师"),
             (6, "音视频开发工程师")]

Job_citys = [(0, "上海"),
             (1, "广州"),
             (2, "北京"),
             (3, "深圳")]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=Job_types, verbose_name="职位类别")
    job_name = models.CharField(blank=False, max_length=1024, verbose_name="职位名称")
    job_city = models.SmallIntegerField(blank=False, choices=Job_citys, verbose_name="岗位城市")
    job_responsibility = models.TextField(blank=False, max_length=1024, verbose_name="职位职责")
    job_requirements = models.TextField(blank=False, max_length=255, verbose_name="任职要求")
    # creator = models.CharField(blank=False, max_length=255, verbose_name="创建人") 需要用户手动输入，不友好，所以定义成系统用户
    # 定义成系统自带的用户（当前登录使用用户）
    # 使用 models 里面的外键引用
    # Django 里面可以用 foreignkey 来表示，这个字段引用的是另外一个模型对象
    # 因为是外键引用，当 creator（系统管理用户）被删除的时候，creator 发布的职位应该如何处理
    # 让职位无效，删除掉，还是怎么处理呢
    # 删除用户，外键管理怎么处理的逻辑
    # 在 Django 中可以用 on_delete 属性来决定如何处理这个行为
    # on_delete 有几种：默认直接忽略这条数据（Job？），级联删除（删除 Job？），关联数据设置为 NULL（Creator？）
    creator = models.ForeignKey(User, verbose_name="创建人", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改时间", default=datetime.now)