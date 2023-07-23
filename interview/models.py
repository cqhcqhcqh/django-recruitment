from django.db import models

FIRST_INTERVIEW_RESULT_TYPE = ((u'建议复试', u'建议复试'), (u'待定', u'待定'), (u'待定', u'待定'))

DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))

HR_SCORE_TYPES = ((u'S', u'S'), (u'A', u'A'), (u'B', u'B'), (u'C', u'C'))

INTERVIEW_RESULT_TYPE = ((u'建议录取', u'建议录取'), (u'待定', u'待定'), (u'放弃', u'放弃'))

# Create your models here.
class Candidate(models.Model):
    # 基础信息
    user_id = models.IntegerField(unique=True, blank=True, null=True, verbose_name=u'应聘者ID')
    user_name = models.CharField(max_length=135, verbose_name=u'姓名')
    city = models.CharField(max_length=135, verbose_name=u'城市')
    phone = models.CharField(max_length=135, verbose_name=u'手机号码')
    email = models.EmailField(max_length=135, blank=True, verbose_name=u'邮箱')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=u'应聘职位')
    born_address = models.CharField(max_length=135, blank=True, verbose_name=u'生源地')
    gender = models.CharField(max_length=135, blank=True, verbose_name=u'性别')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name=u'候选人信息备注')

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=u'本科学校')
    master_school = models.CharField(max_length=135, blank=True, verbose_name=u'研究生学校')
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'博士生学校')
    major = models.CharField(max_length=135, blank=True, verbose_name=u'专业')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=u'学位')

    # 综合能力测评成绩，笔试测评成绩
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True,
                                                        max_digits=3, blank=True, verbose_name=u'综合能力测试成绩')
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name=u'笔试成绩')

    # 第一轮面试记录
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'初试分')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                verbose_name=u'学习能力得分')
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                         verbose_name=u'专业能力得分')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'优势')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'顾虑和不足')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'初试结果')
    first_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'面试官')
    first_remark = models.CharField(max_length=135, blank=True, verbose_name=u'初试备注')

    # 第二轮面试记录
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                       verbose_name=u'专业复试分')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name=u'学习能力得分')
    second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                        verbose_name=u'专业能力得分')
    second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                      verbose_name=u'追求卓越分')
    second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                       verbose_name=u'沟通能力分')
    second_pressure_score = models.DecimalField(decimal_places=1, null=True, blank=True, max_digits=2,
                                                verbose_name=u'抗压能力分')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'优势')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'顾虑和不足')
    second_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name=u'专业复试结果')
    second_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'建议方向或推荐部门')
    second_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'面试官')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name=u'专业复试备注')

    # HR 终面
    hr_level = models.CharField(max_length=10, choices=HR_SCORE_TYPES, blank=True, verbose_name=u'HR复试综合等级')
    hr_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPES, blank=True, verbose_name=u'HR责任心')
    hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPES, blank=True, verbose_name=u'HR坦诚沟通分')
    hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPES, blank=True, verbose_name=u'HR逻辑思维')
    hr_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPES, blank=True, verbose_name=u'HR发展潜力')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'优势')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'顾虑和不足')
    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'HR复试结果')
    hr_interviewer = models.CharField(max_length=135, blank=True, verbose_name=u'HR面试官')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name=u'复试备注')

    creator = models.CharField(max_length=135, blank=True, verbose_name=u'候选人数据的创建人')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modified_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=u'更新时间')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name=u'最后编辑者')

    class Meta:
        db_table = u'candidate'
        # 表对应页面上的显示名称（localhost:8118/admin 首页)
        verbose_name = u'应聘者'
        # 复数名称
        verbose_name_plural = u'所有应聘者'

    # Python 2 优先使用这个方法, 把对象转换成字符串: 如果没有 __unicode__() 方法，使用 __str__() 放阿飞
    def __unicode__(self):
        return self.user_name

    # Python 3 直接定义 __str__() 方法即可，系统使用这个方法把对象换成字符串 (`print(obj)` 会调用这个方法)
    def __str__(self):
        return self.user_name