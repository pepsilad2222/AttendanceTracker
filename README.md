# Attendance Tracking System (Streamlit App)

## Project Requirements & Breakdown

### Problem Identification and Analysis

**Domain:** Education  
Manual attendance tracking in classrooms is inefficient, error-prone, and lacks transparency for both students and administrators.

**Key Challenges:**
- Manual errors in roll calls or sign-in sheets
- Difficulty tracking late arrivals
- No centralized log for accountability
- Instructors wasting valuable teaching time

**Stakeholders:**
- Students
- Teachers/Instructors
- School administrators

**Impact:**
- Accurate and timely attendance impacts academic records, punctuality, and accountability
- Automating this process enhances fairness and improves classroom management

**Supporting Evidence:**
- Many institutions are having a hard time keeping up with all students espically in classes where there are hundreds of people.
- Anywhere from 5 to 10 minuets can be wasted by the instructor calling everyones name either at the beginning or end of class.
- Research shows automating attendance improves reporting accuracy and reduces time spent on class logistics

---

### Solution Design

**Proposed IT Solution:**  
A **Streamlit-based web application** where:
- Students log their attendance by verifying their ID, section, and a secure lecture code
- Attendance is time-logged and categorized as `Present`, `Tardy`, or `Absent`
- Admins securely view and validate attendance logs

**Design Components:**
- **Frontend/UI:** Streamlit interface with clean, clickable login sections
- **Backend/Logic:** Python and Pandas for form handling, verification, and CSV-based storage
- **Security:** Admin login validation with hardcoded credentials, basic lecture code verification
- **Scalability & Reliability:** Easily extended to support new sections, multi-user interface; all data stored persistently in CSV
- **Data Flow:** 
  - `logininfo.csv` contains user details
  - `attendance_log.csv` stores timestamped attendance records

---

### Implementation Details

**Tools Used:**
- Python 3
- Streamlit
- Pandas

**Core Files:**
| File               | Description                                 |
|--------------------|---------------------------------------------|
| `attendance_app.py`| The main Streamlit app                      |
| `logininfo.csv`    | Contains valid usernames, sections, names   |
| `attendance_log.csv`| Stores recorded attendance entries         |

---

### Testing and Validation

- **Time-based logic tested**: 
  - Present: 8:00 – 8:05 AM  
  - Tardy: 8:06 – 8:15 AM  
  - Absent: 8:16 – 9:20 AM  
- **Input validations**: Username format, section name, lecture code
- **Admin vs. Student interface separation** ensures proper access control
- Functional prototype tested with multiple entries

---

### Societal Impact and Contribution

This tool saves educators time and reduces record-keeping mistakes. It promotes:
- Punctuality and responsibility among students
- Better classroom management
- Transparency and automation in academic settings
- A digital solution accessible to any classroom, even with limited infrastructure

---

## Authors

- Michael Aghassi 
- Matthew Delacruz
- Jaden West
- Fabrice Mpozenzi
- Gray Hagood

