import os
import csv
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-secret')

DATA_DIR = 'data'
APPLICATIONS_CSV = os.path.join(DATA_DIR, 'applications.csv')
CONTACTS_CSV = os.path.join(DATA_DIR, 'contacts.csv')

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def ensure_csv_headers():
    ensure_data_dir()
    
    if not os.path.exists(APPLICATIONS_CSV):
        with open(APPLICATIONS_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'timestamp', 'first_name', 'last_name', 'dob', 'email', 'phone',
                'academic_qualification', 'service_documents', 'guarantor_name',
                'guarantor_occupation', 'consent'
            ])
    
    if not os.path.exists(CONTACTS_CSV):
        with open(CONTACTS_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'name', 'email', 'message'])

ensure_csv_headers()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/loan-products')
def loan_products():
    return render_template('loan_products.html')

@app.route('/requirements')
def requirements():
    return render_template('requirements.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        dob = request.form.get('dob', '').strip()
        phone = request.form.get('phone', '').strip()
        email = request.form.get('email', '').strip()
        academic_qualification = request.form.get('academic_qualification', '').strip()
        service_documents = request.form.get('service_documents', '').strip()
        guarantor_name = request.form.get('guarantor_name', '').strip()
        guarantor_occupation = request.form.get('guarantor_occupation', '').strip()
        consent = request.form.get('consent', '')
        
        if not all([first_name, last_name, dob, phone, email]):
            flash('Please fill in all required fields.', 'error')
            return render_template('apply.html', form_data=request.form)
        
        if '@' not in email or '.' not in email:
            flash('Please enter a valid email address.', 'error')
            return render_template('apply.html', form_data=request.form)
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open(APPLICATIONS_CSV, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                timestamp, first_name, last_name, dob, email, phone,
                academic_qualification, service_documents, guarantor_name,
                guarantor_occupation, consent
            ])
        
        return redirect(url_for('thank_you'))
    
    return render_template('apply.html', form_data={})

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        if not all([name, email, message]):
            flash('Please fill in all required fields.', 'error')
            return render_template('contact.html', form_data=request.form)
        
        if '@' not in email or '.' not in email:
            flash('Please enter a valid email address.', 'error')
            return render_template('contact.html', form_data=request.form)
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open(CONTACTS_CSV, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, name, email, message])
        
        return redirect(url_for('thank_you'))
    
    return render_template('contact.html', form_data={})

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
