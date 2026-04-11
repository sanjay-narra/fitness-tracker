# 🏋️ FitTrack — Personal Fitness Tracker Web Application

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.x-red?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge&logo=sqlite)
![Deployed](https://img.shields.io/badge/Deployed-PythonAnywhere-yellow?style=for-the-badge)

> A full-stack fitness tracking web application built with Python Django — featuring user authentication, workout management, category filtering, interactive charts, and a REST API.

🌐 **Live Demo:** [sanjayn.pythonanywhere.com](https://sanjayn.pythonanywhere.com)  
📂 **GitHub:** [github.com/Sanjay284-beep/fitness-tracker](https://github.com/Sanjay284-beep/fitness-tracker)

---

## ✨ Features

### 🔐 User Authentication
- Secure user registration and login system
- Each user has their own private workout data
- Session-based authentication
- Logout functionality

### 💪 Workout Management
- Log workouts with activity name, duration, and date
- Edit existing workouts
- Delete workouts with confirmation page
- Workouts sorted by most recent first

### 🏷️ Workout Categories
- Separate Category model with ForeignKey relationship
- 5 default categories — Cardio, Strength, Flexibility, Sports, Other
- Color-coded badges for each category
- Filter workouts by category with one click
- Categories manageable through Django admin panel

### 📊 Interactive Dashboard
- Weekly activity bar chart (last 7 days)
- Category breakdown doughnut chart
- Stats cards — Total Workouts, Total Minutes, Total Hours, Most Active Day
- Powered by Chart.js
- Real-time data from Django backend

### 🚀 REST API
- Full CRUD API for workouts
- Categories listing endpoint
- Summary statistics endpoint
- Secured with session authentication
- Built with Django REST Framework

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python 3.13 | Core programming language |
| **Framework** | Django 4.2 | Web framework |
| **API** | Django REST Framework | REST API building |
| **Database** | SQLite | Data storage |
| **Frontend** | HTML5, CSS3 | Templates and styling |
| **Charts** | Chart.js | Interactive data visualization |
| **Deployment** | PythonAnywhere | Cloud hosting |
| **Version Control** | Git + GitHub | Source code management |

---

## 🏗️ Project Architecture

```
fitness_tracker/
│
├── fitness_project/           # Django project configuration
│   ├── settings.py            # Project settings
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py                # WSGI deployment entry point
│
├── tracker/                   # Main application
│   ├── migrations/            # Database migration history
│   ├── templates/tracker/     # HTML templates
│   │   ├── workout_list.html  # Main workout list with category filter
│   │   ├── dashboard.html     # Charts and statistics dashboard
│   │   ├── add_workout.html   # Add new workout form
│   │   ├── edit_workout.html  # Edit workout form
│   │   └── delete_workout.html# Delete confirmation page
│   ├── admin.py               # Customized admin panel
│   ├── models.py              # Category and Workout models
│   ├── views.py               # Web views and dashboard logic
│   ├── forms.py               # Django ModelForms
│   ├── urls.py                # App URL patterns
│   ├── serializers.py         # DRF serializers for API
│   ├── api_views.py           # REST API views
│   └── api_urls.py            # API URL patterns
│
├── accounts/                  # Authentication application
│   ├── templates/accounts/    # Login and register templates
│   ├── views.py               # Login, register, logout views
│   └── urls.py                # Auth URL patterns
│
├── staticfiles/               # Collected static files
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management utility
└── requirements.txt           # Python dependencies
```

---

## 🔌 REST API Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/api/workouts/` | List all user workouts | ✅ |
| POST | `/api/workouts/` | Create new workout | ✅ |
| GET | `/api/workouts/<id>/` | Get single workout | ✅ |
| PUT | `/api/workouts/<id>/` | Update workout | ✅ |
| DELETE | `/api/workouts/<id>/` | Delete workout | ✅ |
| GET | `/api/categories/` | List all categories | ✅ |
| GET | `/api/summary/` | Get stats summary | ✅ |

### Sample API Response — GET /api/workouts/
```json
{
    "count": 5,
    "results": [
        {
            "id": 1,
            "activity": "Morning Run",
            "duration": 30,
            "date": "2026-04-11",
            "category": 1,
            "category_name": "Cardio",
            "category_color": "#e74c3c",
            "category_icon": "🏃",
            "username": "sanjay"
        }
    ]
}
```

### Sample API Response — GET /api/summary/
```json
{
    "username": "sanjay",
    "total_workouts": 10,
    "total_minutes": 320,
    "total_hours": 5.3,
    "workouts_by_category": [
        {"category__name": "Cardio", "count": 4},
        {"category__name": "Strength", "count": 3}
    ]
}
```

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.8 or higher
- pip
- Git

### Installation Steps

**1. Clone the repository:**
```bash
git clone https://github.com/Sanjay284-beep/fitness-tracker.git
cd fitness-tracker
```

**2. Create and activate virtual environment:**
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Apply database migrations:**
```bash
python manage.py migrate
```

**5. Create admin superuser:**
```bash
python manage.py createsuperuser
```

**6. Add default categories via Django shell:**
```bash
python manage.py shell
```
```python
from tracker.models import Category
Category.objects.create(name='Cardio', color='#e74c3c', icon='🏃')
Category.objects.create(name='Strength', color='#e67e22', icon='💪')
Category.objects.create(name='Flexibility', color='#27ae60', icon='🧘')
Category.objects.create(name='Sports', color='#2980b9', icon='⚽')
Category.objects.create(name='Other', color='#8e44ad', icon='🏋️')
exit()
```

**7. Run the development server:**
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## 🚀 Deployment

This project is deployed on **PythonAnywhere** free tier.

### Key deployment steps:
- Uploaded project and created virtual environment on PythonAnywhere
- Configured WSGI file to point to Django settings
- Set `ALLOWED_HOSTS`, `STATIC_ROOT`, `DEBUG=False` for production
- Ran `collectstatic` to serve CSS and JS files
- Configured Web App settings on PythonAnywhere dashboard

---

## 🧠 Key Technical Concepts Demonstrated

### Backend
- **Django MVT Architecture** — Models, Views, Templates pattern
- **ForeignKey Relationships** — Category linked to Workout with `SET_NULL`
- **Query Optimization** — `select_related()` to minimize database queries
- **Django ORM Aggregations** — `Sum()`, `Count()`, `annotate()` for statistics
- **Class-based API Views** — `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`
- **Custom Serializers** — `SerializerMethodField` for computed fields
- **Login Required Decorator** — protecting views from unauthenticated access
- **URL Parameter Filtering** — category filter via `request.GET.get()`

### Frontend
- **Django Template Language** — dynamic HTML rendering
- **Chart.js Integration** — passing JSON data from Django to JavaScript charts
- **Responsive CSS Grid** — mobile-friendly layout
- **Dynamic Styling** — category colors stored in database, applied in templates

### DevOps
- **Git Version Control** — full commit history
- **PythonAnywhere Deployment** — live production environment
- **Virtual Environments** — isolated dependency management
- **Static Files Management** — `collectstatic` for production

---

## 📋 Requirements

```
Django>=4.2
djangorestframework
asgiref
sqlparse
```

---

## 🔮 Future Improvements

- [ ] Add workout streak tracking
- [ ] Weekly/monthly workout goals
- [ ] Export workouts as CSV
- [ ] Social features — follow friends
- [ ] Mobile app using the REST API
- [ ] PostgreSQL database for production
- [ ] Docker containerization
- [ ] CI/CD pipeline with GitHub Actions

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Narra Sanjay**
- 🌐 Live App: [sanjayn.pythonanywhere.com](https://sanjayn.pythonanywhere.com)
- 💻 GitHub: [@Sanjay284-beep](https://github.com/Sanjay284-beep)
- 📧 Email: narrasanjayigy7@gmail.com

---

## 🏆 What I Learned Building This

This project taught me the complete Django development cycle:

1. **Project setup** — virtual environments, Django project structure
2. **Database modeling** — defining models, migrations, relationships
3. **Authentication** — Django's built-in auth system
4. **CRUD operations** — Create, Read, Update, Delete with forms and views
5. **REST APIs** — Django REST Framework, serializers, class-based API views
6. **Data visualization** — passing backend data to Chart.js
7. **Deployment** — taking a local project live on the internet
8. **Version control** — Git workflow, GitHub

---

> Built from scratch with ❤️ — from zero to a fully deployed full-stack web application! 🚀
