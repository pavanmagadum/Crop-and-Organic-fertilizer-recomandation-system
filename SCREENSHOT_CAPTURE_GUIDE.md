# Step-by-Step Screenshot Capture Guide
## Practical Instructions for Capturing All Screenshots

**Estimated Total Time:** 60 minutes  
**Last Updated:** December 22, 2025

---

## 🎯 Before You Start

### Prerequisites Checklist:
- [ ] Application is installed and working
- [ ] Virtual environment is activated
- [ ] Database has sample data (at least 2-3 test users)
- [ ] Screenshot tool is ready (Windows Snipping Tool: Win + Shift + S)
- [ ] Folder structure is created

### Quick Setup:
```bash
# 1. Navigate to project
cd c:\Users\sw\Desktop\climate_aware_final_project

# 2. Activate virtual environment
venv\Scripts\activate

# 3. Start the application
streamlit run app\app.py
```

The application should open in your browser at: `http://localhost:8501`

---

## 📸 PART 1: User Interface Screenshots (30 minutes)

### Screenshot 1: User Login Screen
**Time:** 2 minutes  
**File Name:** `07_user_login_screen.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. Open browser to: `http://localhost:8501`
2. Wait for page to fully load
3. Make sure you see "Login to Your Account" header
4. Press `Win + Shift + S` (Windows Snipping Tool)
5. Select rectangular snip
6. Capture the entire login card (including background gradient)
7. Save as: `docs\screenshots\ui\07_user_login_screen.png`

**What Should Be Visible:**
- ✅ "Login to Your Account" header (white text)
- ✅ Username input field
- ✅ Password input field
- ✅ "SIGN IN" button
- ✅ "Forgot Password?" link
- ✅ "Sign Up" button
- ✅ Animated gradient background

**Caption for IEEE Paper:**
```
Figure X: User login interface featuring a clean, modern design with gradient 
background animation. The system provides secure authentication for farmers and 
agricultural experts with password recovery options.
```

---

### Screenshot 2: User Registration Screen
**Time:** 3 minutes  
**File Name:** `13_user_registration.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. On the login page, click "Sign Up" button
2. Wait for registration form to appear
3. Fill in sample data (optional, for better screenshot):
   - Username: `demo_farmer`
   - Password: `Demo@123`
   - Role: Select "Farmer"
4. Press `Win + Shift + S`
5. Capture the registration form
6. Save as: `docs\screenshots\ui\13_user_registration.png`

**What Should Be Visible:**
- ✅ "Create New Account" header
- ✅ Username field (with sample data)
- ✅ Password field
- ✅ Role dropdown (showing "Farmer" selected)
- ✅ "CREATE ACCOUNT" button
- ✅ "Already have an account? Sign In" link

**Caption:**
```
Figure X: User registration interface with role selection capability. New users 
can register as either farmers or agricultural experts, enabling role-based 
access to appropriate features.
```

---

### Screenshot 3: Farmer Dashboard - Main View
**Time:** 3 minutes  
**File Name:** `08_farmer_dashboard_main.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. If not already logged in, login with farmer credentials
2. You should see the main dashboard
3. Make sure sidebar is visible with all navigation options
4. Press `Win + Shift + S`
5. Capture the entire dashboard (sidebar + main content)
6. Save as: `docs\screenshots\ui\08_farmer_dashboard_main.png`

**What Should Be Visible:**
- ✅ Welcome message with username
- ✅ Sidebar with navigation options:
  - 🌾 Crop Recommendation
  - 🧪 Fertilizer Recommendation
  - 🌦️ Weather Forecast
  - 🌱 Organic Conversion
  - 📚 Community
  - 📖 History
- ✅ Main content area
- ✅ Logout button

**Caption:**
```
Figure X: Farmer dashboard main interface showing the navigation sidebar with 
access to crop recommendation, fertilizer analysis, weather forecasting, organic 
conversion, community features, and prediction history.
```

---

### Screenshot 4: Crop Recommendation - Input Form
**Time:** 4 minutes  
**File Name:** `01_crop_recommendation_input.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. Click on "🌾 Crop Recommendation" in sidebar
2. Fill in sample data for better screenshot:
   - **Soil Parameters:**
     - Nitrogen (N): 90
     - Phosphorus (P): 42
     - Potassium (K): 43
     - pH Level: 6.5
   - **Climate Parameters:**
     - Temperature: 25°C
     - Humidity: 80%
     - Rainfall: 200mm
3. **DO NOT CLICK "Get Recommendation" YET**
4. Press `Win + Shift + S`
5. Capture the entire form with filled data
6. Save as: `docs\screenshots\ui\01_crop_recommendation_input.png`

**What Should Be Visible:**
- ✅ "Crop Recommendation" header
- ✅ All soil parameter inputs with values
- ✅ All climate parameter inputs with values
- ✅ "Get Recommendation" button (not clicked yet)
- ✅ Input field labels clearly visible

**Caption:**
```
Figure X: Crop recommendation input interface showing soil parameters (Nitrogen, 
Phosphorus, Potassium, pH) and climate data (Temperature, Humidity, Rainfall). 
The system accepts real-time sensor data or manual input from farmers.
```

---

### Screenshot 5: Crop Recommendation - Result
**Time:** 2 minutes  
**File Name:** `02_crop_recommendation_result.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. With the form still filled from previous step, click "Get Recommendation"
2. Wait for result to appear (should take 1-2 seconds)
3. Press `Win + Shift + S`
4. Capture the result display
5. Save as: `docs\screenshots\ui\02_crop_recommendation_result.png`

**What Should Be Visible:**
- ✅ Recommended crop name (e.g., "RICE")
- ✅ Crop duration (e.g., "120 days")
- ✅ Confidence score or probability (if displayed)
- ✅ Any additional crop information
- ✅ Result card with styling

**Caption:**
```
Figure X: Crop recommendation result displaying the predicted crop (Rice) with 
estimated growth duration (120 days). The machine learning model provides 
recommendations based on soil composition and climate conditions.
```

---

### Screenshot 6: Fertilizer Recommendation
**Time:** 4 minutes  
**File Name:** `12_fertilizer_recommendation.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. Click on "🧪 Fertilizer Recommendation" in sidebar
2. Fill in sample data:
   - Nitrogen: 30
   - Phosphorus: 50
   - Potassium: 40
   - Crop Type: Rice (or select from dropdown)
   - Soil Type: Loamy (if available)
3. Click "Get Recommendation"
4. Wait for result
5. Press `Win + Shift + S`
6. Capture both input form and result
7. Save as: `docs\screenshots\ui\12_fertilizer_recommendation.png`

**What Should Be Visible:**
- ✅ Input form with parameters
- ✅ Recommended fertilizer type
- ✅ NPK values
- ✅ Dosage recommendations
- ✅ Application instructions (if available)

**Caption:**
```
Figure X: Fertilizer recommendation interface showing NPK-based analysis and 
recommended fertilizer type with application guidelines for optimal crop nutrition.
```

---

### Screenshot 7: Organic Fertilizer Conversion
**Time:** 5 minutes  
**File Name:** `03_organic_conversion_complete.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. Click on "🌱 Organic Conversion" in sidebar
2. Fill in sample data:
   - Fertilizer Name: Urea
   - Nitrogen (N): 46%
   - Phosphorus (P): 0%
   - Potassium (K): 0%
   - Quantity: 100 kg
3. Click "Convert to Organic"
4. Wait for conversion results
5. Scroll to see complete result (including pie chart if available)
6. Press `Win + Shift + S`
7. Capture the entire result section
8. Save as: `docs\screenshots\ui\03_organic_conversion_complete.png`

**What Should Be Visible:**
- ✅ Original fertilizer details
- ✅ Organic alternative ingredients list
- ✅ Ingredient quantities
- ✅ Pie chart visualization (if available)
- ✅ Preparation instructions
- ✅ Application guidelines

**Caption:**
```
Figure X: Organic fertilizer conversion engine displaying alternative organic 
ingredients to replace synthetic fertilizers. The system calculates ingredient 
ratios and provides preparation instructions, promoting sustainable farming practices.
```

---

### Screenshot 8: Weather Forecast
**Time:** 3 minutes  
**File Name:** `10_weather_forecast.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. Click on "🌦️ Weather Forecast" in sidebar
2. Enter location or use current location
3. Wait for forecast to load
4. Press `Win + Shift + S`
5. Capture the forecast display
6. Save as: `docs\screenshots\ui\10_weather_forecast.png`

**What Should Be Visible:**
- ✅ Location name
- ✅ Current weather conditions
- ✅ 7-14 day forecast
- ✅ Temperature, humidity, rainfall data
- ✅ Weather icons
- ✅ Climate-aware farming tips (if available)

**Caption:**
```
Figure X: Weather forecast interface providing 7-14 day climate predictions 
integrated with OpenWeatherMap API. The system offers climate-aware farming 
recommendations based on upcoming weather conditions.
```

---

### Screenshot 9: Community Platform
**Time:** 3 minutes  
**File Name:** `09_community_platform.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. Click on "📚 Community" in sidebar
2. You should see posts feed or Q&A section
3. If no posts exist, create 1-2 sample posts first
4. Press `Win + Shift + S`
5. Capture the community interface
6. Save as: `docs\screenshots\ui\09_community_platform.png`

**What Should Be Visible:**
- ✅ Community posts or questions list
- ✅ Post titles, authors, timestamps
- ✅ Like/comment counts (if available)
- ✅ "Create New Post" or "Ask Question" button
- ✅ Modern card-based layout

**Caption:**
```
Figure X: Community platform interface enabling knowledge sharing among farmers 
and agricultural experts. Users can post questions, share experiences, and 
engage in discussions about farming practices.
```

---

### Screenshot 10: Expert Sessions
**Time:** 2 minutes  
**File Name:** `14_expert_sessions.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. In Community section, navigate to "Sessions" tab (if available)
2. If sessions exist, they should be displayed
3. Press `Win + Shift + S`
4. Capture the sessions list
5. Save as: `docs\screenshots\ui\14_expert_sessions.png`

**What Should Be Visible:**
- ✅ List of upcoming expert sessions
- ✅ Session titles
- ✅ Expert names
- ✅ Scheduled times
- ✅ Meeting links
- ✅ "Join Session" buttons

**Caption:**
```
Figure X: Expert sessions scheduling interface showing upcoming educational 
sessions conducted by agricultural experts. Farmers can join virtual meetings 
for real-time guidance and training.
```

---

### Screenshot 11: User History
**Time:** 2 minutes  
**File Name:** `15_user_history.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. Click on "📖 History" in sidebar
2. You should see past predictions (from earlier screenshots)
3. Press `Win + Shift + S`
4. Capture the history view
5. Save as: `docs\screenshots\ui\15_user_history.png`

**What Should Be Visible:**
- ✅ List of past predictions
- ✅ Timestamps
- ✅ Input parameters used
- ✅ Results obtained
- ✅ "View Details" options (if available)

**Caption:**
```
Figure X: Prediction history interface displaying past crop and fertilizer 
recommendations with timestamps and input parameters, enabling farmers to 
track and review their farming decisions.
```

---

## 🔐 PART 2: Admin Panel Screenshots (20 minutes)

### Screenshot 12: Admin Login Screen
**Time:** 2 minutes  
**File Name:** `06_admin_login_screen.png`  
**Save To:** `docs\screenshots\ui\`

**Steps:**
1. **IMPORTANT:** Logout from farmer account first
2. Open new browser tab or window
3. Navigate to: `http://localhost:8501?admin=true`
4. Wait for admin login page to load
5. You should see yellow "ADMIN LOGIN" header with shield icon
6. Press `Win + Shift + S`
7. Capture the admin login interface
8. Save as: `docs\screenshots\ui\06_admin_login_screen.png`

**What Should Be Visible:**
- ✅ 🔐 Shield icon
- ✅ "ADMIN LOGIN" header (bright yellow, bold)
- ✅ "Authorized Access Only" subtitle
- ✅ Username field
- ✅ Password field
- ✅ "SIGN IN" button
- ✅ Security warning message
- ✅ Green gradient background (different from user login)

**Caption:**
```
Figure X: Admin login interface with enhanced security features. The admin 
portal is accessible only via URL parameter (?admin=true) and authenticates 
against environment variables rather than database, providing an additional 
security layer.
```

---

### Screenshot 13: Admin Dashboard Overview
**Time:** 3 minutes  
**File Name:** `04_admin_dashboard_overview.png`  
**Save To:** `docs\screenshots\admin\`

**Steps:**
1. Login with admin credentials:
   - Username: `admin`
   - Password: `Admin@2025` (or your ADMIN_PASSWORD from .env)
2. You should see the admin control panel with 4 tabs
3. Make sure all tabs are visible
4. Press `Win + Shift + S`
5. Capture the entire admin dashboard
6. Save as: `docs\screenshots\admin\04_admin_dashboard_overview.png`

**What Should Be Visible:**
- ✅ "🔐 Admin Control Panel" header
- ✅ Four tabs clearly visible:
  - 👥 User Management
  - 📊 System Analytics
  - 📰 Content Management
  - 🎓 Sessions Management
- ✅ Professional admin interface design

**Caption:**
```
Figure X: Admin control panel overview showing the four main administrative 
modules: User Management, System Analytics, Content Management, and Sessions 
Management. The centralized dashboard provides comprehensive system control.
```

---

### Screenshot 14: Admin User Management
**Time:** 4 minutes  
**File Name:** `05_admin_user_management.png`  
**Save To:** `docs\screenshots\admin\`

**Steps:**
1. Click on "👥 User Management" tab
2. You should see list of all registered users
3. Make sure at least 2-3 users are visible
4. Press `Win + Shift + S`
5. Capture the user management interface
6. Save as: `docs\screenshots\admin\05_admin_user_management.png`

**What Should Be Visible:**
- ✅ Total user count
- ✅ User list with:
  - User ID numbers
  - Usernames
  - Role badges (color-coded: green for farmers, blue for experts)
  - "Change Role" dropdown for each user
  - "Update" button
  - "🗑️ Delete" button
- ✅ Clean table layout

**Caption:**
```
Figure X: Admin user management interface displaying all registered users with 
role-based badges. Administrators can modify user roles and delete accounts 
through inline controls, ensuring efficient user administration.
```

---

### Screenshot 15: Admin System Analytics
**Time:** 3 minutes  
**File Name:** `11_admin_system_analytics.png`  
**Save To:** `docs\screenshots\admin\`

**Steps:**
1. Click on "📊 System Analytics" tab
2. You should see metric cards with statistics
3. Press `Win + Shift + S`
4. Capture the analytics dashboard
5. Save as: `docs\screenshots\admin\11_admin_system_analytics.png`

**What Should Be Visible:**
- ✅ Metric cards showing:
  - Total Users (with gradient background)
  - Total Posts
  - Total Questions
  - Total Predictions
- ✅ User role distribution:
  - Farmers count
  - Experts count
- ✅ Visual styling with gradients

**Caption:**
```
Figure X: System analytics dashboard providing real-time statistics on user 
registrations, community engagement, and system usage. The metrics enable 
administrators to monitor platform growth and user activity.
```

---

### Screenshot 16: Admin Content Management
**Time:** 4 minutes  
**File Name:** `16_admin_content_management.png`  
**Save To:** `docs\screenshots\admin\`

**Steps:**
1. Click on "📰 Content Management" tab
2. You should see posts and questions sections
3. If no content exists, create 1-2 sample posts first (from farmer account)
4. Press `Win + Shift + S`
5. Capture the content management interface
6. Save as: `docs\screenshots\admin\16_admin_content_management.png`

**What Should Be Visible:**
- ✅ Community Posts section with:
  - Post titles
  - Authors
  - Timestamps
  - "🗑️ Delete Post" buttons
- ✅ Questions section with:
  - Question titles
  - Authors
  - View/save counts
  - "🗑️ Delete Question" buttons
- ✅ Expandable post/question details

**Caption:**
```
Figure X: Content management interface enabling administrators to moderate 
community posts and questions. The system provides content oversight capabilities 
to maintain quality and appropriateness of user-generated content.
```

---

### Screenshot 17: Admin Sessions Management
**Time:** 4 minutes  
**File Name:** `17_admin_sessions_management.png`  
**Save To:** `docs\screenshots\admin\`

**Steps:**
1. Click on "🎓 Sessions Management" tab
2. You should see session creation form
3. Optionally, fill in sample session data:
   - Session Title: "Organic Farming Best Practices"
   - Meeting Link: "https://meet.google.com/abc-defg-hij"
   - Scheduled Time: "December 25, 2025 at 3:00 PM"
   - Expert Name: "Dr. Agricultural Expert"
4. Press `Win + Shift + S`
5. Capture both the form and existing sessions list
6. Save as: `docs\screenshots\admin\17_admin_sessions_management.png`

**What Should Be Visible:**
- ✅ "Create New Session" form with:
  - Session Title field
  - Meeting Link field
  - Scheduled Time field
  - Expert Name field
  - "Create Session" button
- ✅ "Existing Sessions" list (if any sessions exist)

**Caption:**
```
Figure X: Sessions management interface allowing administrators to schedule 
expert-led educational sessions. The system integrates with video conferencing 
platforms (Zoom, Google Meet) for virtual farmer training programs.
```

---

## ✅ PART 3: Verification & Organization (10 minutes)

### Step 1: Verify All Screenshots
Check that you have captured all files:

**UI Screenshots (11 files):**
- [ ] `01_crop_recommendation_input.png`
- [ ] `02_crop_recommendation_result.png`
- [ ] `03_organic_conversion_complete.png`
- [ ] `06_admin_login_screen.png`
- [ ] `07_user_login_screen.png`
- [ ] `08_farmer_dashboard_main.png`
- [ ] `09_community_platform.png`
- [ ] `10_weather_forecast.png`
- [ ] `12_fertilizer_recommendation.png`
- [ ] `13_user_registration.png`
- [ ] `14_expert_sessions.png`
- [ ] `15_user_history.png`

**Admin Screenshots (5 files):**
- [ ] `04_admin_dashboard_overview.png`
- [ ] `05_admin_user_management.png`
- [ ] `11_admin_system_analytics.png`
- [ ] `16_admin_content_management.png`
- [ ] `17_admin_sessions_management.png`

### Step 2: Check Image Quality
For each screenshot, verify:
- [ ] Image is clear and not blurry
- [ ] Resolution is at least 1920x1080
- [ ] All text is readable
- [ ] No sensitive information is visible
- [ ] File size is reasonable (< 5MB)

### Step 3: Organize Files
Make sure files are in correct folders:
```
docs\screenshots\ui\        → 12 files
docs\screenshots\admin\     → 5 files
```

---

## 📝 Next Steps

After capturing all screenshots:

1. **Create Diagrams** (see `DIAGRAM_TEMPLATES.md`)
   - Database Schema (15 min)
   - Authentication Flow (20 min)
   - Crop Recommendation Workflow (15 min)
   - Organic Conversion Workflow (10 min)

2. **Prepare Captions**
   - Copy captions from this guide
   - Adjust figure numbers sequentially
   - Add to IEEE paper draft

3. **Update Progress**
   - Mark completed items in `SCREENSHOTS_INDEX.md`
   - Update completion percentage

---

## 🆘 Troubleshooting

### Issue: Admin login not showing yellow theme
**Solution:** Make sure you're accessing `?admin=true` URL parameter

### Issue: No data in community/history
**Solution:** Create sample data first:
- Register 2-3 test users
- Make 2-3 crop predictions
- Create 2-3 community posts

### Issue: Screenshot too large
**Solution:** Use image compression:
- Windows: Right-click → Edit with Photos → Resize
- Online: tinypng.com

### Issue: Can't see full page
**Solution:** 
- Zoom out browser (Ctrl + Mouse Wheel)
- Or take multiple screenshots and stitch together

---

## ✨ Pro Tips

1. **Consistency:** Use same browser window size for all screenshots
2. **Timing:** Capture screenshots when UI is fully loaded
3. **Data:** Use realistic sample data for better screenshots
4. **Annotations:** Add arrows/highlights later if needed
5. **Backup:** Keep original screenshots before editing

---

**Estimated Total Time:** 60 minutes  
**Difficulty:** Easy  
**Required Tools:** Browser + Windows Snipping Tool

**Good luck! 🚀**
