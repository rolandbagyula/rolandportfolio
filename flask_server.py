#!/usr/bin/env python3
"""
Flask Development Server for Roland's Portfolio
Combines static file serving with dynamic backend features
"""

from flask import Flask, render_template_string, request, jsonify, send_from_directory
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-app-password'     # Replace with app password

mail = Mail(app)

@app.route('/')
def index():
    """Serve the main portfolio page"""
    return send_from_directory('.', 'index.html')

@app.route('/blog.html')
def blog():
    """Serve the blog page"""
    return send_from_directory('.', 'blog.html')

@app.route('/react-hooks-tutorial.html')
def tutorial():
    """Serve the tutorial page"""
    return send_from_directory('.', 'react-hooks-tutorial.html')

@app.route('/styles.css')
def styles():
    """Serve CSS with proper content type"""
    return send_from_directory('.', 'styles.css', mimetype='text/css')

@app.route('/script.js')
def script():
    """Serve JavaScript with proper content type"""
    return send_from_directory('.', 'script.js', mimetype='application/javascript')

@app.route('/<path:filename>')
def static_files(filename):
    """Serve static files (images, etc.)"""
    return send_from_directory('.', filename)

@app.route('/api/contact', methods=['POST'])
def contact_form():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        if not all([name, email, message]):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Create email message
        msg = Message(
            subject=f'Portfolio Contact: {name}',
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],
            body=f"""
New contact form submission:

Name: {name}
Email: {email}
Message: {message}
            """
        )
        
        # Send email (uncomment when email is configured)
        # mail.send(msg)
        
        # For now, just log the message
        print(f"Contact form submission from {name} ({email}): {message}")
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
        
    except Exception as e:
        print(f"Error processing contact form: {e}")
        return jsonify({'error': 'Server error'}), 500

@app.route('/api/status')
def status():
    """API endpoint to check server status"""
    return jsonify({
        'status': 'running',
        'message': 'Flask server is working!',
        'features': [
            'Static file serving',
            'Contact form handling',
            'Email integration ready',
            'API endpoints'
        ]
    })

if __name__ == '__main__':
    print("Starting Roland Portfolio Server...")
    print("Features available:")
    print("   - Static file serving (HTML, CSS, JS)")
    print("   - Contact form backend (/api/contact)")
    print("   - Server status API (/api/status)")
    print("   - Email integration (configure MAIL_* settings)")
    print()
    print("Open: http://localhost:5000")
    print("Development mode with auto-reload")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
