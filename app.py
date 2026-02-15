from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/security-dashboard')
def dashboard():
    # S4 Security Metrics
    data = {
        'Critical Vulns': 0,
        'High': 2,
        'Medium': 5,
        'Low': 12,
        'S4 Score': '98.5%',
        'Compliance': 'SOC2, ISO27001, PCI-DSS'
    }
    
    fig = px.pie(
        values=[data['Critical Vulns'], data['High'], data['Medium'], data['Low']],
        names=['Critical', 'High', 'Medium', 'Low'],
        title='S4 Vulnerability Distribution'
    )
    
    return render_template('dashboard.html', data=data, plot=fig.to_html())