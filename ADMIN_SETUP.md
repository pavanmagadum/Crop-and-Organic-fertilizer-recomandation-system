# Admin Setup Guide

## 🔐 Admin Authentication System

This guide explains how to access and use the admin panel for the Climate-Aware Farming application.

---

## Quick Start

### Default Admin Credentials

- **Username:** `admin`
- **Password:** `Admin@2025` (You can change this in the `.env` file)

### How to Access Admin Login

The admin login is **hidden from regular users** to maintain security. To access it:

1. **Local Development:**
   ```
   http://localhost:8501?admin=true
   ```

2. **After Deployment:**
   ```
   https://your-app-url.com?admin=true
   ```

**Important:** The `?admin=true` parameter is required to see the admin login option.

---

## Changing Admin Password

### For Local Development

1. Open the `.env` file in the project root directory
2. Change the `ADMIN_PASSWORD` value:
   ```
   ADMIN_PASSWORD=YourNewSecurePassword123!
   ```
3. Save the file and restart the application

### For Deployment (Streamlit Cloud)

1. Go to your app settings on Streamlit Cloud
2. Navigate to **Secrets** section
3. Add the following:
   ```toml
   ADMIN_PASSWORD = "YourNewSecurePassword123!"
   ```
4. Save and redeploy

### For Deployment (Heroku)

1. Go to your app dashboard on Heroku
2. Navigate to **Settings** → **Config Vars**
3. Add a new config var:
   - **KEY:** `ADMIN_PASSWORD`
   - **VALUE:** `YourNewSecurePassword123!`
4. Save changes

### For Deployment (Other Platforms)

Set an environment variable named `ADMIN_PASSWORD` with your desired password value.

---

## Admin Dashboard Features

Once logged in as admin, you'll have access to four main sections:

### 1. 👥 User Management

**Features:**
- View all registered users (Farmers and Experts)
- See user IDs, usernames, and roles
- Change user roles (Farmer ↔ Agricultural Expert)
- Delete users from the system

**Use Cases:**
- Moderate user accounts
- Upgrade farmers to expert status
- Remove spam or inactive accounts

---

### 2. 📊 System Analytics

**Features:**
- **Total Users:** Count of all registered users
- **Total Posts:** Number of community posts
- **Total Questions:** Questions asked by farmers
- **Predictions Made:** Number of crop/fertilizer predictions

**Additional Metrics:**
- User role distribution (Farmers vs Experts)
- Real-time system statistics

**Use Cases:**
- Monitor platform growth
- Track user engagement
- Identify trends and patterns

---

### 3. 📰 Content Management

**Features:**
- View all community posts with details
- View all questions with metadata (views, saves)
- Delete inappropriate or spam content
- Moderate community discussions

**Use Cases:**
- Remove spam or offensive content
- Manage community quality
- Monitor user-generated content

---

### 4. 🎓 Sessions Management

**Features:**
- Create new expert sessions
- Schedule live sessions with meeting links
- View all existing sessions
- Manage session details (title, expert, time, link)

**Session Creation Fields:**
- **Session Title:** Name of the session
- **Meeting Link:** Zoom/Google Meet URL
- **Scheduled Time:** When the session will occur
- **Expert Name:** Who will conduct the session

**Use Cases:**
- Schedule educational webinars
- Organize Q&A sessions
- Connect farmers with experts

---

## Security Best Practices

### ✅ DO:
- Change the default admin password immediately
- Use a strong password (mix of letters, numbers, symbols)
- Keep the `.env` file secure and never commit it to Git
- Only share admin credentials with trusted team members
- Use the `?admin=true` URL parameter to access admin login

### ❌ DON'T:
- Share admin credentials publicly
- Use simple passwords like "admin123"
- Commit the `.env` file to version control
- Share the admin login URL with regular users
- Leave the default password in production

---

## Troubleshooting

### Issue: "Invalid admin credentials"

**Solution:**
1. Verify you're using the correct username: `admin`
2. Check the password in your `.env` file
3. Ensure the `.env` file is in the project root directory
4. Restart the application after changing the password

### Issue: "Can't see admin login option"

**Solution:**
1. Make sure you're using the URL with `?admin=true` parameter
2. Example: `http://localhost:8501?admin=true`

### Issue: "Environment variable not found"

**Solution:**
1. Create a `.env` file in the project root
2. Add: `ADMIN_PASSWORD=YourPassword`
3. Install python-dotenv: `pip install python-dotenv`
4. Restart the application

---

## Regular User Access

Regular users (Farmers and Experts) should access the application normally:

- **Local:** `http://localhost:8501`
- **Deployed:** `https://your-app-url.com`

They will see the standard login/register interface and **will not** see admin options.

---

## Support

For additional help or questions:
1. Check the application logs for error messages
2. Verify all environment variables are set correctly
3. Ensure the database file has proper permissions
4. Contact the development team if issues persist

---

## Summary

- **Admin Username:** `admin` (fixed)
- **Admin Password:** Set in `.env` file (changeable)
- **Admin Access URL:** Add `?admin=true` to your application URL
- **Security:** Keep credentials secure and change default password
- **Features:** User management, analytics, content moderation, session scheduling

**Remember:** The admin panel gives you complete control over the system. Use it responsibly!
