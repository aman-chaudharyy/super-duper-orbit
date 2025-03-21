from django.shortcuts import render
from django.shortcuts import HttpResponse
import os
import subprocess
from datetime import datetime
import pytz

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def htop(request):
    # Get system username

    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get the "top" command output
    top_output = subprocess.getoutput('top -n 1')

    # Replace "your full name" with your actual full name
    full_name = 'Aman Chaudhary'

    return HttpResponse(f"""
        <html>
            <body>
                <h1>System Information</h1>
                <p><strong>Name:</strong> {full_name}</p>
                <p><strong>Username:</strong> aman-chaudharyy</p>
                <p><strong>Server Time (IST):</strong> {server_time}</p>
                <h2>Top Output:</h2>
                <pre>{top_output}</pre>
            </body>
        </html>
    """)