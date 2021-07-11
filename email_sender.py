#!/usr/bin/env python3
"""
Author : Gabriel Lilly
Date   : 2021-05-17
Purpose: Send emails
"""

import argparse
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Gabriel Lilly"
email["to"] = "whatemail@gmail.com"
email["subject"] = "You won 1,000,000 dollars!"

email.set_content(html.substitute({"name": "TinTin"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("gabebusiness03@gmail.com", "Nogabe2010")
    smtp.send_message(email)
    print("all good boss!")
