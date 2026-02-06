from django import forms
from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline as UnfoldTabularInline
from .models import (
    AcademicYear, Semester, SchoolLevel, Department,
    Course, Subject, Student, Enrollment, EnrolledSubject
)

# Unregister default User/Group to use Unfold
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, UnfoldModelAdmin):
    icon = "people"

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, UnfoldModelAdmin):
    icon = "groups"

@admin.register(AcademicYear)
class AcademicYearAdmin(UnfoldModelAdmin):
    icon = "calendar_today"
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(Semester)
class SemesterAdmin(UnfoldModelAdmin):
    icon = "date_range"
    list_display = ('acad_year', 'term')
    list_filter = ('acad_year', 'term')
    search_fields = ('acad_year__name', 'term')
    autocomplete_fields = ['acad_year']

@admin.register(SchoolLevel)
class SchoolLevelAdmin(UnfoldModelAdmin):
    icon = "stairs"
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Department)
class DepartmentAdmin(UnfoldModelAdmin):
    icon = "domain"
    list_display = ('name', 'school_level')
    list_filter = ('school_level',)
    search_fields = ('name',)
    autocomplete_fields = ['school_level']

@admin.register(Course)
class CourseAdmin(UnfoldModelAdmin):
    icon = "school"
    list_display = ('name', 'department')
    list_filter = ('department__school_level', 'department')
    search_fields = ('name', 'department__name')
    autocomplete_fields = ['department']

@admin.register(Subject)
class SubjectAdmin(UnfoldModelAdmin):
    icon = "menu_book"
    list_display = ('name', 'code', 'course')
    list_filter = ('course__department', 'course')
    search_fields = ('name', 'code', 'course__name')
    autocomplete_fields = ['course']

@admin.register(Student)
class StudentAdmin(UnfoldModelAdmin):
    icon = "person"
    list_display = ('student_id', 'last_name', 'first_name', 'year_level_display', 'gender', 'civil_status', 'contact_number')
    list_filter = ('gender', 'civil_status', 'date_joined')
    search_fields = ('student_id', 'last_name', 'first_name', 'email', 'contact_number')
    ordering = ('last_name', 'first_name')


    fieldsets = (
        ("Personal Information", {
            "fields": (
                ("student_id", "first_name", "middle_name", "last_name"),
                ("birthdate", "birth_place", "religion"),
                ("gender", "civil_status", "nationality"),
                ("permanent_address", "current_address"),
            ),
        }),
        ("Contact Details", {
            "fields": (
                ("email", "contact_number", "emergency_contact_name", "emergency_contact_number"),
            ),
        }),
        ("Educational Background", {
            "fields": (
                ("elem_school_name", "elem_year_graduated"),
                ("secondary_school_name", "secondary_year_graduated"),
                ("college_school_name", "college_year_graduated", "college_course"),
            ),
        }),
    )


    def year_level_display(self, obj):
        # Allow column sorting by getting the latest enrollment
        latest_enrollment = obj.enrollments.first()  # Relies on Meta ordering=['-date_enrolled']
        return latest_enrollment.year_level if latest_enrollment else "-"
    year_level_display.short_description = "Current Year Level"

class EnrolledSubjectInline(UnfoldTabularInline):
    model = EnrolledSubject
    extra = 1
    tab = True
    autocomplete_fields = ['subject']

@admin.register(Enrollment)
class EnrollmentAdmin(UnfoldModelAdmin):
    icon = "how_to_reg"
    list_display = ('student', 'course', 'semester', 'year_level', 'status')
    list_filter = ('semester', 'course', 'status', 'year_level')
    search_fields = ('student__last_name', 'student__student_id', 'course__name')
    autocomplete_fields = ['student', 'semester', 'course']
    inlines = [EnrolledSubjectInline]
