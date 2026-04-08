# 🏋️ Fitness Tracker

A full-stack web application built with **Python Django** that allows users to log, track, and manage their workout sessions. Deployed live on PythonAnywhere.

🌐 **Live Demo:** [sanjayn.pythonanywhere.com](https://sanjayn.pythonanywhere.com)

---

## 📸 Screenshots

| Workout List | Log a Workout |
|---|---|
| View all your logged workouts | Add new workout entries |

---

## ✨ Features

- 📝 **Log Workouts** — Add activity name, duration, and date
- 📋 **View All Workouts** — See all your workouts sorted by most recent
- 🛡️ **Admin Panel** — Manage all data via Django's built-in admin dashboard
- 📱 **Mobile Friendly** — Works on any device — mobile, tablet, or desktop
- ✅ **Form Validation** — Instant error messages for invalid inputs

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.13** | Programming Language |
| **Django 4.2** | Web Framework |
| **SQLite** | Database |
| **HTML & CSS** | Frontend Templates |
| **PythonAnywhere** | Deployment & Hosting |

---

## 📁 Project Structure

```
fitness_tracker/
│
├── fitness_project/          # Main Django project folder
│   ├── settings.py           # Project settings and configuration
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI entry point for deployment
│
├── tracker/                  # Django app for workout tracking
│   ├── migrations/           # Database migration files
│   ├── templates/tracker/    # HTML templates
│   │   ├── workout_list.html # Page to view all workouts
│   │   └── add_workout.html  # Page to log a new workout
│   ├── admin.py              # Admin panel configuration
│   ├── forms.py              # Django ModelForm for workouts
│   ├── models.py             # Workout database model
│   ├── urls.py               # App-level URL patterns
│   └── views.py              # View functions (logic)
│
├── staticfiles/              # Collected static files for production
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management utility
└── requirements.txt          # Python dependencies
```

---

## ⚙️ Local Setup Instructions

Follow these steps to run the project on your own machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Sanjay284-beep/fitness-tracker.git
cd fitness-tracker
```

### 2. Create and Activate Virtual Environment
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Create Admin Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and visit: **http://127.0.0.1:8000/**

---

## 🚀 Deployment

This project is deployed on **PythonAnywhere** (free tier).

Key deployment steps:
- Uploaded project files and set up virtual environment on PythonAnywhere
- Configured WSGI file to point to Django settings
- Set `ALLOWED_HOSTS` and `STATIC_ROOT` in `settings.py`
- Ran `collectstatic` to serve static files
- Configured Web App settings on PythonAnywhere dashboard

---

## 📌 How It Works

```
User visits URL
      ↓
Django checks urls.py
      ↓
Matching view function runs
      ↓
View queries the database
      ↓
Data is passed to HTML template
      ↓
Rendered page shown to user
```

---

## 🔮 Future Improvements

- [ ] User Authentication (Login / Register)
- [ ] Edit and Delete workouts
- [ ] Workout Categories (Cardio, Strength, Flexibility)
- [ ] Progress Charts using Chart.js
- [ ] REST API with Django REST Framework

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Sanjay N**
- GitHub: [@Sanjay284-beep](https://github.com/Sanjay284-beep)
- Live App: [sanjayn.pythonanywhere.com](https://sanjayn.pythonanywhere.com)

---

> Built with ❤️ while learning Django — from zero to deployed! 🚀
