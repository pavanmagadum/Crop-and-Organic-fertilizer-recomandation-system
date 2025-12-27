# Screenshot and Diagram Guide for Documentation
## Climate-Aware Crop & Organic Fertilizer Recommendation System

---

## 📋 Table of Contents
1. [System Architecture Diagrams](#system-architecture-diagrams)
2. [User Interface Screenshots](#user-interface-screenshots)
3. [Admin Panel Screenshots](#admin-panel-screenshots)
4. [Feature Demonstration Screenshots](#feature-demonstration-screenshots)
5. [Database Schema Diagrams](#database-schema-diagrams)
6. [Workflow Diagrams](#workflow-diagrams)
7. [Screenshot Organization Tips](#screenshot-organization-tips)

---

## 🏗️ System Architecture Diagrams

### 1. **Overall System Architecture Diagram**
**File to Use:** `docs/architecture_diagram.png` (already exists)

**What it Shows:**
- Frontend (Streamlit UI)
- Backend (Python Application Layer)
- Machine Learning Models (Crop & Fertilizer Prediction)
- Database Layer (SQLite)
- External APIs (Weather API, Google Custom Search)
- Community Platform Components

**Purpose:** Provides a high-level overview of the entire system architecture showing how different components interact.

**Where to Include:**
- IEEE Paper: Section II (System Architecture)
- Technical Documentation: Architecture Overview
- Project Report: System Design section

---

### 2. **Authentication Flow Diagram**
**Already Exists In:** `ADMIN_TECHNICAL_DOCUMENTATION.md` (Lines 42-80)

**What to Create:**
A visual flowchart showing:
```
User Access → URL Check → Admin Mode? → Admin Login / User Login → Dashboard
```

**Recommended Tool:** Draw.io, Lucidchart, or PowerPoint

**Key Elements to Show:**
- URL parameter detection (`?admin=true`)
- Dual authentication paths (Admin vs User)
- Environment variable validation for admin
- Database validation for users
- Role-based dashboard routing

**Where to Include:**
- IEEE Paper: Security Implementation section
- Admin Documentation
- Technical Documentation

---

### 3. **Component Architecture Diagram**
**Already Exists In:** `ADMIN_TECHNICAL_DOCUMENTATION.md` (Lines 84-112)

**What to Create:**
A layered architecture diagram showing:
- **Application Layer:** Authentication, Admin Dashboard, User Dashboard
- **Database Layer:** Admin Functions, User Functions, Content Management
- **Data Storage Layer:** SQLite, Environment Variables, Session State

**Recommended Format:** Horizontal layered diagram with clear separation

**Where to Include:**
- IEEE Paper: Implementation section
- Technical Documentation
- Developer Guide

---

## 🖥️ User Interface Screenshots

### 4. **Landing Page / Login Screen (User Mode)**
**How to Capture:**
1. Run: `streamlit run app/app.py`
2. Access: `http://localhost:8501`
3. Screenshot the login interface

**What Should Be Visible:**
- "Login to Your Account" header
- Username and Password fields
- "SIGN IN" button
- "Forgot Password?" link
- "Sign Up" button
- Animated gradient background
- Clean, modern UI design

**Purpose:** Shows the user-facing login interface

**Where to Include:**
- IEEE Paper: User Interface section
- Project Report: Frontend Design
- User Manual

---

### 5. **Admin Login Screen**
**How to Capture:**
1. Run: `streamlit run app/app.py`
2. Access: `http://localhost:8501?admin=true`
3. Screenshot the admin login interface

**What Should Be Visible:**
- 🔐 Shield icon
- "ADMIN LOGIN" header (bright yellow, bold)
- "Authorized Access Only" subtitle
- Username and Password fields
- "SIGN IN" button
- Security warning message
- Green gradient background

**Purpose:** Demonstrates the hidden admin access feature

**Where to Include:**
- IEEE Paper: Security Features section
- Admin Documentation
- Technical Documentation

---

### 6. **User Registration Screen**
**How to Capture:**
1. Click "Sign Up" button on login screen
2. Screenshot the registration form

**What Should Be Visible:**
- "Create New Account" header
- Username field
- Password field
- Role selection (Farmer / Agricultural Expert)
- "CREATE ACCOUNT" button
- Form validation indicators

**Purpose:** Shows user onboarding process

**Where to Include:**
- User Manual
- Project Report

---

### 7. **Farmer Dashboard - Main View**
**How to Capture:**
1. Login as a farmer
2. Screenshot the main dashboard

**What Should Be Visible:**
- Welcome message with username
- Navigation sidebar with options:
  - 🌾 Crop Recommendation
  - 🧪 Fertilizer Recommendation
  - 🌦️ Weather Forecast
  - 🌱 Organic Conversion
  - 📚 Community
  - 📖 History
- Main content area
- Modern, responsive design

**Purpose:** Shows the farmer's primary interface

**Where to Include:**
- IEEE Paper: User Interface section
- User Manual
- Project Report

---

### 8. **Crop Recommendation Feature**
**How to Capture:**
1. Navigate to "Crop Recommendation"
2. Fill in soil parameters (N, P, K, pH, etc.)
3. Fill in climate data (Temperature, Humidity, Rainfall)
4. Click "Get Recommendation"
5. Screenshot the results

**What Should Be Visible:**
- Input form with all parameters
- Recommended crop name
- Crop duration display (e.g., "120 days")
- Confidence score or probability
- Additional crop information
- Clean result card design

**Purpose:** Demonstrates the core ML-based crop prediction feature

**Where to Include:**
- IEEE Paper: Results section
- Project Report: Features section
- User Manual

---

### 9. **Fertilizer Recommendation Feature**
**How to Capture:**
1. Navigate to "Fertilizer Recommendation"
2. Enter soil parameters and crop type
3. Click "Get Recommendation"
4. Screenshot the results

**What Should Be Visible:**
- Input form
- Recommended fertilizer type
- NPK values
- Dosage recommendations
- Application instructions
- Result visualization

**Purpose:** Shows the fertilizer prediction capability

**Where to Include:**
- IEEE Paper: Results section
- Project Report
- User Manual

---

### 10. **Organic Fertilizer Conversion Engine**
**How to Capture:**
1. Navigate to "Organic Conversion"
2. Enter non-organic fertilizer details
3. View organic alternatives
4. Screenshot the conversion results

**What Should Be Visible:**
- Input: Non-organic fertilizer details
- Output: Organic alternatives with recipes
- Ingredient breakdown
- Preparation instructions
- Conversion ratios
- Pie chart visualization (if available)

**Purpose:** Highlights the novel organic conversion feature

**Where to Include:**
- IEEE Paper: Novel Contributions section
- Project Report: Key Features
- User Manual

---

### 11. **Weather Forecast Display**
**How to Capture:**
1. Navigate to "Weather Forecast"
2. Enter location or use current location
3. Screenshot the 7-14 day forecast

**What Should Be Visible:**
- Location name
- Current weather conditions
- 7-14 day forecast with:
  - Temperature
  - Humidity
  - Rainfall prediction
  - Weather icons
- Climate-aware farming tips
- Visual weather cards

**Purpose:** Shows weather integration for climate-aware recommendations

**Where to Include:**
- IEEE Paper: Features section
- Project Report
- User Manual

---

### 12. **Community Platform - Posts Feed**
**How to Capture:**
1. Navigate to "Community"
2. View the posts feed
3. Screenshot the community interface

**What Should Be Visible:**
- List of community posts
- Post titles, authors, timestamps
- Like/comment counts
- "Create New Post" button
- Search/filter options
- Modern card-based layout

**Purpose:** Demonstrates the community engagement feature

**Where to Include:**
- IEEE Paper: Community Features section
- Project Report
- User Manual

---

### 13. **Community Platform - Q&A Section**
**How to Capture:**
1. Navigate to Q&A section in Community
2. Screenshot the questions list

**What Should Be Visible:**
- List of questions
- Question titles, authors
- View counts, save counts
- Answer counts
- "Ask Question" button
- Expert badges (if applicable)

**Purpose:** Shows the knowledge-sharing platform

**Where to Include:**
- IEEE Paper: Community Features
- Project Report

---

### 14. **Expert Sessions Scheduling**
**How to Capture:**
1. Navigate to "Sessions" in Community
2. Screenshot the sessions list

**What Should Be Visible:**
- Upcoming expert sessions
- Session titles
- Expert names
- Scheduled times
- Meeting links (Zoom/Google Meet)
- "Join Session" buttons

**Purpose:** Demonstrates expert-farmer interaction feature

**Where to Include:**
- IEEE Paper: Community Features
- Project Report

---

### 15. **User History/Prediction History**
**How to Capture:**
1. Navigate to "History"
2. Screenshot past predictions

**What Should Be Visible:**
- List of past crop/fertilizer recommendations
- Timestamps
- Input parameters used
- Results obtained
- "View Details" or "Repeat" options

**Purpose:** Shows user data persistence and tracking

**Where to Include:**
- Project Report
- User Manual

---

## 🔐 Admin Panel Screenshots

### 16. **Admin Dashboard - Overview**
**How to Capture:**
1. Login as admin (`?admin=true`)
2. Screenshot the admin control panel

**What Should Be Visible:**
- "🔐 Admin Control Panel" header
- Four tabs:
  - 👥 User Management
  - 📊 System Analytics
  - 📰 Content Management
  - 🎓 Sessions Management
- Professional admin interface design

**Purpose:** Shows the complete admin dashboard

**Where to Include:**
- IEEE Paper: Admin Features section
- Admin Documentation
- Technical Documentation

---

### 17. **Admin - User Management Tab**
**How to Capture:**
1. Click on "User Management" tab
2. Screenshot the user list

**What Should Be Visible:**
- Total user count
- User list with:
  - User ID
  - Username
  - Role badges (color-coded: green for farmers, blue for experts)
  - "Change Role" dropdown
  - "Update" button
  - "🗑️ Delete" button
- Clean table layout

**Purpose:** Demonstrates user management capabilities

**Where to Include:**
- IEEE Paper: Admin Features
- Admin Documentation
- Technical Documentation

---

### 18. **Admin - System Analytics Tab**
**How to Capture:**
1. Click on "System Analytics" tab
2. Screenshot the analytics dashboard

**What Should Be Visible:**
- Metric cards showing:
  - Total Users (with gradient background)
  - Total Posts
  - Total Questions
  - Total Predictions
- User role distribution:
  - Farmers count
  - Experts count
- Visual charts or graphs (if available)

**Purpose:** Shows system monitoring and analytics

**Where to Include:**
- IEEE Paper: Admin Features
- Admin Documentation
- Project Report

---

### 19. **Admin - Content Management Tab**
**How to Capture:**
1. Click on "Content Management" tab
2. Screenshot the posts/questions management interface

**What Should Be Visible:**
- Community Posts section with:
  - Post titles
  - Authors
  - Timestamps
  - "🗑️ Delete Post" buttons
- Questions section with:
  - Question titles
  - Authors
  - View/save counts
  - "🗑️ Delete Question" buttons
- Expandable post/question details

**Purpose:** Demonstrates content moderation capabilities

**Where to Include:**
- IEEE Paper: Admin Features
- Admin Documentation

---

### 20. **Admin - Sessions Management Tab**
**How to Capture:**
1. Click on "Sessions Management" tab
2. Screenshot the session creation form and existing sessions

**What Should Be Visible:**
- "Create New Session" form with:
  - Session Title field
  - Meeting Link field
  - Scheduled Time field
  - Expert Name field
  - "Create Session" button
- "Existing Sessions" list showing:
  - Session titles
  - Expert names
  - Scheduled times
  - Meeting links

**Purpose:** Shows expert session scheduling by admin

**Where to Include:**
- IEEE Paper: Admin Features
- Admin Documentation

---

## 🎯 Feature Demonstration Screenshots

### 21. **AI Crop Doctor Feature**
**How to Capture:**
1. Find the AI Crop Doctor component in the app
2. Upload a plant disease image or enter symptoms
3. Screenshot the diagnosis results

**What Should Be Visible:**
- Image upload interface
- Symptom description field
- AI-generated diagnosis
- Treatment recommendations
- Confidence scores

**Purpose:** Shows AI-powered plant disease diagnosis

**Where to Include:**
- IEEE Paper: AI Features section
- Project Report

---

### 22. **Plagiarism Detection Feature**
**How to Capture:**
1. Navigate to plagiarism checker (if accessible)
2. Upload a PDF document
3. Screenshot the plagiarism report

**What Should Be Visible:**
- PDF upload interface
- "Check Plagiarism" button
- Plagiarism percentage
- Matched sources
- Highlighted plagiarized sections
- Google Custom Search API integration indicator

**Purpose:** Demonstrates content verification feature

**Where to Include:**
- IEEE Paper: Additional Features
- Technical Documentation

---

### 23. **Responsive Design - Mobile View**
**How to Capture:**
1. Open browser developer tools (F12)
2. Switch to mobile device emulation
3. Screenshot key pages in mobile view

**What Should Be Visible:**
- Responsive layout adaptation
- Mobile-friendly navigation
- Touch-optimized buttons
- Readable text on small screens
- Properly scaled images

**Purpose:** Shows responsive design implementation

**Where to Include:**
- IEEE Paper: UI/UX section
- Project Report

---

### 24. **Dark Mode / Theme Toggle (if available)**
**How to Capture:**
1. Toggle theme if available
2. Screenshot the interface in dark mode

**What Should Be Visible:**
- Dark background
- Adjusted color scheme
- Maintained readability
- Consistent design language

**Purpose:** Shows UI customization options

**Where to Include:**
- Project Report
- User Manual

---

## 🗄️ Database Schema Diagrams

### 25. **Complete Database Schema**
**What to Create:**
An ER (Entity-Relationship) diagram showing all tables:

**Tables to Include:**
1. **users**
   - id (PK)
   - username (UNIQUE)
   - password (hashed)
   - role

2. **posts**
   - id (PK)
   - title
   - content
   - author (FK → users.username)
   - created_at

3. **questions**
   - id (PK)
   - title
   - content
   - author (FK → users.username)
   - attachment_path
   - created_at
   - views
   - saves

4. **answers**
   - id (PK)
   - question_id (FK → questions.id)
   - content
   - author (FK → users.username)
   - created_at

5. **sessions**
   - id (PK)
   - title
   - link
   - scheduled_at
   - expert

6. **history**
   - id (PK)
   - username (FK → users.username)
   - input_json
   - result_json
   - created_at

**Recommended Tool:** MySQL Workbench, dbdiagram.io, or Draw.io

**Where to Include:**
- IEEE Paper: Database Design section
- Technical Documentation
- Developer Guide

---

### 26. **Authentication Data Flow Diagram**
**What to Create:**
A diagram showing:
- User credentials input
- Password hashing (SHA-256)
- Database query
- Session state management
- Role-based routing

**Where to Include:**
- IEEE Paper: Security section
- Technical Documentation

---

## 🔄 Workflow Diagrams

### 27. **Crop Recommendation Workflow**
**What to Create:**
A flowchart showing:
```
User Input (Soil + Climate Data) 
  ↓
Data Validation
  ↓
Feature Engineering
  ↓
ML Model Prediction (crop_model.joblib)
  ↓
Crop Duration Lookup
  ↓
Result Display
  ↓
Save to History
```

**Recommended Tool:** Draw.io, Lucidchart

**Where to Include:**
- IEEE Paper: Methodology section
- Technical Documentation
- Project Report

---

### 28. **Organic Fertilizer Conversion Workflow**
**What to Create:**
A flowchart showing:
```
Non-Organic Fertilizer Input (NPK values)
  ↓
Conversion Algorithm (conversion.py)
  ↓
Organic Recipe Generation
  ↓
Ingredient Calculation
  ↓
Pie Chart Visualization
  ↓
Display Results with Instructions
```

**Where to Include:**
- IEEE Paper: Novel Contributions section
- Technical Documentation

---

### 29. **Admin User Management Workflow**
**What to Create:**
A flowchart showing:
```
Admin Login (Environment Variable Auth)
  ↓
Access Admin Dashboard
  ↓
Select User Management Tab
  ↓
View All Users (get_all_users())
  ↓
Admin Actions:
  - Update Role (update_user_role())
  - Delete User (delete_user())
  ↓
Database Update
  ↓
UI Refresh (st.rerun())
```

**Where to Include:**
- Admin Documentation
- Technical Documentation

---

### 30. **Community Post Creation Workflow**
**What to Create:**
A flowchart showing:
```
User Authenticated
  ↓
Navigate to Community
  ↓
Click "Create Post"
  ↓
Fill Post Form (Title, Content)
  ↓
Submit Post
  ↓
Validate Input
  ↓
Save to Database (posts table)
  ↓
Display in Feed
  ↓
Notify Community Members (optional)
```

**Where to Include:**
- Project Report
- User Manual

---

## 📸 Screenshot Organization Tips

### File Naming Convention
Use descriptive, consistent naming:
```
01_landing_page_user_login.png
02_admin_login_screen.png
03_farmer_dashboard_main.png
04_crop_recommendation_input.png
05_crop_recommendation_result.png
06_fertilizer_recommendation.png
07_organic_conversion_engine.png
08_weather_forecast_display.png
09_community_posts_feed.png
10_community_qa_section.png
11_expert_sessions_list.png
12_user_history_view.png
13_admin_dashboard_overview.png
14_admin_user_management.png
15_admin_system_analytics.png
16_admin_content_management.png
17_admin_sessions_management.png
18_ai_crop_doctor.png
19_plagiarism_checker.png
20_mobile_responsive_view.png
21_database_schema_diagram.png
22_system_architecture_diagram.png
23_authentication_flow_diagram.png
24_crop_recommendation_workflow.png
25_organic_conversion_workflow.png
```

---

### Folder Structure
```
climate_aware_final_project/
├── docs/
│   ├── screenshots/
│   │   ├── ui/
│   │   │   ├── 01_landing_page_user_login.png
│   │   │   ├── 02_admin_login_screen.png
│   │   │   ├── 03_farmer_dashboard_main.png
│   │   │   └── ...
│   │   ├── admin/
│   │   │   ├── 13_admin_dashboard_overview.png
│   │   │   ├── 14_admin_user_management.png
│   │   │   └── ...
│   │   ├── features/
│   │   │   ├── 04_crop_recommendation_input.png
│   │   │   ├── 05_crop_recommendation_result.png
│   │   │   └── ...
│   │   └── diagrams/
│   │       ├── 21_database_schema_diagram.png
│   │       ├── 22_system_architecture_diagram.png
│   │       └── ...
```

---

### Screenshot Quality Guidelines

1. **Resolution:** Minimum 1920x1080 for desktop screenshots
2. **Format:** PNG for UI screenshots, SVG for diagrams (if possible)
3. **Annotations:** Add arrows, highlights, or text boxes to emphasize key features
4. **Consistency:** Use the same browser, theme, and window size for all screenshots
5. **Privacy:** Remove or blur any sensitive information (API keys, passwords)
6. **Clarity:** Ensure text is readable, no blurry images
7. **Context:** Include enough context to understand what's being shown

---

### Tools for Screenshot Capture

**Windows:**
- **Snipping Tool** (Built-in): Win + Shift + S
- **Greenshot** (Free): Advanced annotation features
- **ShareX** (Free): Automatic uploading and organization
- **Lightshot** (Free): Quick editing and sharing

**For Diagrams:**
- **Draw.io** (Free, Web-based): https://app.diagrams.net/
- **Lucidchart** (Free tier available): Professional diagrams
- **Microsoft PowerPoint**: Simple flowcharts and diagrams
- **dbdiagram.io** (Free): Database schema diagrams

**For Annotations:**
- **Greenshot**: Built-in annotation
- **Paint.NET** (Free): Image editing
- **GIMP** (Free): Advanced editing
- **Canva** (Free tier): Design and annotations

---

## 📊 Summary: Priority Screenshots for IEEE Paper

### Must-Have (High Priority):
1. ✅ System Architecture Diagram (already exists)
2. ✅ Authentication Flow Diagram
3. ✅ Crop Recommendation Feature (input + result)
4. ✅ Organic Fertilizer Conversion Engine
5. ✅ Admin Dashboard Overview
6. ✅ Admin User Management
7. ✅ Database Schema Diagram
8. ✅ Community Platform Interface

### Should-Have (Medium Priority):
9. ⭐ Weather Forecast Display
10. ⭐ Fertilizer Recommendation Feature
11. ⭐ Admin System Analytics
12. ⭐ User Login Screen
13. ⭐ Admin Login Screen
14. ⭐ Workflow Diagrams (Crop Recommendation, Organic Conversion)

### Nice-to-Have (Low Priority):
15. 💡 Mobile Responsive View
16. 💡 AI Crop Doctor
17. 💡 Plagiarism Checker
18. 💡 User History
19. 💡 Expert Sessions

---

## 🎓 IEEE Paper Section Mapping

### Section I: Introduction
- System Architecture Diagram (high-level overview)

### Section II: Related Work
- (No screenshots needed, literature review)

### Section III: System Architecture
- Complete System Architecture Diagram
- Component Architecture Diagram
- Database Schema Diagram

### Section IV: Implementation
- Authentication Flow Diagram
- Crop Recommendation Workflow
- Organic Conversion Workflow
- Technology Stack Diagram (if created)

### Section V: Features
- Crop Recommendation Screenshot (input + result)
- Fertilizer Recommendation Screenshot
- Organic Conversion Engine Screenshot
- Weather Forecast Screenshot
- Community Platform Screenshot

### Section VI: Admin Features
- Admin Dashboard Overview
- Admin User Management
- Admin System Analytics
- Admin Content Management

### Section VII: Results
- Crop Prediction Results
- Fertilizer Prediction Results
- Organic Conversion Results
- User Engagement Metrics (from analytics)

### Section VIII: Security
- Authentication Flow Diagram
- Admin Login Screen
- Role-Based Access Control Diagram

### Section IX: Conclusion
- (No screenshots needed)

---

## 📝 Caption Templates for Screenshots

### For UI Screenshots:
```
Figure X: [Feature Name] interface showing [key elements]. 
The system provides [functionality description] with [notable features].
```

**Example:**
```
Figure 3: Crop Recommendation interface showing soil parameter inputs (N, P, K, pH) 
and climate data fields (Temperature, Humidity, Rainfall). The system provides 
real-time crop suggestions based on machine learning predictions with crop duration estimates.
```

### For Diagrams:
```
Figure X: [Diagram Type] illustrating [what it shows]. 
[Brief explanation of the flow/structure].
```

**Example:**
```
Figure 1: System Architecture Diagram illustrating the multi-tier architecture 
of the Climate-Aware Farming application. The system integrates machine learning 
models, external APIs, and a community platform within a Streamlit-based frontend.
```

### For Admin Screenshots:
```
Figure X: Admin [Feature Name] showing [administrative capabilities]. 
Administrators can [list of actions] through this interface.
```

**Example:**
```
Figure 8: Admin User Management interface showing the complete user list with 
role-based badges and inline editing capabilities. Administrators can update 
user roles and delete accounts through this centralized control panel.
```

---

## ✅ Checklist for Documentation

### Before Taking Screenshots:
- [ ] Application is running without errors
- [ ] Database is populated with sample data
- [ ] All features are functional
- [ ] UI is in its best visual state (no debug messages)
- [ ] Browser window is at consistent size (1920x1080 recommended)
- [ ] Streamlit branding is hidden (as per your CSS)

### For Each Screenshot:
- [ ] Image is clear and high-resolution
- [ ] Relevant features are visible
- [ ] No sensitive information is exposed
- [ ] File is named according to convention
- [ ] File is saved in appropriate folder
- [ ] Caption is prepared for documentation

### For Diagrams:
- [ ] All components are labeled
- [ ] Flow direction is clear
- [ ] Legend is included (if needed)
- [ ] Consistent styling throughout
- [ ] Exported in high-quality format (PNG/SVG)
- [ ] Editable source file is saved

### For IEEE Paper:
- [ ] All figures are referenced in text
- [ ] Figure numbers are sequential
- [ ] Captions are descriptive and professional
- [ ] Images are properly sized for paper format
- [ ] All diagrams follow IEEE formatting guidelines

---

## 🚀 Quick Start Guide

### Step 1: Capture UI Screenshots
1. Start your application: `streamlit run app/app.py`
2. Create a test user account (farmer role)
3. Create an admin account access via `?admin=true`
4. Navigate through each feature and capture screenshots
5. Save in `docs/screenshots/ui/` folder

### Step 2: Capture Admin Screenshots
1. Login as admin
2. Navigate through all 4 admin tabs
3. Capture each tab's interface
4. Save in `docs/screenshots/admin/` folder

### Step 3: Create Diagrams
1. Use Draw.io or Lucidchart
2. Create system architecture diagrams
3. Create workflow diagrams
4. Create database schema diagram
5. Export as PNG (high resolution)
6. Save in `docs/screenshots/diagrams/` folder

### Step 4: Organize and Document
1. Rename files according to naming convention
2. Create a `SCREENSHOTS_INDEX.md` file listing all screenshots
3. Prepare captions for each image
4. Map screenshots to IEEE paper sections

---

## 📞 Need Help?

If you need assistance with:
- **Creating specific diagrams:** Let me know which diagram you'd like help with
- **Screenshot annotations:** I can guide you through annotation tools
- **IEEE paper integration:** I can help format figures for your paper
- **Additional visualizations:** I can suggest other useful diagrams

---

**Last Updated:** December 22, 2025  
**Version:** 1.0  
**Author:** Climate-Aware Farming Project Team
