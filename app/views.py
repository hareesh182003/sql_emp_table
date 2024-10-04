from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_dept(request):
    deptno_r = int(input('Enter the deptno: '))
    dname_r = input('Enter the deptname: ')
    loc_r = input('Enter the location: ')

    do = Dept.objects.get_or_create(deptno = deptno_r,dname = dname_r,loc = loc_r)
    do = Dept.objects.all()
    d = {'department': do}
    return render(request,'insert_dept.html',d)

def insert_emp(request):
    empno_r = int(input("enter the empno: "))
    ename_r = input('enter the ename: ')
    job_r = input('enter the job: ')
    hiredate_r = input('Enter the hiredate: ')
    sal_r = float(input('Enter the sal(decimal): '))
    comm_r = input('enter the commision(decimal): ')
    mgr = input("Enter the mgr: ")
    deptno_r = int(input('enter the deptno: '))
    mgrval = None
    deptob = Dept.objects.filter(deptno = deptno_r)
    if not mgr:
        mgrval = None
        empob = Emp.objects.get_or_create(empno = empno_r,ename = ename_r,job = job_r,Hiredate = hiredate_r,
                                      sal = sal_r,comm = comm_r,mgr = None,deptno = deptob[0])
    else:
        mgrval = Emp.objects.filter(empno = mgr)
        empob = Emp.objects.get_or_create(empno = empno_r,ename = ename_r,job = job_r,Hiredate = hiredate_r,
                                      sal = sal_r,comm = comm_r,mgr = mgrval[0],deptno = deptob[0])
    
    d = {'employee' : Emp.objects.all()}
    return render(request,'insert_emp.html',d)

    