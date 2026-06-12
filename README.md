# 🛒 Django E-Commerce (Persian / Localized)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20.svg?logo=django&logoColor=white)
![Localization](https://img.shields.io/badge/Localization-Persian%20(FA)-success.svg)
![E-Commerce](https://img.shields.io/badge/Domain-E--Commerce-FFA500.svg)

## 📖 Overview
A fully functional, localized e-commerce backend platform built with Django, specifically tailored for the Iranian market. This project bridges the gap between standard e-commerce features and regional requirements, demonstrating expertise in handling Persian language constraints, Jalali calendars, and localized payment flows.

## ✨ Key Features & Localization
* **Full E-Commerce Flow:** Product catalog, shopping cart sessions, inventory management, and order processing.
* **Persian Localization (i18n):** Fully configured for Persian language (FA) and RTL (Right-to-Left) interface compatibility.
* **Jalali Date Integration:** Seamless conversion and display of standard dates to Jalali (Shamsi) calendar for realistic local user experience.
* **Payment Gateway Ready:** Architecture designed to easily integrate with Iranian payment providers (e.g., ZarinPal, IDPay).
* **Custom Admin Panel:** Enhanced Django admin interface for easy product and order management by local store owners.

## 🛠️ Tech Stack
* **Backend:** Python, Django
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Frontend/Templates:** Django Templates (HTML/CSS) with RTL support
* **Date Management:** `django-jalali` (or similar packages for Shamsi dates)

## 🚀 Quick Start (Local Setup)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Abolfazlparadox/Web-Ecommerce-Django-Persian.git](https://github.com/Abolfazlparadox/Web-Ecommerce-Django-Persian.git)
   cd Web-Ecommerce-Django-Persian
    
    ```

2. **Create and Activate Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


4. **Apply Migrations:**
```bash
python manage.py migrate

```


5. **Create Superuser (Admin):**
```bash
python manage.py createsuperuser

```


6. **Run the Server:**
```bash
python manage.py runserver

```


Access the website at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## 💼 Why This Project Matters

Developing for localized markets presents unique backend challenges—from handling non-ASCII string operations to timezone and calendar conversions. This project showcases the ability to adapt standard frameworks to specific regional business needs.

## ✉️ Contact

**Abolfazl Mohammadshahi** - Backend Developer

* [LinkedIn](https://www.linkedin.com/in/abolfazl-mohammadshahi-12b87b324)
* [GitHub](https://www.google.com/search?q=https://github.com/Abolfazlparadox)
* Email: abolfazlmohammadshahi78@gmail.com
