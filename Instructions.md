# Attendance Tracking System

A lightweight Streamlit application for managing classroom attendance efficiently and securely.

---

## How to Clone and Run the App

### Step 1: Clone the Repository
In your terminal or command prompt, run:
git clone https://github.com/pepsilad2222/AttendanceTracker.git  
cd AttendanceTracker
cd "MIS Project"

### Step 2: Install the Dependencies
Make sure you have python installed. Once you do,
Run the following commands:
pip install streamlit

pip install pandas

### Step 3: Run the App
Start the app by running:
streamlit run attendance_app.py

This will open the app in your default browser at:  
http://localhost:8501

---

## How to Use the App

###  Student Sign-In Instructions

1. Click **"User Log In"** on the homepage.
2. Refer to `logininfo.csv` to find a valid:
   - **9-digit Username** (e.g., `000000006`)
   - **Section** (e.g., `324.01`)
3. Use the default **Lecture Code**: `55555`
4. The point of the Lecture Code is to only access the attendance while in class. The instructor will have it at the beginning of class and it will be randomly generated each class peroid. For the sake of this demonstration is will be 55555.
5. Click **Enter** to verify your credentials.
6. If valid, confirm your attendance by checking **"Yes, I am present"** and clicking **Submit Attendance**.
7. You will see a success message confirming your attendance.

### Admin Panel Instructions

1. Click **"Administrator Log In"** on the homepage.
2. Use one of the following credentials:

| Name          | Username    | Section  | Lecture Code |
|---------------|-------------|----------|---------------|
| Joseph Manga  | 000000040   | 324.01   | 55555         |
| Jacob Russell | 000000039   | 324.01   | 55555         |

3. Click **Enter** to access the admin dashboard.
4. You can view all attendance logs and click **Log out** to return to the main screen.

---

## Status Logic Reference

| Time Logged        | Attendance Status |
|--------------------|-------------------|
| 8:00 – 8:05 AM     | Present           |
| 8:06 – 8:15 AM     | Tardy             |
| 8:16 – 9:20 AM     | Absent            |
| Outside Class Time | Absent            |

---

## Future Improvements

- Integration with SQLite or Firebase for scalable storage
- Graphical analytics dashboard for admins
- Support for multiple class sections and schedules
- Email or SMS notifications
- Admin export to CSV/PDF

---

## License

This project is intended for educational use only. All rights reserved.
