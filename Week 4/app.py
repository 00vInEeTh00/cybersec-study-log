from flask import Flask, render_template,request, redirect,flash,session,url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import generate_csrf

from flask_talisman import Talisman
import requests
import re


# password hashing
# email verification
# api integration
# https 
# csrf token
# strong password
# talissman




app = Flask(__name__)
app.secret_key = 'evaskey123'

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]", password):
        return False
    return True

Talisman(app) 


# Database config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'myflaskdb'
mysql = MySQL(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'evastir81@gmail.com'  
app.config['MAIL_PASSWORD'] = 'qxheckgdmrneywhc'      
app.config['MAIL_DEFAULT_SENDER'] = 'evastir81@gmail.com'   # ✔️ Usually same as username
mail = Mail(app)

s = URLSafeTimedSerializer("ThisIsASecretKey!")

app.config['SECRET_KEY'] = 'super-secret-key-here'  # make this long and random!
csrf = CSRFProtect(app)

@app.route("/")
def home():
    session.clear()  
    return redirect("/login")


@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf)

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        name = session['user']

        city = "Kozhikode"
        api_key = "f46347d52a33b0f216bea1d3accae355"
        url = url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response =requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
        else:
            temp = "N/A"
            desc = "Could not fetch weather."


        return render_template("dashboard.html", name=name, city=city,temp=temp ,desc=desc)
    else:
        flash("Please log in first")
        return redirect("/login")

    

@app.route("/register" ,methods = ['GET','POST'])
def register():
    if request.method == "POST":
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash("❌ Passwords do not match", "register")
            return render_template("register.html")

        if not is_strong_password(password):
            flash("❌ Password must be at least 6 characters long","register")
            flash("and inlude uppercase, lowercase, number, and special character.","register")
            return render_template("register.html")
        
        hashed_password = generate_password_hash(password)
        
         # ✅ Store temporarily in session (or in a secure cache/db if big)
        session['pending_user'] = {
            'fullname': fullname,
            'username': username,
            'email': email,
            'password': hashed_password
        }   

        token = s.dumps(email, salt='email-confirm')
        confirm_url = url_for('confirm_email', token=token,_external=True)

        msg = Message("Confirm Your Email.",recipients=[email])
        msg.body = f"Hi {fullname}, click the link to confirm your email: {confirm_url}"
        mail.send(msg)

        flash("✅ Thanks for registering! ", "register")
        flash("Please check your email to activate your account.","register")
        return redirect("/register")
        
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print("📥 Form received:", email, password)

        # ✅ Only check email in SQL
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user:
            print("✅ User found in DB:", user)
            stored_password = user[4]  # 🔐 Hashed password
            is_confirmed = user[5]     # ✅ Confirmed field
            print("🔒 Checking if confirmed:", is_confirmed)

            if not is_confirmed:
                flash("❌ Please confirm your email first.", "login")
                return redirect("/register")

            if check_password_hash(stored_password, password):
                session['user'] = user[1]  # 👤 Username or whatever you like
                print("🎉 Password matched, redirecting to dashboard")
                return redirect("/dashboard")
            else:
                flash("❌ Incorrect password.", "login")
                print("❌ Password didn't match")
        else:
            flash("❌ No user found with that email.", "login")
            print("❌ No user found")

        return redirect("/login")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop('email', None)  # Remove email from session
    flash("👋 You have been logged out.")
    return redirect("/login")


@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
        pending = session.get('pending_user')

        if not pending or pending['email'] != email:
            flash("Invalid or expired confirmation link.","login")
            return redirect("/register")

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cur.fetchone():
            flash("⚠️ This email is already registered.", "login")
            return redirect("/login")

         # ✅ Insert into database
        cur.execute("INSERT INTO users (fullname, username, email, password, confirmed) VALUES (%s, %s, %s, %s, %s)",
                    (pending['fullname'], pending['username'], pending['email'], pending['password'], True))
        mysql.connection.commit()
        cur.close()

        session.pop('pending_user',None)

        flash("Email confirmed! You can now log in.","login")
        return redirect("/login")

    except Exception as e:
        print("Token error :",e)
        flash("The confirmation link is invalid or expired .","login")
        return redirect("/register")



if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
