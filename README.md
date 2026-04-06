# 🎓 College Event Registration System

A modern, full-stack web application designed for seamless student registration for university events. This project features a clean user interface and a robust backend connected to a MySQL database.

---

## 🚀 Features
* **Clean UI:** Minimalistic design with smooth transitions and responsive layout.
* **Real-time Interactivity:** Uses JavaScript Fetch API to submit data without page reloads.
* **Automated Database Management:** Backend automatically generates necessary SQL tables on first run.
* **Admin Panel:** A protected view to monitor all student registrations in a tabular format.

---

## 🛠️ Technology Stack
* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Python 3.14, Flask Framework
* **Database:** MySQL (Relational Database)
* **ORM:** SQLAlchemy (Object Relational Mapper)
* **Server:** XAMPP (Apache & MySQL)

---

## 📈 Step-by-Step Development Process

To build this project from scratch, the following methodology was followed:

### Phase 1: Environment & Architecture Setup
* Initialized a Python virtual environment and installed necessary dependencies (`Flask`, `SQLAlchemy`, `PyMySQL`).
* Structured the project using the **Flask Blueprint** pattern: `static/` for assets, `templates/` for HTML, and `app.py` as the entry point.

### Phase 2: Database Modeling
* Configured a local MySQL server using **XAMPP**.
* Designed a `Registration` model in Python to define the database schema (Fields: Name, ID, Course, Event).

### Phase 3: Backend Logic (API)
* Created a `POST` route (`/register`) to handle incoming data.
* Implemented error handling to prevent application crashes during database downtime.
* Developed the `/admin` route to query the database and pass record sets to the frontend.

### Phase 4: Frontend Design & UX
* Developed a CSS stylesheet focusing on typography and white space.
* Integrated **JavaScript** to intercept form submissions, allowing for a "Single Page Application" feel by updating the UI dynamically upon success.

---

## 💻 Installation & Setup

Follow these steps to run the project locally:

### 1. Prerequisites
* Install [Python 3.14](https://www.python.org/)
* Install [XAMPP](https://www.apachefriends.org/)

### 2. Database Configuration
1.  Open XAMPP Control Panel and start **Apache** and **MySQL**.
2.  Navigate to `http://localhost/phpmyadmin/`.
3.  Create a new database named **`college_db`**.

### 3. Application Setup
1.  Clone this repository or download the ZIP.
2.  Open your terminal in the project folder and install requirements:
    ```bash
    pip install flask flask-sqlalchemy pymysql
    ```
3.  Run the application:
    ```bash
    python app.py
    ```

### 4. Accessing the App
* **Student Registration:** `http://127.0.0.1:5000/`
* **Admin View:** `http://127.0.0.1:5000/admin`

---

## 📂 Project Structure
```text
college_event_project/
│
├── app.py              # Flask Backend & Database Configuration
├── requirements.txt    # List of Python dependencies
├── static/             # Assets Folder
│   ├── style.css       # Aesthetic Custom Styles
│   └── script.js       # Frontend Logic (Fetch API)
└── templates/          # HTML Views
    ├── index.html      # Registration Form
    └── admin.html      # Records Table View
