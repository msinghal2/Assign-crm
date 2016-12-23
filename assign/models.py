from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class EmployeeInfo(models.Model):
    employeeName = models.CharField(max_length=50)
    # address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    # photo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('assign:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.employeeName  # + ' - ' + self.email


class Assignment(models.Model):
    # empname = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE)
    assignee = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE)
    assignor = models.CharField(max_length=50)
    # assignor = models.ForeignKey(Delegation, on_delete=models.SET('admin'))
    abuilding = models.CharField(max_length=10)
    afloor = models.CharField(max_length=10)
    aroom = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('assign:assigndetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.abuilding + '-' + self.aroom


class Delegation(models.Model):
    delegator = models.CharField(max_length=50)
    delegated = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE)
    dbuilding = models.CharField(max_length=10, default='all')
    dfloor = models.CharField(max_length=10, default='all')
    dwing = models.CharField(max_length=10, default='all')

    def get_absolute_url(self):
        return reverse('assign:delegdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.dbuilding + '-' + self.dfloor + '-' + self.dwing