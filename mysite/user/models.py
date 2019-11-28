from django.db import models


class UserDetail(models.Model):
    Name= models.CharField(max_length=50)
    Address=models.CharField(max_length=60)
    Phone= models.IntegerField()

    def __str__(self):
        return self.Name


class UserPersonal(models.Model):
    Id= models.ForeignKey(UserDetail,on_delete=models.DO_NOTHING)
    Blog= models.TextField(max_length=1000)

    def __str__(self):
        return self.Blog


class ExtraInfo(models.Model):
    Relationof = models.ForeignKey(UserDetail,on_delete=models.DO_NOTHING)
    FatherName = models.CharField(max_length=50)
    Citizenship= models.IntegerField()

    def __str__(self):
        return self.FatherName





