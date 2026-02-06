# Educational Management System (EMS)

A local-first, Admin-centric Educational Management System built with **Django 5** and **Docker**. designed for simplicity and efficiency.

## Quick Start

### Prerequisites

- Docker & Docker Compose

### Running the App

1.  **Start the services**:
    ```bash
    docker-compose up --build
    ```
2.  **Access the Dashboard**:
    Open [http://localhost:8000/admin](http://localhost:8000/admin)

3.  **Create a Superuser** (First time only):
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

## Key Features

### v1.0 Modernization (Current)

- **Modern UI**: Fully themed with Tailwind CSS (`django-unfold`), featuring Dark Mode and a responsive layout.
- **Grading System**: Track individual subject grades (`1.0`, `95`), status (`Passed`, `Failed`), and subject-specific remarks.
- **Smart Navigation**: Organized sidebar with intuitive grouping (Academics, Students, Configuration) and icons.
- **In-line Management**: Add subjects and grades directly from the Student Enrollment screen.

### v0 Core (Foundation)

- **Academic Structure**: manage Years, Semesters, Departments, Courses, and Subjects.
- **Student Management**: Profile tracking with history-safe Enrollment snapshots.
- **RBAC**: Pre-configured roles for **Registrars** (Student/Enrollment focus) and **Academic Heads** (Curriculum focus).
- **Local-First**: Zero-dependency setup via Docker.

## Documentation

- [v1 Features (Grading & UI)](docs/features_v1.md)
- [v0 Features (Core Architecture)](docs/features_v0.md)

## Technology Stack

- **Backend**: Python, Django 5.x
- **Database**: PostgreSQL 16
- **Containerization**: Docker Compose
- **Interface**: Django Admin + Unfold Theme
