from django.db import models
class Student(models.Model):
    reg_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Std_mrk(models.Model):
    mark_id=models.OneToOneField(Student, on_delete=models.CASCADE,primary_key=True)
    mark=models.IntegerField(default=0)
