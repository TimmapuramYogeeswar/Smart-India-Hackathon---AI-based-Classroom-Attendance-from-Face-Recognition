# Smart-India-Hackathon---AI-based-Classroom-Attendance-from-Face-Recognition
# ClassTrack — AI-Based Classroom Attendance

## Important scope
This educational project demonstrates **face detection plus teacher verification**. The computer-vision component detects faces in a classroom image but does not identify people by biometric identity. The teacher remains responsible for the final Present/Absent decision.

## Features
- Student registration
- SQLite database
- Classroom-photo face detection using OpenCV
- Teacher dashboard
- Present/Absent correction
- Attendance history by date
- CSV export
- Responsive interface
- Sample seed data

## Setup

### 1. Create a virtual environment
```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add sample students
```bash
python seed.py
```

### 4. Run
```bash
python app.py
```

Open `http://127.0.0.1:5000`.

## Demo flow
1. Open Students and show registration.
2. Open Detection and upload a classroom photo.
3. Show detected-face count.
4. Return to Dashboard.
5. Change Present/Absent status for sample students and save.
6. Select a date and show the attendance summary.
7. Export CSV.

## Architecture
Browser → Flask routes → OpenCV face detection / SQLite → Dashboard → CSV export.

## Evaluation
For a report, evaluate the face detector separately using a labelled set of classroom images. Recommended metrics:
- Face detection precision
- Face detection recall
- F1 score
- False positives / false negatives
- Runtime per image

Do not describe detection accuracy as student-identification accuracy; this implementation does not perform identity recognition.

## Output

<img width="1917" height="837" alt="image" src="https://github.com/user-attachments/assets/e74548b8-44a0-4414-a4aa-9b2844902bba" />
