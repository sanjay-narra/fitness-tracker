<div align="center">

<h1>🏋️ FitTrack — Personal Fitness Tracker</h1>

<p><em>A full-stack Django web app to log workouts, visualize progress with interactive charts, and expose a complete REST API — deployed live on PythonAnywhere.</em></p>

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.x-D00000?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Deployed](https://img.shields.io/badge/Deployed-PythonAnywhere-FFD43B?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

<br>

🌐 **[Live Demo](https://sanjayn.pythonanywhere.com)** &nbsp;·&nbsp; 📂 **[GitHub Repo](https://github.com/sanjay-narra/fitness-tracker)**

</div>

---

## 🚀 What This Project Does

FitTrack lets users register, log their workouts by category, and instantly see their progress on a live dashboard — weekly bar charts, category doughnut charts, and summary stats (total workouts, total minutes, most active day). On the backend, every feature is also exposed as a **secured REST API** built with Django REST Framework, ready to power a mobile app.

Built end-to-end: database design → authentication → CRUD → API → Chart.js visualizations → cloud deployment.

---

## 🖥️ App Preview

<div align="center">

| Login | Workout List |
|:---:|:---:|
| <img src="screenshots/Login.png" width="100%" alt="Login Page"/> | <img src="screenshots/workouts.png" width="100%" alt="Workout List"/> |

| Dashboard | Add Workout |
|:---:|:---:|
| <img src="screenshots/dashboard.png" width="100%" alt="Dashboard"/> | <img src="screenshots/Add.png" width="100%" alt="Add Workout"/> |

</div>

---

## ✨ Features

### 🔐 Authentication
- Secure registration, login, and logout
- Each user sees only their own data
- Session-based authentication with login-required protection on all views

### 💪 Workout Management
- Log workouts with activity name, duration, date, and category
- Edit and delete workouts (with confirmation)
- List sorted by most recent first

### 🏷️ Categories
- 5 default categories: Cardio, Strength, Flexibility, Sports, Other
- Color-coded badges per category
- One-click category filter on the workout list
- Fully manageable via Django admin

### 📊 Interactive Dashboard
- **Weekly bar chart** — activity over the last 7 days
- **Doughnut chart** — breakdown by category
- **Stats cards** — Total Workouts · Total Minutes · Total Hours · Most Active Day
- Powered by Chart.js with real-time data from the Django backend

### 🔌 REST API
- Full CRUD for workouts
- Categories listing and summary stats endpoints
- Secured with session authentication
- Built with Django REST Framework

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Backend | Python 3.13 | Core language |
| Framework | Django 4.2 | Web framework & ORM |
| API | Django REST Framework | REST API |
| Database | SQLite | Data storage |
| Frontend | HTML5, CSS3 | Templates & styling |
| Charts | Chart.js | Interactive visualizations |
| Hosting | PythonAnywhere | Cloud deployment |
| Version Control | Git + GitHub | Source management |

---

## 🔌 REST API Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/workouts/` | List all user workouts | ✅ |
| POST | `/api/workouts/` | Create a new workout | ✅ |
| GET | `/api/workouts/<id>/` | Get a single workout | ✅ |
| PUT | `/api/workouts/<id>/` | Update a workout | ✅ |
| DELETE | `/api/workouts/<id>/` | Delete a workout | ✅ |
| GET | `/api/categories/` | List all categories | ✅ |
| GET | `/api/summary/` | Get stats summary | ✅ |

**Sample response — `GET /api/workouts/`**

```json
{
    "count": 5,
    "results": [
        {
            "id": 1,
            "activity": "Morning Run",
            "duration": 30,
            "date": "2026-04-11",
            "category_name": "Cardio",
            "category_color": "#e74c3c",
            "category_icon": "🏃",
            "username": "sanjay"
        }
    ]
}
```

---

## 📁 Project Structure

```
fitness_tracker/
├── fitness_project/            # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tracker/                    # Core app
│   ├── models.py               # Category & Workout models
│   ├── views.py                # Web views & dashboard logic
│   ├── forms.py                # Django ModelForms
│   ├── admin.py                # Customized admin panel
│   ├── serializers.py          # DRF serializers
│   ├── api_views.py            # REST API views
│   ├── api_urls.py             # API URL patterns
│   ├── urls.py                 # App URL patterns
│   └── templates/tracker/
│       ├── workout_list.html
│       ├── dashboard.html
│       ├── add_workout.html
│       ├── edit_workout.html
│       └── delete_workout.html
│
├── accounts/                   # Auth app
│   ├── views.py
│   ├── urls.py
│   └── templates/accounts/
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Local Setup

**1. Clone the repo**
```bash
git clone https://github.com/sanjay-narra/fitness-tracker.git
cd fitness-tracker
```

**2. Create & activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Apply migrations**
```bash
python manage.py migrate
```

**5. Seed default categories**
```bash
python manage.py shell
```
```python
from tracker.models import Category
Category.objects.create(name='Cardio',      color='#e74c3c', icon='🏃')
Category.objects.create(name='Strength',    color='#e67e22', icon='💪')
Category.objects.create(name='Flexibility', color='#27ae60', icon='🧘')
Category.objects.create(name='Sports',      color='#2980b9', icon='⚽')
Category.objects.create(name='Other',       color='#8e44ad', icon='🏋️')
exit()
```

**6. Run the dev server**
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## 🧠 Key Concepts Demonstrated

| Area | Concepts |
|------|----------|
| **Django ORM** | ForeignKey with `SET_NULL`, `select_related()`, `Sum()` / `Count()` / `annotate()` |
| **Auth** | Session-based login, `@login_required` decorator |
| **REST API** | DRF serializers, class-based API views, CRUD endpoints |
| **Frontend** | Django Template Language, Chart.js JSON integration, CSS Grid |
| **Deployment** | WSGI config, `DEBUG=False`, `collectstatic`, PythonAnywhere |
| **DevOps** | Git workflow, virtual environments, dependency management |

---

## 🔮 Roadmap

- [ ] Workout streak tracking with badges
- [ ] Mobile app using the REST API
- [ ] PostgreSQL migration for production
- [ ] Docker containerization
- [ ] CI/CD with GitHub Actions

---

## 👨‍💻 Author

<div align="center">

**Narra Sanjay** · B.Tech Computer Science Engineering, 2026

[![Live App](https://img.shields.io/badge/Live%20App-sanjayn.pythonanywhere.com-22c55e?style=for-the-badge&logo=python&logoColor=white)](https://sanjayn.pythonanywhere.com)&nbsp;&nbsp;[![GitHub](https://img.shields.io/badge/GitHub-sanjay--narra-181717?style=for-the-badge&logo=github)](https://github.com/sanjay-narra)&nbsp;&nbsp;[![Email](https://img.shields.io/badge/Email-narrasanjayigy7@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:narrasanjayigy7@gmail.com)

</div>

---

<div align="center">
<sub>Licensed under the <a href="LICENSE">MIT License</a> · Built and deployed end-to-end by Narra Sanjay</sub>
</div>
