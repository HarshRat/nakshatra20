import os
from flask import url_for
from requests import post as send_post

def send_reset_email(user):
    MAILGUN_DOMAIN = os.environ['MAILGUN_DOMAIN']
    MAILGUN_API_KEY = os.environ['MAILGUN_API_KEY']
    FROM_TITLE = 'Reset Password'
    FROM_EMAIL = os.environ['MAILGUN_EMAIL']
    token = user.get_reset_token()
    response = send_post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            'from': f"{FROM_TITLE} <{FROM_EMAIL}>",
            'to': user.email,
            'subject': 'RESET YOUR PASSWORD',
            'text': f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
''',
            'html':''
        }
    )

def send_generated_login(user,gen_password):
    MAILGUN_DOMAIN = os.environ['MAILGUN_DOMAIN']
    MAILGUN_API_KEY = os.environ['MAILGUN_API_KEY']
    FROM_TITLE = 'Login Password for Treasure Hunt (Nakshatra\' 20)'
    FROM_EMAIL = os.environ['MAILGUN_EMAIL']
    response = send_post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            'from': f"{FROM_TITLE} <{FROM_EMAIL}>",
            'to': user.email,
            'subject': f'Login Password for Treasure Hunt (Nakshatra\' 20): {gen_password}',
            'text': f'''Your details:
username: {user.email}
password: {gen_password}
If you did not make this request then simply ignore this email and no changes will be made.
''',
            'html':''
        }
    )