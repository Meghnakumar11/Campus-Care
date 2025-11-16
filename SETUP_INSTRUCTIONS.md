# Campus Care - Frontend & Backend Setup

## Setup Complete! ✅

Your consultation form is now connected to the Python backend.

## What Was Done:

1. **Frontend (campuscare.html)**: Added proper form IDs and connected booking.js
2. **JavaScript (booking.js)**: Updated to handle form submission with proper error handling
3. **Backend (campuscare.py)**: Added `/consultation` endpoint to receive form data
4. **Database (init_db.py)**: Added `consultations` table to store booking requests

## How to Run:

### Step 1: Initialize the Database
```bash
python init_db.py
```

### Step 2: Start the Backend Server
```bash
python campuscare.py
```
The server will run on `http://localhost:5000`

### Step 3: Open the Frontend
Open `campuscare.html` in your browser (double-click or use a local server)

## Testing the Form:

1. Navigate to the "Book a Consultation" section
2. Fill in all fields:
   - Full Name
   - Roll Number
   - Email
   - Service Type
   - Concern Description
3. Click "Request Appointment"
4. You should see a success message!

## API Endpoints:

- `POST /consultation` - Submit consultation request
- `GET /consultations` - View all consultation requests
- `POST /signup` - User registration
- `POST /login` - User login
- `POST /logout` - User logout
- `POST /feedback` - Submit feedback
- `GET /myfeedback` - View user's feedback

## Database Tables:

- `users` - User accounts
- `feedback` - User feedback
- `consultations` - Consultation booking requests

## Troubleshooting:

- If you get CORS errors, make sure Flask-CORS is installed: `pip install flask-cors`
- If database errors occur, delete `database.db` and run `init_db.py` again
- Make sure the backend is running before submitting the form
