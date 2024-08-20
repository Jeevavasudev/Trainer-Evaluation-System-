from django.contrib import admin
from .models import FeedbackDetails, Trainer,Course,Student,Feedback

# Register your models here.
class MasterAdmin(admin.ModelAdmin):

    # in order to exclude the field 'created_user' from the form
    exclude = ['created_user']

    list_per_page = 10
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    # To order Active field last in all forms
    def get_fields(self, request, obj=None, **kwargs):
        fields = super().get_fields(request, obj, **kwargs)
        fields.remove('isactive')
        fields.append('isactive')  # can also use insert
        return fields
    def save_model(self, request, obj, form, change):
        obj.created_user = request.user
        #print(eval(self._class.name_))
        super().save_model(request, obj, form, change)

class TrainerAdmin(MasterAdmin):
    ordering=['trainer_name']
    search_fields=['name']


class CourseAdmin(MasterAdmin):
    ordering =['course_name']
    search_fields=['course_name']



class FeedbackDetailsAdmin(MasterAdmin):
    autocomplete_fields=['trainer_name']
    ordering=('date_submitted',)
class FeedbackAdmin(MasterAdmin):
    list_display=['coments','rating','date']

class StudentAdmin(MasterAdmin):
    list_display=['id','student_name','course_name']
    ordering=['student_name']
    search_fields=['name']





admin.site.register(Trainer,TrainerAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(FeedbackDetails,FeedbackDetailsAdmin)
admin.site.register(Feedback,FeedbackAdmin)