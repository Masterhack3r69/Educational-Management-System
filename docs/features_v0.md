# EMS v0 - Current Feature Set

## 1. Core Architecture

- **Framework**: Django 5.x (Latest stable)
- **Database**: PostgreSQL 16
- **Deployment**: Docker Compose (One-command setup)
- **Interface**: Native Django Admin (No custom frontend)

## 2. Academic Structure Management

The system enforces a strict hierarchy to ensure data integrity:

- **Academic Years**: Manages school years (e.g., "2025-2026").
- **Semesters**: Links specifically to an Academic Year (e.g., "1st Sem 2025-2026").
- **School Levels**: Categories like "Elementary", "High School", "College".
- **Departments**: Linked to School Levels (e.g., "ICT Dept" is under "College").
- **Courses**: The specific degree/program (e.g., "BSCS").
- **Subjects**: The individual classes (e.g., "Intro to Programming").

## 3. Student & Enrollment Management

- **Student Profiles**: Stores unique ID, name, gender, birthdate, and address.
- **Enrollment History**:
  - **Logic**: Uses a "Snapshot" approach. Every semester a student enrolls, a _new_ record is created.
  - **Fields**: Tracks `Student` + `Semester` + `Course` + `Year Level` + `Status`.
  - **Benefits**: Allows a student to change courses or status (e.g., Dropped, Graduated) without losing past history.

## 4. Security & Access Control (RBAC)

Two pre-configured Roles (Groups) restrict access:

- **Registrar**:
  - **Can View/Edit**: Users, Students, Enrollments.
  - **Cannot Edit**: Courses, Subjects, Academic Years (Curriculum).
- **Academic Head**:
  - **Can View/Edit**: Curriculum (Courses, Subjects, etc.).
  - **Cannot Edit**: Sensitive Student data.

## 5. Developer Experience

- **Local-First**: Complete `docker-compose.yml` included.
- **Auto-Setup**: Helper scripts (`setup_roles`) to initialize permissions instantly.
- **Searchable Admin**: All models have `search_fields` and `list_filters` pre-configured for quick data lookup.
