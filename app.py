from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from google import genai
from google.genai import types
import re
from typing import Optional, Dict
from PyPDF2 import PdfReader
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import io
from sentence_transformers import SentenceTransformer
import datetime

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

# Setup MongoDB
uri = "mongodb+srv://neerajshetkar:29gx0gMglCCyhdff@cluster0.qfkfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["chemar"]

@app.route('/')
def hello_world():
    return 'Hello, World!'
