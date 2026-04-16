# College Notice Board System

A simple full-stack web application with login (student/admin), notice listing, and admin notice creation.

---

## 📁 Project Structure

```
college_notice_board/
├── index.html       ← Login page
├── student.html     ← Student notice view
├── admin.html       ← Admin notice view + add notice
├── notices.js       ← Shared JS to load/render notices
├── style.css        ← All styles
├── app.py           ← Flask backend (all APIs)
├── requirements.txt ← Python packages
└── setup.sql        ← MySQL setup queries
```

---

## 🚀 Setup Steps

### 1. Set Up MySQL Database

Open MySQL and run:
```sql
source setup.sql
```
Or paste the contents of `setup.sql` into your MySQL client.

### 2. Update Database Credentials in app.py

Edit the `get_db()` function in `app.py`:
```python
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",      # ← your MySQL username
        password="",      # ← your MySQL password
        database="college_notice_board"
    )
```

### 3. Install Python Packages

```bash
pip install -r requirements.txt
```

### 4. Run the Backend

```bash
python app.py
```

Backend runs at: `http://localhost:5000`

### 5. Open the Frontend

Open `index.html` in your browser directly (double-click), or serve it with:
```bash
# Python simple server (from project folder)
python -m http.server 8080
```
Then visit: `http://localhost:8080`

---

## 🔐 Demo Login Credentials

| Role    | Email                  | Password    |
|---------|------------------------|-------------|
| Admin   | admin@college.edu      | admin123    |
| Student | student@college.edu    | student123  |

---

## 🔌 API Endpoints

| Method | Endpoint      | Description                    |
|--------|---------------|--------------------------------|
| POST   | /login        | Login with email + password    |
| GET    | /notices      | Get all notices                |
| POST   | /add-notice   | Add a new notice (admin only)  |
| POST   | /logout       | Clear session                  |
