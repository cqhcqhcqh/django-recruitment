from interview import dingtalk

# 通知一面面试官有面试通知
def notify_interviewer(modeladmin, request, queryset):
    candidates = ""
    interviewers = ""
    for obj in queryset:
        candidates = obj.user_name + ";" + candidates
        interviewers = obj.first_interviewer + ";" + interviewers
    dingtalk.send("候选人 %s 进入面试关节，亲爱的面试官，请做好面试贮备： %s" %(candidates, interviewers))
