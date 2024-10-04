from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=20)
    loc = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.deptno)
class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    job = models.CharField(max_length=30)
    Hiredate = models.DateField()
    mgr = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL)
    sal = models.DecimalField(max_digits=10,decimal_places=2)
    comm = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno = models.ForeignKey(Dept,on_delete=models.CASCADE)
    