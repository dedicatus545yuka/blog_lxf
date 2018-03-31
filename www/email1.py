from threading import Thread
from flask import render_template
from flask_mail import Message, Mail
from flask import Flask

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '670754807@qq.com'
app.config['MAIL_PASSWORD'] = 'jocotefehyqzbegi'

# app.config['FLASKY_ADMIN'] = '670754807@qq.com'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <670754807@qq.com>'


def send_async_email(app, msg):
	with app.app_context():
		mail = Mail(app)
		mail.send(msg)

def send_email(to, subject, template, **kwargs):
	msg = Message(
	app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
	sender=app.config['FLASKY_MAIL_SENDER'],
	recipients=[to]
	)
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	# mail.send(msg) # 同步发送
	thr = Thread(target=send_async_email, args=[app, msg])
	thr.start()
	return thr



if __name__ == '__main__':
	app.run(debug=True)
