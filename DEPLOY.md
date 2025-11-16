# Campus Care - Deployment Guide

This guide covers multiple deployment options to get your Campus Care application live on the internet.

---

## Option 1: Deploy on Render (Recommended - Free & Easy)

### Backend Deployment on Render

1. **Prepare your project:**
   - Create a `requirements.txt` file:
     ```
     Flask==3.1.2
     Flask-CORS==6.0.1
     Werkzeug==3.1.3
     gunicorn==21.2.0
     ```

2. **Create a `render.yaml` or use Render Dashboard:**
   - Go to [render.com](https://render.com) and sign up
   - Click "New +" → "Web Service"
   - Connect your GitHub repository (push your code to GitHub first)
   - Configure:
     - **Name:** campuscare-backend
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn campuscare:app`
   - Click "Create Web Service"

3. **Initialize database:**
   - After deployment, go to Shell tab in Render dashboard
   - Run: `python init_db.py`

4. **Note your backend URL:** `https://campuscare-backend.onrender.com`

### Frontend Deployment

**Option A: Netlify (Easiest)**
1. Go to [netlify.com](https://netlify.com) and sign up
2. Drag and drop your frontend files (HTML, CSS, JS, images)
3. Update `booking.js` - replace `http://localhost:5000` with your Render backend URL
4. Your site is live!

**Option B: Vercel**
1. Go to [vercel.com](https://vercel.com) and sign up
2. Import your project from GitHub
3. Deploy - it's automatic!

---

## Option 2: Deploy on PythonAnywhere (Free Tier Available)

### Steps:

1. **Sign up at [pythonanywhere.com](https://pythonanywhere.com)**

2. **Upload your files:**
   - Go to Files tab
   - Upload all Python files, database, etc.

3. **Install dependencies:**
   - Go to Consoles → Bash
   - Run:
     ```bash
     pip3 install --user flask flask-cors werkzeug
     python3 init_db.py
     ```

4. **Configure Web App:**
   - Go to Web tab → Add a new web app
   - Choose Flask
   - Set source code path: `/home/yourusername/campuscare.py`
   - Edit WSGI file to point to your app
   - Reload the web app

5. **Update CORS settings in `campuscare.py`:**
   ```python
   CORS(app, origins=["https://yourusername.pythonanywhere.com"])
   ```

6. **Deploy frontend:**
   - Use Netlify/Vercel for frontend
   - Update `booking.js` with PythonAnywhere URL

---

## Option 3: Deploy on Heroku

### Backend on Heroku:

1. **Create required files:**

   **Procfile:**
   ```
   web: gunicorn campuscare:app
   ```

   **requirements.txt:**
   ```
   Flask==3.1.2
   Flask-CORS==6.0.1
   Werkzeug==3.1.3
   gunicorn==21.2.0
   ```

   **runtime.txt:**
   ```
   python-3.12.0
   ```

2. **Deploy:**
   ```bash
   heroku login
   heroku create campuscare-backend
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   heroku run python init_db.py
   ```

3. **Get your app URL:** `https://campuscare-backend.herokuapp.com`

---

## Option 4: Deploy on Railway

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-detects Python and deploys
6. Add environment variables if needed
7. Get your deployment URL

---

## Important: Update Frontend URLs

After deploying backend, update `booking.js`:

```javascript
// Change this line:
const response = await fetch('http://localhost:5000/consultation', {

// To your deployed backend URL:
const response = await fetch('https://your-backend-url.com/consultation', {
```

---

## Database Considerations

### For Production:

**SQLite (Current):** Good for small projects, but has limitations

**Upgrade to PostgreSQL (Recommended for production):**

1. Install psycopg2: `pip install psycopg2-binary`

2. Update `campuscare.py`:
   ```python
   import psycopg2
   from psycopg2.extras import RealDictCursor
   
   DATABASE_URL = os.environ.get('DATABASE_URL')
   
   def get_db_connection():
       conn = psycopg2.connect(DATABASE_URL)
       return conn
   ```

3. Most hosting platforms (Render, Railway, Heroku) offer free PostgreSQL databases

---

## Environment Variables

For production, use environment variables for sensitive data:

```python
import os

app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key')
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
```

Set these in your hosting platform's dashboard.

---

## SSL/HTTPS

Most modern hosting platforms (Netlify, Vercel, Render) provide free SSL certificates automatically.

For VPS, use Let's Encrypt:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## Testing Your Deployment

1. Visit your frontend URL
2. Fill out the consultation form
3. Check if data is saved (use `/consultations` endpoint)
4. Monitor logs for errors

---

## Troubleshooting

**CORS Errors:**
- Update CORS settings in `campuscare.py` to include your frontend domain
- Example: `CORS(app, origins=["https://your-frontend.netlify.app"])`

**Database Errors:**
- Ensure `init_db.py` was run on the server
- Check file permissions for SQLite database

**500 Internal Server Error:**
- Check server logs
- Verify all dependencies are installed
- Ensure environment variables are set

---

## Recommended Stack for Beginners

✅ **Backend:** Render (Free tier, auto-deploys from GitHub)
✅ **Frontend:** Netlify (Free, drag-and-drop deployment)
✅ **Database:** SQLite (for start) → PostgreSQL (for scale)

**Total Cost:** $0 (Free tier)
**Setup Time:** 15-30 minutes

---

## Quick Start Deployment Checklist

- [ ] Push code to GitHub
- [ ] Create `requirements.txt`
- [ ] Deploy backend on Render
- [ ] Run `init_db.py` on server
- [ ] Update `booking.js` with backend URL
- [ ] Deploy frontend on Netlify
- [ ] Test the form submission
- [ ] Monitor for errors

---

## Need Help?

- Render Docs: https://render.com/docs
- Netlify Docs: https://docs.netlify.com
- Flask Deployment: https://flask.palletsprojects.com/en/latest/deploying/

Good luck with your deployment! 🚀
