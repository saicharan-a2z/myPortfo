from flask import Flask, render_template, request, redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    to_email = request.form['to']
    subject = request.form['subject']
    message = request.form['message']

    # Set up your email details
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'

    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to_email
        msg.set_content(message)

        # SMTP settings (use your email provider's)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        return "Email sent successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
