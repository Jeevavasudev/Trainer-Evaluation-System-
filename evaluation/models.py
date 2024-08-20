from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here


class Master(models.Model):
    #created_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True,verbose_name="Active")
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        abstract = True
        ordering = ['-isactive']

    

class Trainer(Master):
    trainer_name=models.CharField(max_length=50,default='')
    course_name=models.ForeignKey('Course',on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return str(self.trainer_name)
    
class Course(Master):
    course_name=models.CharField(max_length=220)
    
    
    def __str__(self):
        return str(self.course_name)
    

class Student(Master):
    student_name=models.CharField(max_length=220)
    course_name=models.ForeignKey('Course',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.student_name
    


class Feedback(Master):
    coments=models.TextField()
    rating=models.IntegerField()
    date=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.student_name
    

class FeedbackDetails(Master):

    CHOICES = (
        ('Strongly Disagree', 'Strongly Disagree'),
        ('Disagree', 'Disagree'),
        ('Sometimes', 'Sometimes'),
        ('Agree', 'Agree'),
        ('Strongly Agree', 'Strongly Agree'),
    )

    date_submitted = models.DateTimeField(auto_now=True)

    trainer_name = models.ForeignKey(Trainer, verbose_name='Name of Teacher',
                                     on_delete=models.CASCADE)
    
    course_name=models.ForeignKey(Course,verbose_name='COURSE NAME',on_delete=models.CASCADE,null=True,blank=True)

    punctuality = models.CharField(verbose_name='The teacher is punctual in coming to class',
                                   max_length=225,
                                   choices=CHOICES)

    portion = models.CharField(verbose_name='The teacher completes portions at the appropriate time',
                               max_length=225,
                               choices=CHOICES)

    doubt = models.CharField(verbose_name='The teacher takes in effort to clear your doubts',
                             max_length=225,
                             choices=CHOICES)

    interactive = models.CharField(verbose_name='The teacher makes the class interactive',
                                   max_length=225,
                                   choices=CHOICES)

    comments = models.TextField(verbose_name='Any other feedback (your comments)',
                                blank=True)
    student=models.ForeignKey(Student, verbose_name='Name of Student',
                                     on_delete=models.CASCADE,default=None)

    class Meta:
        verbose_name = 'Feedback Data'
        verbose_name_plural = 'Feedback Data'
        get_latest_by='date_submitted'
        

    def __str__(self):
        return str(self.trainer_name)
    

