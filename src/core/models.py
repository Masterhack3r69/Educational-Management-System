from django.db import models
from django.utils.translation import gettext_lazy as _

class SchoolLevel(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="e.g. Elementary, High School, College")

    def __str__(self):
        return self.name

class AcademicYear(models.Model):
    name = models.CharField(max_length=20, unique=True, help_text="e.g. 2025-2026")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Semester(models.Model):
    acad_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='semesters')
    term = models.CharField(max_length=20, help_text="e.g. 1st Semester, 2nd Semester, Summer")
    
    class Meta:
        unique_together = ('acad_year', 'term')

    def __str__(self):
        return f"{self.acad_year} - {self.term}"

class Department(models.Model):
    school_level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=100, unique=True, help_text="e.g. ICT Dept, General")

    def __str__(self):
        return f"{self.name} ({self.school_level})"

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100, help_text="e.g. BSCS, Grade 10")
    
    class Meta:
        unique_together = ('department', 'name')

    def __str__(self):
        return self.name

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100, help_text="e.g. Algebra, World History")
    code = models.CharField(max_length=20, blank=True, null=True, help_text="Optional subject code")

    def __str__(self):
        return f"{self.name} ({self.course})"

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    CIVIL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
    ]

    NATIONALITY_CHOICES = [
        ('Filipino', 'Filipino'),
        ('American', 'American'),
        ('British', 'British'),
        ('Canadian', 'Canadian'),
        ('Chinese', 'Chinese'),
        ('Indian', 'Indian'),
        ('Japanese', 'Japanese'),
        ('Korean', 'Korean'),
        ('Australian', 'Australian'),
        ('Singaporean', 'Singaporean'),
        ('Other', 'Other'),
    ]

    RELIGION_CHOICES = [
        ('Roman Catholic', 'Roman Catholic'),
        ('Islam', 'Islam'),
        ('Evangelical', 'Evangelical'),
        ('Iglesia ni Cristo', 'Iglesia ni Cristo'),
        ('Protestant', 'Protestant'),
        ('Buddhist', 'Buddhist'),
        ('Hindu', 'Hindu'),
        ('Seventh Day Adventist', 'Seventh Day Adventist'),
        ('Aglipay', 'Aglipay'),
        ('Other', 'Other'),
        ('None', 'None'),
    ]

    student_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    civil_status = models.CharField(max_length=20, choices=CIVIL_STATUS_CHOICES, default='Single')
    birth_place = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, blank=True, null=True)
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES, blank=True, null=True)
    
    email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    
    permanent_address = models.CharField(max_length=255, blank=True, null=True)
    current_address = models.CharField(max_length=255, blank=True, null=True)
    
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Educational Background
    elem_school_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Elementary School")
    elem_year_graduated = models.PositiveIntegerField(blank=True, null=True, verbose_name="Year Graduated")
    
    secondary_school_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Secondary School")
    secondary_year_graduated = models.PositiveIntegerField(blank=True, null=True, verbose_name="Year Graduated")
    
    college_school_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="College/University")
    college_year_graduated = models.PositiveIntegerField(blank=True, null=True, verbose_name="Year Graduated")
    college_course = models.CharField(max_length=100, blank=True, null=True, verbose_name="Course/Degree")
    
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.student_id})"

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('ENROLLED', 'Enrolled'),
        ('DROPPED', 'Dropped'),
        ('GRADUATED', 'Graduated'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    year_level = models.CharField(max_length=50, help_text="e.g. Grade 1, 1st Year College")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ENROLLED')
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'semester')
        ordering = ['-date_enrolled']

    def __str__(self):
        return f"{self.student} - {self.semester} ({self.status})"

class EnrolledSubject(models.Model):
    STATUS_CHOICES = [
        ('ONGOING', 'Ongoing'),
        ('PASSED', 'Passed'),
        ('FAILED', 'Failed'),
        ('DROPPED', 'Dropped'),
    ]

    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='enrolled_students')
    grade = models.CharField(max_length=5, blank=True, null=True, help_text="e.g. 1.0, 95, A")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ONGOING')
    
    class Meta:
        unique_together = ('enrollment', 'subject')

    def __str__(self):
        return f"{self.subject} ({self.grade})"
