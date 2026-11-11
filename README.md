# SafeRoute – Tourist Safety Management System

## Project Overview
SafeRoute is a Flask-based web application designed to improve tourist safety through location monitoring, emergency assistance, incident reporting, and safe-place information.

## Technologies Used
- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript

## Main Features
- User Registration and Login
- Tourist Dashboard
- Route and Location Monitoring
- Safe Places Information
- Risk Zone Management
- SOS Emergency Assistance
- Emergency Contact Management
- Incident Reporting
- Admin Dashboard
- Feedback Management

## Project Structure
- `app.py` – Main Flask application
- `config.py` – Application and database configuration
- `db.py` – Database connection and query functions
- `schema.sql` – Database structure
- `templates/` – HTML templates
- `static/` – CSS, JavaScript, and images
- `requirements.txt` – Python dependencies

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/randheshruti/SafeRoute-SkillPilot_advanced_day1.git
   ```

2. Open the project folder:
   ```bash
   cd SafeRoute-SkillPilot_advanced_day1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create the MySQL database and import `schema.sql`.

5. Set your database password and secret key as environment variables:
   - `SAFEROUTE_DB_PASSWORD`
   - `SAFEROUTE_SECRET_KEY`

6. Run the application:
   ```bash
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.

## Author
Shruti Randhe

## Project Type
SkillPilot Flask Project Submission