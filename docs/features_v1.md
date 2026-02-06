# EMS v1 - Modernization & Grading Update

## 1. Grade Management System

v1 introduces granular tracking of academic consistency.

- **Enrolled Subjects**: Instead of just enrolling in a "Course", students now have records for specific subjects within that enrollment.
- **Grades & Status**:
  - Track individual grades (e.g., "1.0", "95").
  - Subject-specific status: `Ongoing`, `Passed`, `Failed`, `Dropped`.
- **Inline Editing**: registrars can add/remove subjects and input grades directly from the main Enrollment screen.

## 2. Modern UI/UX Overhaul

Completely replaced the default Django Admin interface with a tailored **Tailwind CSS** theme (`django-unfold`).

- **Visuals**: Clean, modern typography and whitespace.
- **Dark Mode**: Fully supported out-of-the-box.
- **Responsive**: Better mobile and tablet experience for administrators on-the-go.

## 3. Enhanced Navigation

- **Sidebar Groups**: Models are logically organized into sections:
  - _Student Management_ (Students, Enrollments)
  - _Academics_ (Courses, Subjects, Departments)
  - _Configuration_ (Semesters, School Levels)
- **Visual Cues**: Material Symbols (Icons) added to every model for instant recognition.
- **Global Search**: "Command Palette" style search bar available in the sidebar.

## 4. Admin Customization

- **Compact Forms**: Optimized layout density to show more data with less scrolling.
- **Tabbed Inlines**: Enrolled subjects are presented in a clean, tabbed interface to avoid cluttering the main enrollment details.
