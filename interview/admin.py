import logging

from django.contrib import admin
from interview.models import Candidate
# Register your models here.

# __name__ 就是当前模块（interview) 当前运行的脚本的名字（admin）
logger = logging.getLogger(__name__)
logger.info("custom logger")
# logger.info("%s exported %s candidate records" (request.user, len(queryset)))

class CandidateAdmin(admin.ModelAdmin):
    # 定义搜索字段
    search_fields = ('user_name', 'city', 'phone', 'email', 'bachelor_school')

    # 定义过滤字段（枚举）
    list_filter = ('city', 'first_result', 'second_result', 'hr_result', 'first_interviewer', 'second_interviewer', 'hr_interviewer')

    # 定义默认排序规则
    # 先用 hr_result 排序，再 second_result，最后 first_result
    ordering = ('hr_result', 'second_result', 'first_result')

    exclude = ('creator', 'created_date', 'modified_date')

    list_display = ('user_name', 'city','bachelor_school',
                    'first_result', 'first_interviewer',
                    'second_result', 'second_interviewer',
                    'hr_level', 'hr_result',
                    'last_editor')

    fieldsets = (
        (None, {'fields': ("user_id", ("user_name", "city", "phone"), ("email", "apply_position", "born_address"), ("gender", "candidate_remark", "bachelor_school", "master_school", "doctor_school"), "major", "degree", "test_score_of_general_ability", "paper_score", "last_editor")}),
        ('第一轮基础面试记录', {'fields': (("first_score", "first_learning_ability", "first_professional_competency"), "first_advantage", "first_disadvantage", ("first_result", "first_interviewer", "first_remark"),)}),
        ('第二轮专业面试记录', {'fields': (("second_score", "second_learning_ability", "second_professional_competency"), ("second_pursue_of_excellence", "second_communication_ability", "second_pressure_score"), "second_advantage", "second_disadvantage", ("second_result", "second_recommend_position", "second_interviewer"), "second_remark",)}),
        ('HR复试记录', {'fields': ("hr_level", ("hr_responsibility", "hr_communication_ability", "hr_logic_ability", "hr_potential"), "hr_advantage", "hr_disadvantage", "hr_result", "hr_interviewer", "hr_remark",)})
    )
admin.site.register(Candidate, CandidateAdmin)