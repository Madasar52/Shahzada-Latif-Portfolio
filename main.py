from flask import Flask, render_template, redirect, url_for, request, flash
import smtplib
import os
from email.mime.text import MIMEText


app = Flask(__name__)
app.secret_key = os.environ.get("secret_key")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blog-home")
def blog_home():
    return render_template('blog-home.html')

@app.route("/blog-post")
def blog_post():
    return render_template('blog-post.html')

@app.route("/case-study")
def case_study():
    return render_template('case-study.html')

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=="POST":
        my_email=os.environ.get("email")
        to_email = os.environ.get("my_email")
        password=os.environ.get("password")
        message = request.form['message']
        name = request.form['name']
        email = request.form['email']

        msg = MIMEText(f"Message: {message}\n\nContact information of sender:\nName: {name}\n\nEmail: {email}")
        msg['Subject'] = "Query from Shahzada's portfolio!"

        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(my_email, password)
        s.sendmail(my_email, to_email, msg.as_string())
        s.quit()
        flash("Email sent to Shahzada!")
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')




if __name__ == '__main__':
    app.run(debug=False, port=5001)