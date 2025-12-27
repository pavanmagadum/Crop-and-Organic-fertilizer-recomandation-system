# 📸 QUICK REFERENCE CARD
## Screenshot & Diagram Checklist

**Print this page and check off items as you complete them!**

---

## 🔴 CRITICAL PRIORITY (Do These First!)

### Screenshots to Capture:

- [ ] **1. Crop Recommendation Input**
  - File: `01_crop_recommendation_input.png`
  - Folder: `docs\screenshots\ui\`
  - Time: 4 min

- [ ] **2. Crop Recommendation Result**
  - File: `02_crop_recommendation_result.png`
  - Folder: `docs\screenshots\ui\`
  - Time: 2 min

- [ ] **3. Organic Conversion Complete**
  - File: `03_organic_conversion_complete.png`
  - Folder: `docs\screenshots\ui\`
  - Time: 5 min

- [ ] **4. Admin Dashboard Overview**
  - File: `04_admin_dashboard_overview.png`
  - Folder: `docs\screenshots\admin\`
  - Time: 3 min
  - **URL:** `http://localhost:8501?admin=true`

- [ ] **5. Admin User Management**
  - File: `05_admin_user_management.png`
  - Folder: `docs\screenshots\admin\`
  - Time: 4 min

- [ ] **6. Admin Login Screen**
  - File: `06_admin_login_screen.png`
  - Folder: `docs\screenshots\ui\`
  - Time: 2 min
  - **URL:** `http://localhost:8501?admin=true`

- [ ] **7. User Login Screen**
  - File: `07_user_login_screen.png`
  - Folder: `docs\screenshots\ui\`
  - Time: 2 min
  - **URL:** `http://localhost:8501`

- [ ] **8. Farmer Dashboard Main**
  - File: `08_farmer_dashboard_main.png`
  - Folder: `docs\screenshots\ui\`
  - Time: 3 min

**Total Time: 25 minutes**

---

### Diagrams to Create:

- [ ] **1. Database Schema ER Diagram**
  - File: `24_database_schema.png`
  - Folder: `docs\screenshots\diagrams\exports\`
  - Tool: https://dbdiagram.io
  - Template: `DIAGRAM_TEMPLATES.md` Section 5
  - Time: 15 min

- [ ] **2. Authentication Flow Diagram**
  - File: `23_authentication_flow.png`
  - Folder: `docs\screenshots\diagrams\exports\`
  - Tool: https://app.diagrams.net
  - Template: `DIAGRAM_TEMPLATES.md` Section 1
  - Time: 20 min

- [ ] **3. Crop Recommendation Workflow**
  - File: `25_crop_recommendation_workflow.png`
  - Folder: `docs\screenshots\diagrams\exports\`
  - Tool: https://app.diagrams.net
  - Template: `DIAGRAM_TEMPLATES.md` Section 2
  - Time: 15 min

**Total Time: 50 minutes**

---

## 🟡 HIGH PRIORITY (Do These Second)

### Screenshots:

- [ ] **9. Community Platform**
  - File: `09_community_platform.png`
  - Time: 3 min

- [ ] **10. Weather Forecast**
  - File: `10_weather_forecast.png`
  - Time: 3 min

- [ ] **11. Admin System Analytics**
  - File: `11_admin_system_analytics.png`
  - Time: 3 min

- [ ] **12. Fertilizer Recommendation**
  - File: `12_fertilizer_recommendation.png`
  - Time: 4 min

- [ ] **13. User Registration**
  - File: `13_user_registration.png`
  - Time: 3 min

**Total Time: 16 minutes**

---

### Diagrams:

- [ ] **4. Organic Conversion Workflow**
  - File: `26_organic_conversion_workflow.png`
  - Time: 10 min

**Total Time: 10 minutes**

---

## 🟢 MEDIUM PRIORITY (Optional)

- [ ] Expert Sessions (2 min)
- [ ] User History (2 min)
- [ ] Admin Content Management (4 min)
- [ ] Admin Sessions Management (4 min)

**Total Time: 12 minutes**

---

## ⚡ QUICK COMMANDS

### Start Application:
```bash
cd c:\Users\sw\Desktop\climate_aware_final_project
venv\Scripts\activate
streamlit run app\app.py
```

### Admin Login Credentials:
- **URL:** `http://localhost:8501?admin=true`
- **Username:** `admin`
- **Password:** `Admin@2025` (check your `.env` file)

### Screenshot Tool:
- **Windows:** `Win + Shift + S`

---

## 📁 FOLDER STRUCTURE

```
docs\screenshots\
├── ui\               ← User interface screenshots
├── admin\            ← Admin panel screenshots
├── features\         ← Feature demos
└── diagrams\
    ├── source\       ← .drawio, .dbml files
    └── exports\      ← PNG files for paper
```

---

## 🎯 SAMPLE DATA FOR SCREENSHOTS

### Crop Recommendation:
- N: 90, P: 42, K: 43
- pH: 6.5
- Temp: 25°C, Humidity: 80%, Rainfall: 200mm

### Fertilizer Recommendation:
- N: 30, P: 50, K: 40
- Crop: Rice
- Soil: Loamy

### Organic Conversion:
- Fertilizer: Urea
- N: 46%, P: 0%, K: 0%
- Quantity: 100 kg

---

## ✅ QUALITY CHECKLIST

Before marking complete:
- [ ] Image is clear (not blurry)
- [ ] Resolution ≥ 1920x1080
- [ ] All text is readable
- [ ] No sensitive info visible
- [ ] File named correctly
- [ ] Saved in correct folder

---

## 📊 PROGRESS TRACKER

**Critical Screenshots:** ___/8 complete  
**Critical Diagrams:** ___/3 complete  
**High Priority Screenshots:** ___/5 complete  
**High Priority Diagrams:** ___/1 complete  

**Total Critical Items:** ___/11 complete  
**Overall Progress:** ___/38 complete (___%)

---

## 🔗 DOCUMENT GUIDE

| Need to... | Open this file... |
|------------|-------------------|
| Understand what's needed | `SCREENSHOT_GUIDE.md` |
| Create diagrams | `DIAGRAM_TEMPLATES.md` |
| Capture screenshots | `SCREENSHOT_CAPTURE_GUIDE.md` |
| Track progress | `SCREENSHOTS_INDEX.md` |
| Get overview | `DOCUMENTATION_VISUALS_SUMMARY.md` |
| Quick reference | **THIS FILE** |

---

## ⏱️ TIME ESTIMATES

| Task | Time |
|------|------|
| Critical Screenshots | 25 min |
| Critical Diagrams | 50 min |
| High Priority Screenshots | 16 min |
| High Priority Diagrams | 10 min |
| **TOTAL CRITICAL** | **75 min** |
| **TOTAL HIGH** | **26 min** |
| **GRAND TOTAL** | **101 min** |

---

## 🎓 FOR IEEE PAPER

### Figure Numbering:
Start from Figure 1 and number sequentially.

### Caption Format:
```
Figure X: [Description]. [Additional details].
```

### Placement:
Place figure after first reference in text.

---

## 🆘 TROUBLESHOOTING

**App won't start?**
→ Check virtual environment is activated

**Admin login not yellow?**
→ Make sure URL has `?admin=true`

**No data showing?**
→ Create sample users/posts first

**Screenshot too large?**
→ Compress at tinypng.com

---

## 📞 NEED HELP?

1. Check `SCREENSHOT_CAPTURE_GUIDE.md` for detailed steps
2. Check `DIAGRAM_TEMPLATES.md` for diagram templates
3. Check troubleshooting sections in guides

---

**🎯 TODAY'S GOAL:** Complete all CRITICAL items (11 items, 75 min)

**START TIME:** _________  
**END TIME:** _________  
**ACTUAL TIME:** _________

---

**Good luck! 🚀**

---

**Print this page and keep it next to you while working!**
