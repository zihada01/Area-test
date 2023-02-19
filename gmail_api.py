#!/usr/bin/env python
# encoding: utf-8

# Imports
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
from googleapiclient.errors import HttpError
import os.path
from flask import Blueprint

Gmail = Blueprint('Gmail', __name__)

global gmail_service
# Authenticate
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.modify https://mail.google.com/'


def gmail_authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return (service)

/*@Gmail.route('/auth_gmail', methods=['POST'])
def auth_gmail():
    global gmail_service
    service = gmail_authenticate()
    gmail_service = service
    return '0K', 200
*/
