PYTHON FLASK PROJECT


E

     1.  ## 📌 What is App Routing?

        App Routing is how Flask connects a **URL** (like `/home`) to a **Python function** (like `home()`).

        It tells Flask:
        > “When a user goes to this web address, run this function!”

        We use the `@app.route()` decorator to create routes.

 In Simple Eva Words:

    🧠 "__name__ means → the name of the file I’m in now"
    🧠 "__main__" means → I’m the file being run right now!"
    
    # Flask Redirect and `url_for()` Demo

This is a simple Flask project that shows how to use:

- 🔁 `redirect()` – to send the user to a different page
- 🌐 `url_for()` – to find the current URL of a function


# Flask Request Methods Demo

This is a simple Flask project that shows how to use:

- 🧠 `request.args.get()` – to get data from the URL (GET request)
- 📝 `request.form.get()` – to get data from a form (POST request)
- 🧾 `request.get_json()` – to read JSON data (used in APIs)
- 📁 `request.files['file']` – to handle file uploads
- 🧪



## 🚦 What is Routing?

In **Flask**, routing is the process of connecting a **URL path** to a **Python function**.

🧠 When someone visits a web address like `http://localhost:5000/`,  
Flask checks if you have a route for it and then runs the connected function.

It's like setting up road signs 🪧 for different pages in your app!

---

## 🧱 Static Routing

### ✅ What is Static Routing?

A **static route** uses a **fixed URL**.  
When someone visits that exact URL, Flask returns the same response every time.

### 📘 Example 1: Homepage and About Page

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🏠 This is the homepage."

@app.route("/about")
def about():
    return "📖 This is the about page."
    
    


# ❓ Flask Query Strings — Beginner Guide

This guide explains **what query strings are** and **how to use them** in a Flask app using `request.args.get()`.

---

## 🌐 What is a Query String?

A **query string** is extra information added to the end of a URL.

It starts with a `?` and uses **key-value pairs**.

### 📘 Example:
from flask import Flask, request
app = Flask(__name__)

@app.route("/greet")
def greet():
    name = request.args.get("name")
    age = request.args.get("age")
    return f"👋 Hello, {name}! You are {age} years old."

if __name__ == "__main__":
    app.run(port=3000)

🌐 Example URL:

http://localhost:3000/greet?name=Eva&age=10



## Dynamic Routing
✅ What is Dynamic Routing?

A dynamic route lets you pass a value in the URL (like a name or number).
Flask will read the value and give a custom response.

You write it using angle brackets like <name> or <int:age>.
📘 Example 1: Greet by Name

@app.route("/hello/<name>")
def greet(name):
    return f"👋 Hello, {name}!"

    Visiting /hello/Eva → 👋 Hello, Eva!

    Visiting /hello/Tom → 👋 Hello, Tom!

📘 Example 2: Show User with Age

@app.route("/user/<name>/<int:age>")
def show_user(name, age):
    return f"👤 {name} is {age} years old."
    



# 🧁 Flask Template Rendering — Random HTML Page Example

This guide shows how to use **Flask** to render a simple **HTML template** using `render_template()`.

---

## 🎨 What Does "Render a Template" Mean?

In Flask, instead of returning plain text like `"Hello"`,  
you can show a real web page using an HTML file.

✅ You do this with:

```python
from flask import render_template

return render_template("template.html")

 Folder Structure (Important!)

Flask looks for HTML files in a special folder called templates.

project/
├── app.py
└── templates/
    └── random_page.html
    
    
    
    
    

# 🌟 Jinja2 Template Engine — Beginner Guide for Flask 🐍

Welcome! This guide explains what **Jinja2** is, why it is used with **Flask**, and how to use it step-by-step with simple examples for beginners.

---

## 📦 What is Jinja2?

**Jinja2** is a **template engine** for Python, mainly used with Flask.

✅ It lets you:
- Write **dynamic HTML pages**
- Mix **Python logic** into HTML
- Display variables, loops, if-else, and more

🧠 Think of it as a bridge between **Python** and **HTML**!

---

## 🎯 Why Use Jinja2 in Flask?

Without Jinja2, you can only return **plain text** from Flask:

```python
return "Hello"


With Jinja2, you can return full HTML pages with Python logic inside:

return render_template("hello.html", name="Eva")

Then in hello.html, show the name like this:

<h1>Hello {{ name }}!</h1>

✅ This makes your web app smarter, interactive, and fun!



🧰 Jinja2 Syntax (Super Easy!)
Type	Syntax	What It Does
Show variable	{{ variable }}	Shows a Python value
Logic block	{% ... %}	Runs logic like if, for, with
Comment	{# comment #}	Hidden comment in template






---

## 🧠 Why Use Static Files?

- CSS makes your page **beautiful**
- Images make it **visual**
- JavaScript makes it **interactive**

---

## 💡 How to Use Static Files in HTML

Use Flask’s `url_for('static', filename='...')` like this:

```html
<!-- Link to CSS file -->
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

<!-- Show image -->
<img src="{{ url_for('static', filename='happy.png') }}" alt="Happy Face">

<!-- Add JavaScript -->
<script src="{{ url_for('static', filename='script.js') }}"></script>

    
    
    
    🏗️ Folder Structure in Flask

Flask looks for static files inside a folder named static

project/
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── style.css
    ├── script.js
    └── happy.png
    




    # 🐬 Flask MySQL Database Integration Guide

This guide shows how to **configure** MySQL in Flask and how to **save data** into your MySQL database step-by-step. It's beginner-friendly and perfect for new Flask learners! 💡

---

## ✅ What You'll Learn

- How to connect Flask to a MySQL database
- How to configure the connection
- How to create a users table
- How to insert user data into the table

---

## 1️⃣ MySQL Configuration in Flask

First, install `flask_mysqldb`:

```bash
pip install flask-mysqldb

    
    
    Now, add the MySQL settings in your app.py:

from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# ✅ MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'eva_flask_db'

mysql = MySQL(app)
    
    
    
    2️⃣ Create MySQL Database and Table

In your MySQL terminal or phpMyAdmin, run the following:

-- Create a database
CREATE DATABASE eva_flask_db;

-- Use the database
USE eva_flask_db;

-- Create a table to store user info
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100),
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(255)
);
    
   
   3️⃣ Create a Registration Form (register.html)
    
    
    
    4️⃣ Insert Form Data into MySQL

In app.py, add this route:

from flask import render_template, request, redirect, flash
from werkzeug.security import generate_password_hash

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("❌ Passwords do not match!")
            return redirect('/register')

        hashed_password = generate_password_hash(password)

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users (fullname, username, email, password) VALUES (%s, %s, %s, %s)",
            (fullname, username, email, hashed_password)
        )
        mysql.connection.commit()
        cur.close()

        flash("✅ Registered successfully!")
        return redirect('/register')

    return render_template('register.html')
    
    
    
    
    
    
    
    
    # 🔐 Hashed Password in Flask (Simple Guide)

---

## ✅ What is a Hashed Password?

A **hashed password** is a secret version of your real password.

Instead of saving this:

hello123


We save this:

$pbkdf2-sha256$29000$3gRwv...


This protects the user's password, so no one can read it — even if they see your database!

---

## 🔧 How to Create (Hash) a Password

Use this function in Flask:

```python
from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash("hello123")

Now save hashed_password in your database.
🔍 How to Check the Password (on Login)

Use this function to check if the user typed the correct password:

from werkzeug.security import check_password_hash

check_password_hash(stored_password_from_db, typed_password)

Returns True if they match.
    
    
    
    
    
    
# 🛡️ CSRF Token in Flask — Full Guide for Beginners

This note explains what a **CSRF token** is and how to implement it step-by-step in a Flask application. It's simple, secure, and beginner-friendly!

---

## 🧠 What Is a CSRF Token?

CSRF stands for:

> **C**ross-**S**ite **R**equest **F**orgery

It's a type of **cyber attack** where a bad website tries to **submit your form without your permission** 😠

A **CSRF token** is a secret code that Flask adds to your form.  
✅ Only the real user can send this secret.  
❌ Hackers don’t know it — so Flask blocks them!

---

## 🛠️ How to Implement CSRF Token in Flask

---

### ✅ Step 1: Install Flask-WTF

```bash
pip install flask-wtf



✅ Step 2: Setup CSRF in Your Flask App

In your app.py file:

from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF

csrf = CSRFProtect(app)

    📝 Hint: The secret_key keeps your tokens secure.



    
✅ Step 3: Add CSRF Token to Your HTML Form

In your HTML form (like register.html):

       <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
    
    
✅ Step 4: Done! CSRF is Now Active 🎉

Now when the form is submitted, Flask will:

✅ Check the CSRF token
✅ Allow good requests
❌ Block fake/unsafe requests
    
   





# 📦 Flask Sessions — Beginner Guide

This note explains what a **session** is and how to use it in your Flask app to remember user data, like login information.

---

## 🧠 What Is a Session?

A **session** is like a **temporary memory box** 📦 that stores data about the user during their visit.

### ✨ Example:
When a user logs in, Flask can remember their name across pages using a session.

Without session:
- Flask forgets the user every time they visit a new page ❌

With session:
- Flask remembers who they are ✅

---

## 🔐 Why Use Sessions?

| You Want To...            | Use a Session? |
|---------------------------|----------------|
| Keep a user logged in     | ✅              |
| Remember user preferences | ✅              |
| Store temporary info      | ✅              |

---

## 🛠️ How to Use Sessions in Flask

---

### ✅ Step 1: Import and Set Secret Key

```python
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required to use sessions

    

✅ Step 2: Store Data in a Session

session['username'] = 'Eva'
session['user_id'] = 101

    🎉 This remembers the user info until they log out or close the browser.

✅ Step 3: Access Data from Session

username = session.get('username')
print(username)  # Output: Eva

✅ Step 4: Remove or Clear Session (Logout)

session.pop('username', None)  # Remove just one item
session.clear()                # Clear all session data

