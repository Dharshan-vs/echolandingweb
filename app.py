from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import csv
import os
from datetime import datetime
import pandas as pd

app = Flask(__name__)
CORS(app)

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Initialize CSV files with headers if they don't exist
def init_csv_files():
    # Contact form data
    contact_file = 'data/contact_submissions.csv'
    if not os.path.exists(contact_file):
        with open(contact_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Name', 'Email', 'Message'])
    
    # Newsletter subscriptions
    newsletter_file = 'data/newsletter_subscriptions.csv'
    if not os.path.exists(newsletter_file):
        with open(newsletter_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Email'])

# Initialize CSV files on startup
init_csv_files()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not email or not message:
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        # Save to CSV
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('data/contact_submissions.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, name, email, message])
        
        # Also save to Excel format
        try:
            df = pd.read_csv('data/contact_submissions.csv')
            df.to_excel('data/contact_submissions.xlsx', index=False)
        except Exception as e:
            print(f"Error creating Excel file: {e}")
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
    
    except Exception as e:
        print(f"Error processing contact form: {e}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'}), 500

@app.route('/subscribe-newsletter', methods=['POST'])
def subscribe_newsletter():
    try:
        data = request.get_json()
        email = data.get('email', '').strip()
        
        if not email:
            return jsonify({'success': False, 'message': 'Email is required'}), 400
        
        # Check if email already exists
        with open('data/newsletter_subscriptions.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            existing_emails = [row[1] for row in reader]
        
        if email in existing_emails:
            return jsonify({'success': False, 'message': 'Email already subscribed!'}), 400
        
        # Save to CSV
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('data/newsletter_subscriptions.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, email])
        
        return jsonify({'success': True, 'message': 'Successfully subscribed to newsletter!'})
    
    except Exception as e:
        print(f"Error processing newsletter subscription: {e}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'}), 500

@app.route('/get-data', methods=['GET'])
def get_data():
    try:
        data_type = request.args.get('type', 'contact')
        
        if data_type == 'contact':
            file_path = 'data/contact_submissions.csv'
        elif data_type == 'newsletter':
            file_path = 'data/newsletter_subscriptions.csv'
        else:
            return jsonify({'error': 'Invalid data type'}), 400
        
        if not os.path.exists(file_path):
            return jsonify({'data': []})
        
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        return jsonify({'data': data})
    
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return jsonify({'error': 'An error occurred while retrieving data'}), 500

if __name__ == '__main__':
    print("Starting ECHO Web Server...")
    print("Contact form data will be saved to: data/contact_submissions.csv and data/contact_submissions.xlsx")
    print("Newsletter subscriptions will be saved to: data/newsletter_subscriptions.csv")
    print("Server running at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
