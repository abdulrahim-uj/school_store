from datetime import date

from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Department(BaseModel):
    department_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    wiki = models.CharField(max_length=128)
    description = models.TextField(max_length=256, blank=True)
    is_visible = models.BooleanField(default=False)

    class Meta:
        db_table = "submissions_department"
        verbose_name = _('department')
        verbose_name_plural = _('departments')

    def __str__(self):
        return self.department_name


class Course(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    fees = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        db_table = "submissions_course"
        verbose_name = _('course')
        verbose_name_plural = _('courses')

    def __str__(self):
        return self.course_name


class MaterialsChoices(models.Model):
    materials = models.CharField(max_length=128)

    class Meta:
        db_table = "submissions_materialschoices"
        verbose_name = _('materialschoice')
        verbose_name_plural = _('materialschoices')

    def __str__(self):
        return self.materials


class Suggestion(BaseModel):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

    GENDER_CHOICE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    )

    PURPOSES_CHOICE = (
        ('request', 'REQUEST'),
        ('enquiry', 'ENQUIRY'),
        ('order', 'ORDER'),
        ('return', 'RETURN')
    )

    name = models.CharField(max_length=128)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.TextField(max_length=128)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(choices=PURPOSES_CHOICE, default='enquiry',  max_length=7)
    materials = models.ManyToManyField(MaterialsChoices)

    class Meta:
        db_table = "submissions_suggestion"
        verbose_name = _('suggestion')
        verbose_name_plural = _('suggestions')

    def __str__(self):
        return self.purpose
