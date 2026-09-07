# Project Report
## AI-Based Classroom Attendance from Face Detection and Teacher Verification

### 1. Problem Statement
Manual classroom attendance consumes teaching time and can be error-prone. This project provides a web-based workflow that uses computer vision to detect faces in classroom photographs and gives teachers a structured dashboard for verifying and recording attendance.

### 2. Objectives
- Reduce repetitive attendance-entry work.
- Provide a centralized student roster.
- Detect visible faces in classroom images.
- Allow teachers to verify and correct attendance.
- Store attendance records reliably.
- Export records as CSV.

### 3. System Architecture
The system contains a browser-based teacher interface, a Flask backend, an OpenCV detection service, and an SQLite database. Uploaded images are processed by the detection module, while final attendance is entered or verified by the teacher.

### 4. Dataset
For evaluation, use classroom photographs for which the number and approximate location of visible faces can be manually annotated. Split the dataset into training/development and test subsets if experimenting with detector parameters. Record image resolution, number of annotated faces, lighting conditions, occlusion, and crowd density.

### 5. Results
Report detection precision, recall, F1 score, and average processing time. Example table format:

| Metric | Result |
|---|---:|
| Precision | [fill from test] |
| Recall | [fill from test] |
| F1 Score | [fill from test] |
| Average image processing time | [fill from test] |

### 6. Limitations
Face detection can fail under occlusion, poor lighting, unusual camera angles, small faces, or heavy crowding. Detection of a face also does not establish a person's identity. Therefore, this prototype keeps the teacher in the verification loop.

### 7. Future Scope
Future work can investigate institution-approved, privacy-preserving attendance mechanisms, stronger face-detection models, liveness checks, better classroom-camera positioning, role-based access, audit logs, and deployment on a secured institutional network.

### 8. Conclusion
The prototype demonstrates an end-to-end attendance workflow: student registration, classroom face detection, teacher verification, database storage, dashboard review, and CSV export.
