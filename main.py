from flask import Flask, render_template, redirect, url_for, request, flash
import smtplib
import os


app = Flask(__name__)
app.secret_key = "2589"


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
        my_email="latifshahzada4@gmail.com"
        password="jfkzbjgubfytvbcw"
        message = request.form['message']
        name = request.form['name']
        email = request.form['email']
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="madasar54321@gmail.com",
                                msg=f"Subject: Query from Shahzada's portfolio!\n\nMessage: {message}\n\nContact information of sender:\nName: {name}\n\nEmail: {email}",
                                )
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