import csv
from datetime import datetime
from django.http import HttpResponse

exportable_fields = ('user_name', 'city', 'phone', 'bachelor_school', 'degree', 'first_result',
                     'first_interviewer', 'second_result', 'second_interviewer',
                     'hr_result', 'hr_level', 'hr_remark', 'hr_interviewer')

def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=recuritment-candidate-list-%s.csv' %(
        datetime.now().strftime('%Y%M%D%H%M%S'),
    )
    field_list = exportable_fields

    # 根据类文件对象来创建一个 writer
    # 操作 writer 对象来进行 writerrow 写入行
    # 来影响类文件对象的存储内容
    # HTTPResponse 对象就是一个类文件对象
    # writer 对象来 writerow 实则改变的是 HTTPResponse 对象的
    # 存储内容
    writer = csv.writer(response)
    # 写入表头
    # `queryset.model._meta.get_field(f)`可以获取一个 ofield_object 对象
    # tongg
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list]
    )
    # 写入其他行（数据部分）
    for obj in queryset:
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            # 通过 field_object 对象 来获取每一行 field 对应的 value
            filed_value = field_object.value_from_object(obj)
            csv_line_values.append(filed_value)
        writer.writerow(csv_line_values)
    return response