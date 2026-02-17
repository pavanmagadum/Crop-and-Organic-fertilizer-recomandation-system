# 🚀 DEPLOYMENT GUIDE: Fast & Reliable Deployment

## Quick Start (5 minutes)

### Local Development
```bash
# 1. Start the app
cd c:\Users\sw\Desktop\climate_aware_final_project
venv\Scripts\streamlit run app\app.py

# 2. Open browser
http://localhost:8502
```

---

## 🚀 DEPLOYMENT OPTIONS (Recommended Order)

### Option 1: Railway (⭐ BEST FOR STREAMLIT)
**Fastest setup, free tier available, persistent storage**

#### Step 1: Connect Repository
```bash
# 1. Go to https://railway.app
# 2. Click "New Project"
# 3. Select "Deploy from GitHub repo"
# 4. Authorize and select: crop-and-organic-fertilizer-recommendation-system
```

#### Step 2: Set Environment Variables
In Railway Dashboard → Variables:
```
ADMIN_PASSWORD=Admin@2025
DATABASE_TYPE=sqlite
PYTHONUNBUFFERED=1
```

#### Step 3: Deploy
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway up
```

**Your app will be live at:** `https://your-app.railway.app`

---

### Option 2: Docker + Railway
**Faster, optimized deployment**

```bash
# 1. Build Docker image
docker build -t climate-app .

# 2. Tag for Railway
docker tag climate-app:latest registry.railway.app/climate-app:latest

# 3. Push to Railway
docker push registry.railway.app/climate-app:latest

# 4. Deploy in Railway Dashboard
# → Select Docker image
# → Set PORT=8502
# → Deploy
```

---

### Option 3: Docker + Render
**Alternative, free option**

```bash
# 1. Build Docker image
docker build -t climate-app .

# 2. Push to Docker Hub
docker tag climate-app:latest yourname/climate-app:latest
docker push yourname/climate-app:latest

# 3. Go to https://render.com
# 4. Create new Web Service
# 5. Use image: yourname/climate-app:latest
# 6. Set PORT=8502
# 7. Deploy
```

---

### Option 4: Docker Compose (Local/VPS)
**For self-hosted deployment**

```bash
# 1. Start with Docker Compose
docker-compose up -d

# 2. Check status
docker-compose ps

# 3. View logs
docker-compose logs -f climate-app

# 4. Stop
docker-compose down
```

---

## ⚡ PERFORMANCE OPTIMIZATIONS (Already Applied)

✅ **Fixed Navigation Buttons** - Proportional layout
✅ **Caching System** - @st.cache_data decorators  
✅ **Multi-threading** - ThreadPoolExecutor with 20 workers
✅ **Async Tasks** - Background processing
✅ **Health Checks** - Docker health monitoring
✅ **CI/CD Pipeline** - Automated testing & deployment

---

## 🛡️ KEEP-ALIVE (Prevent Sleep)

### Method 1: UptimeRobot (Free)
```
1. Go to https://uptimerobot.com
2. Create free account
3. Add new monitor
   - Type: HTTPS
   - URL: https://your-app.railway.app
   - Interval: 5 minutes
4. Get alerts if app goes down
```

### Method 2: Built-in Keep-Alive
```python
from src.keep_alive import AppKeepAlive
import os

# In app.py (add after imports)
if 'keep_alive' not in st.session_state:
    app_url = os.getenv('APP_URL', 'http://localhost:8502')
    keep_alive = AppKeepAlive(app_url, interval=300)
    keep_alive.start()
    st.session_state['keep_alive'] = keep_alive
```

---

## 🔄 CI/CD PIPELINE (Already Configured)

Automatic workflow for every push to `main`:

```
┌─────────────────┐
│   Git Push      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Run Tests       │ ← pytest + coverage
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Code Quality    │ ← black, isort, flake8
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Security Scan   │ ← bandit + detect-secrets
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Deploy (main)   │ ← Railway auto-deploy
└─────────────────┘
```

**Status Badge:** [![CI/CD Pipeline](https://github.com/yourname/crop-and-organic-fertilizer-recommendation-system/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/yourname/crop-and-organic-fertilizer-recommendation-system/actions)

---

## 📊 MONITORING & PERFORMANCE

### View Performance Metrics
```python
# In admin dashboard (upcoming feature)
# → System Analytics tab
# → Performance Metrics
# → Response times, cache hits, etc.
```

### Docker Health Check
```bash
# Check container health
docker ps --format "table {{.Names}}\t{{.Status}}"

# View logs
docker logs climate-app -f
```

---

## 🆘 TROUBLESHOOTING

### App won't start?
```bash
# Check logs
docker logs climate-app

# Rebuild
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Slow performance?
```bash
# Check if caching is working
# → Open browser DevTools (F12)
# → Check network tab
# → Should see cached responses

# Monitor threads
# → Check system resources
# → Railway dashboard → Metrics
```

### Database issues?
```bash
# Backup database
cp community/community.db community/community.db.backup

# Reset if needed
rm community/community.db
# App will recreate it on next run
```

---

## 📈 NEXT STEPS FOR EVEN FASTER

1. **Add PostgreSQL** (replace SQLite)
   - Better for concurrent users
   - Edit: community/config.py

2. **Add Redis Caching** (optional)
   - Cache prediction results
   - Faster repeat queries

3. **CDN for Static Files** (Cloudflare)
   - Serve CSS/JS faster
   - Free tier available

4. **Load Balancing** (if needed)
   - Railway handles this automatically

---

## 📞 DEPLOYMENT CHECKLIST

- [ ] Environment variables configured
- [ ] .env file created with ADMIN_PASSWORD
- [ ] Git repository updated and pushed
- [ ] CI/CD pipeline running successfully
- [ ] Docker image builds without errors
- [ ] Railway/Render account created
- [ ] App deployed and accessible
- [ ] UptimeRobot monitor configured
- [ ] Admin login tested
- [ ] Users can register and login
- [ ] Database persisting correctly
- [ ] Performance metrics tracking

---

## 🎯 COMMANDS CHEAT SHEET

```bash
# Local Development
streamlit run app/app.py

# Docker
docker build -t climate-app .
docker run -p 8502:8502 climate-app

# Docker Compose
docker-compose up -d
docker-compose logs -f

# Railway
railway up
railway link
railway run

# Git CI/CD
git add .
git commit -m "feat: production ready deployment"
git push origin main
# → GitHub Actions automatically run tests and deploy
```

---

**Your app is now production-ready and will stay online! 🚀✨**
