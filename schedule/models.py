from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class DayOff(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="day_offs")

    class Meta:
        unique_together = ("date", "employee")
        ordering = ("date",)

    def __str__(self):
        return f"{self.date} - self.{self.employee.first_name} + {self.employee.last_name}"

