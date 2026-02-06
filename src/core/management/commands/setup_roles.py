from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from src.core.models import (
    AcademicYear, Semester, SchoolLevel, Department,
    Course, Subject, Student, Enrollment
)

class Command(BaseCommand):
    help = 'Setup default RBAC groups: Registrar and Academic Head'

    def handle(self, *args, **kwargs):
        # 1. Registrar: Can manage Students and Enrollments
        registrar_group, created = Group.objects.get_or_create(name='Registrar')
        registrar_models = [Student, Enrollment]
        self.assign_permissions(registrar_group, registrar_models)
        self.stdout.write(self.style.SUCCESS('Successfully configured "Registrar" group'))

        # 2. Academic Head: Can manage Curriculum (AcademicYear, Semester, SchoolLevel, Dept, Course, Subject)
        head_group, created = Group.objects.get_or_create(name='Academic Head')
        head_models = [AcademicYear, Semester, SchoolLevel, Department, Course, Subject]
        self.assign_permissions(head_group, head_models)
        self.stdout.write(self.style.SUCCESS('Successfully configured "Academic Head" group'))

    def assign_permissions(self, group, models):
        permissions = []
        for model in models:
            content_type = ContentType.objects.get_for_model(model)
            # Get all permissions for this model (add, change, delete, view)
            model_perms = Permission.objects.filter(content_type=content_type)
            permissions.extend(model_perms)
        
        group.permissions.set(permissions)
        group.save()
