from django.contrib import admin
from .models import (
    AcademicYear, Semester, SchoolLevel, Department,
    Course, Subject, Student, Enrollment
)

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('acad_year', 'term')
    list_filter = ('acad_year', 'term')
    search_fields = ('acad_year__name', 'term')
    autocomplete_fields = ['acad_year']

@admin.register(SchoolLevel)
class SchoolLevelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'school_level')
    list_filter = ('school_level',)
    search_fields = ('name',)
    autocomplete_fields = ['school_level']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department__school_level', 'department')
    search_fields = ('name', 'department__name')
    autocomplete_fields = ['department']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'course')
    list_filter = ('course__department', 'course')
    search_fields = ('name', 'code', 'course__name')
    autocomplete_fields = ['course']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'last_name', 'first_name', 'gender')
    list_filter = ('gender', 'date_joined')
    search_fields = ('student_id', 'last_name', 'first_name')
    ordering = ('last_name', 'first_name')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'year_level', 'status')
    list_filter = ('semester', 'course', 'status', 'year_level')
    search_fields = ('student__last_name', 'student__student_id', 'course__name')
    autocomplete_fields = ['student', 'semester', 'course']
