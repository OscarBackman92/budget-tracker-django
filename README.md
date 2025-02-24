# 📜 Budget Tracker API

A Django-based **Budget Tracker API** with **user authentication, transaction management, and PostgreSQL support**.
Includes **Django REST Framework (DRF), JWT authentication, and Heroku deployment**.

## 🚀 Features
✅ **User Authentication** (`dj-rest-auth` & `django-allauth`)  
✅ **JWT Authentication** (`djangorestframework-simplejwt`)  
✅ **CRUD Operations for Transactions** (Income/Expense tracking)  
✅ **Role-based Access Control** (Users can only manage their own transactions)  
✅ **Pagination, Filtering, and Ordering** (`django-filter`, DRF pagination)  
✅ **PostgreSQL Support** for production (SQLite for development)  
✅ **Heroku Deployment Ready** (`gunicorn`, `whitenoise` for static files)  

---

## 📦 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_USERNAME/budget-tracker-django.git
cd budget-tracker-django
```

### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project root:
```
DEBUG=True
SECRET_KEY=your-super-secret-key
DATABASE_URL=your_database_url_here
```

---

## 🐘 Database Setup
### For Local Development (SQLite)
```sh
python manage.py migrate
```
### For Production (PostgreSQL)
Ensure **`DATABASE_URL`** is set in `.env` or on Heroku.

---

## 🛠️ Running the Server
### Start Local Development Server
```sh
python manage.py runserver
```
✅ Server runs at **http://127.0.0.1:8000/**  

---

## 🧪 Running Tests
```sh
python manage.py test transactions
```
✅ Expected output:
```plaintext
Ran 8 tests in 4.494s
OK
```

---

## 🛠 API Endpoints
### 🔐 Authentication
| Method | Endpoint                     | Description |
|--------|------------------------------|-------------|
| `POST`  | `/auth/registration/`         | Register a new user |
| `POST`  | `/auth/login/`                | Log in a user (returns JWT token) |
| `POST`  | `/auth/logout/`               | Log out a user |
| `POST`  | `/auth/token/refresh/`        | Refresh JWT token |

### 💰 Transactions
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| `GET`  | `/transactions/`       | Get all transactions (user-specific) |
| `POST` | `/transactions/`       | Create a new transaction |
| `GET`  | `/transactions/{id}/`  | Get a single transaction |
| `PATCH`| `/transactions/{id}/`  | Update a transaction |
| `DELETE` | `/transactions/{id}/` | Delete a transaction |

---

## 🚀 Deploying to Heroku
### 1️⃣ Create a Heroku App
```sh
heroku create your-app-name
```

### 2️⃣ Add Heroku PostgreSQL
```sh
heroku addons:create heroku-postgresql:hobby-dev
```

### 3️⃣ Set Environment Variables
```sh
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-production-secret-key
heroku config:set DATABASE_URL=your-production-database-url
```

### 4️⃣ Deploy the App
```sh
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### 5️⃣ Run Migrations on Heroku
```sh
heroku run python manage.py migrate
```

### 6️⃣ Open the App
```sh
heroku open
```

✅ **Your API is now live on Heroku!** 🎉  

---

## 📜 License
This project is licensed under the MIT License.

