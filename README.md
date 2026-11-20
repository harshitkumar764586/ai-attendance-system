# 🎓 SnapClass - Intelligent AI Attendance System (Face & Voice)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-FF4B4B?logo=streamlit)
![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?logo=supabase)
![AI/ML](https://img.shields.io/badge/ML-dlib%20%7C%20scikit--learn-orange)

> **SnapClass** is a modern, AI-powered attendance management web application that eliminates manual roll calls using facial recognition and voice identification pipelines. Built with Streamlit, Supabase, dlib, and Scikit-Learn.

---

## 🌟 Key Features

* **Dual-Portal Architecture:**
  * **Teacher Portal:** Create & manage courses, review attendance logs, generate instant QR codes for student onboarding, and conduct live AI attendance sessions.
  * **Student Portal:** Seamless FaceID login, self-enrollment into subjects via codes/QR links, and personal attendance statistics tracking.
* **Biometric AI Pipelines:**
  * **Facial Recognition (dlib + 128-d ResNet Embeddings):** Deep metric face recognition with Euclidean nearest-neighbor distance matching.
  * **Classroom Multi-Face Scanning:** Upload or snapshot full classroom photos; the AI detects and identifies all enrolled students in a single pass.
  * **Voice Attendance (Optional Pipeline):** Speaker identification from recorded audio utterances.
* **Instant Onboarding:**
  * Quick Subject Enrollment via scannable QR Codes (`segno`) and auto-enrolment query parameter links (`?join-code=<subject_code>`).
* **Cloud Database & Security:**
  * Relational database tables hosted on Supabase (PostgreSQL).
  * Secure password hashing with `bcrypt`.

---

## 🛠️ Tech Stack

* **Frontend & Core App:** [Streamlit](https://streamlit.io/) (with custom CSS style overrides and stateful multi-screen routing)
* **Database & Cloud:** [Supabase](https://supabase.com/) (PostgreSQL)
* **Authentication Security:** `bcrypt`
* **Machine Learning & Image Processing:**
  * `dlib-bin` (Facial shape predictor & ResNet recognition model)
  * `face_recognition_models` (Pretrained landmark & 128-d metric weights)
  * `scikit-learn` (Support Vector Classifier / Euclidean nearest neighbor)
  * `numpy` & `pandas` (Vector mathematics & tabular reporting)
  * `Pillow` (PIL) (Image decoding and RGB sanitation)
* **QR Code Engine:** `segno`

---

## 📂 Project Structure

```text
SNAPCLASS/
├── app.py                      # Main Streamlit router & entrypoint
├── requirements.txt            # Python dependencies
├── view_db.py                  # Terminal database viewer utility
├── .gitignore                  # Git ignore rules (protects credentials & venv)
└── src/
    ├── components/             # Reusable UI & modal dialogs
    │   ├── header.py           # Brand header
    │   ├── footer.py           # Brand footer
    │   ├── subject_card.py     # Course cards with stats
    │   ├── dialog_add_photo.py # Camera / photo upload dialog
    │   ├── dialog_attendance_results.py # Attendance review modal
    │   ├── dialog_auto_enroll.py # QR code 1-click enrollment
    │   ├── dialog_create_subject.py
    │   ├── dialog_enroll.py    # Manual subject code enrollment
    │   ├── dialog_share_subject.py # QR code generator
    │   └── dialog_voice_attendance.py
    ├── database/
    │   ├── config.py           # Supabase client proxy
    │   └── db.py               # Database CRUD queries & bcrypt auth
    ├── pipelines/
    │   ├── face_pipeline.py    # dlib face detection & descriptor matching
    │   └── voice_pipeline.py   # Speaker identification logic
    ├── screens/
    │   ├── home_screen.py      # Teacher vs Student portal landing
    │   ├── teacher_screen.py   # Teacher auth, dashboard & attendance flow
    │   └── student_screen.py   # FaceID login, student registration & dashboard
    └── ui/
        └── base_layout.py      # Custom CSS styling, Google fonts & theme
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/harshitkumar764586/ai-attendance-system.git
cd ai-attendance-system
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Supabase Credentials
Create a `.streamlit/secrets.toml` file in the project root:
```toml
SUPABASE_URL = "https://your-project-id.supabase.co"
SUPABASE_KEY = "your-anon-public-key"
```

### 5. Launch Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 👤 Author

* **Harshit Kumar** - [GitHub Profile](https://github.com/harshitkumar764586)
