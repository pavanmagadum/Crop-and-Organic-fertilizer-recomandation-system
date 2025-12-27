# 🔧 HOME PAGE CARDS - WHITE BACKGROUND FIX

## ❌ **PROBLEM IDENTIFIED:**

The Home page feature cards have **white/light backgrounds** making text invisible.

**Cause:** The CSS classes (`.feature-card`) were added to `css_magic.css` but aren't being applied properly.

---

## ✅ **SOLUTION - MANUAL FIX:**

### **Option 1: Add Inline Styles (Quick Fix)**

Edit `app/app.py` around lines 446-517 and add inline `style` attributes to each card div:

**Find this:**
```html
<div class="feature-card">
```

**Replace with:**
```html
<div class="feature-card" style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(26, 31, 58, 0.7) 100%); border: 2px solid rgba(139, 92, 246, 0.3); border-radius: 20px; padding: 32px;">
```

**Do this for all 4 cards:**
1. Smart Crop Prediction (line ~449)
2. Organic Fertilizer (line ~486)
3. Preparation Guides (line ~468)
4. Expert Community (line ~505)

---

### **Option 2: Force CSS Load**

Add this at the top of the Home page (after line 427):

```python
st.markdown("""
<style>
.feature-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(26, 31, 58, 0.7) 100%) !important;
    border: 2px solid rgba(139, 92, 246, 0.3) !important;
    border-radius: 20px !important;
    padding: 32px !important;
}
.feature-card-title {
    color: #e2e8f0 !important;
}
</style>
""", unsafe_allow_html=True)
```

---

## 🎯 **WHAT THIS FIXES:**

✅ Dark card backgrounds  
✅ Visible text (white/gray on dark)  
✅ Purple borders  
✅ Professional appearance  

---

## 📝 **QUICK MANUAL EDIT:**

1. Open `app/app.py`
2. Go to line 449 (first card)
3. Find: `<div class="feature-card">`
4. Replace with the styled version above
5. Repeat for all 4 cards
6. Save and refresh browser

---

**This will immediately fix the white card backgrounds!**
