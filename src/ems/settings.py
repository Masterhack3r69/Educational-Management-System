import os
from pathlib import Path
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'insecure-key-for-dev')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'unfold.contrib.import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'src.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.ems.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.ems.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'ems'),
        'USER': os.environ.get('DB_USER', 'ems_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'ems_password'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

UNFOLD = {
    "SITE_TITLE": "EMS Administration",
    "SITE_HEADER": "EMS Dashboard",
    "SITE_URL": "/",
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": "Navigation",
                "separator": True,
                "items": [
                    {
                        "title": "Dashboard",
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                ],
            },
            {
                "title": "Student Management",
                "separator": True,
                "items": [
                    {
                        "title": "Students",
                        "icon": "person",
                        "link": reverse_lazy("admin:core_student_changelist"),
                    },
                    {
                        "title": "Enrollments",
                        "icon": "how_to_reg",
                        "link": reverse_lazy("admin:core_enrollment_changelist"),
                    },
                ],
            },
            {
                "title": "Academics",
                "separator": True,
                "items": [
                    {
                        "title": "Courses",
                        "icon": "school",
                        "link": reverse_lazy("admin:core_course_changelist"),
                    },
                     {
                        "title": "Subjects",
                        "icon": "menu_book",
                        "link": reverse_lazy("admin:core_subject_changelist"),
                    },
                     {
                        "title": "Departments",
                        "icon": "domain",
                        "link": reverse_lazy("admin:core_department_changelist"),
                    },
                ],
            },
               {
                "title": "Configuration",
                "separator": True,
                "items": [
                    {
                        "title": "Academic Years",
                        "icon": "calendar_today",
                        "link": reverse_lazy("admin:core_academicyear_changelist"),
                    },
                     {
                        "title": "Semesters",
                        "icon": "date_range",
                        "link": reverse_lazy("admin:core_semester_changelist"),
                    },
                     {
                        "title": "School Levels",
                        "icon": "stairs",
                        "link": reverse_lazy("admin:core_schoollevel_changelist"),
                    },
                ],
            },
             {
                "title": "Users & Groups",
                "separator": True,
                "items": [
                    {
                        "title": "Users",
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": "Groups",
                        "icon": "groups",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}
