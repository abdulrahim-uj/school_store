from django.contrib import admin
from .models import Department, Course, MaterialsChoices, Suggestion


class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('department_name',)}
    list_display = ('id', 'auto_id', 'department_name', 'slug', 'wiki', 'description', 'is_visible', 'creator',
                    'updater', 'date_added', 'date_updated', 'is_deleted')
    ordering = ('-date_added',)
    list_editable = ('wiki', 'is_visible',)
    list_per_page = 10
    search_fields = ('department_name', 'slug')
    list_filter = ('is_visible',)
    list_display_links = ('department_name',)


admin.site.register(Department, DepartmentAdmin)


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('course_name',)}
    list_display = ('id', 'auto_id', 'department', 'course_name', 'slug', 'fees', 'duration', 'creator',
                    'updater', 'date_added', 'date_updated', 'is_deleted')
    ordering = ('-date_added',)
    list_editable = ('fees', 'duration',)
    list_per_page = 10
    search_fields = ('department__department_name', 'course_name', 'slug')
    list_filter = ('is_deleted',)
    list_display_links = ('course_name',)


admin.site.register(Course, CourseAdmin)


class MaterialsChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'materials')
    ordering = ('-id',)
    list_per_page = 10
    search_fields = ('materials',)
    list_display_links = ('materials',)


admin.site.register(MaterialsChoices, MaterialsChoiceAdmin)


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'auto_id', 'name', 'dob', 'age', 'gender', 'phone', 'email', 'address', 'department',
                    'course', 'purpose', 'creator', 'updater', 'date_added', 'date_updated', 'is_deleted')
    ordering = ('-date_added',)
    list_per_page = 10
    search_fields = ('department__department_name', 'course__course_name', 'purpose')
    list_filter = ('is_deleted',)
    list_display_links = ('name',)


admin.site.register(Suggestion, SuggestionAdmin)
