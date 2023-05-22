from flask import Flask, render_template,request
import datetime
import smtplib
import wtforms

# OWN_EMAIL = "estujemato@gmail.com"
# OWN_PASSWORD = "abcababc"

app = Flask(__name__)

@app.route('/')
def home_page():
    footer_tag = datetime.datetime.now().year
    return render_template('index.html',footer_el=footer_tag)

@app.route("/contact", methods=["POST","GET"])
def contact():
    if request.method=="POST":
        # send_email(request.form["name"], request.form["email"], request.form["message"])
        return render_template('index.html', msg_sent=True)
    return render_template("index.html", msg_sent=False)

# def send_email(name, email, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(OWN_EMAIL, OWN_PASSWORD)
#         connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    