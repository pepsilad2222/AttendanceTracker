import streamlit as st
import datetime
import pandas as pd
import re
import os

# File paths
LOGIN_FILE = "logininfo.csv"
ATTENDANCE_FILE = "attendance_log.csv"
ADMIN_USERS = {"000000039", "000000040"}

# Create attendance log file if it doesn't exist
def initialize_attendance_csv():
    if not os.path.exists(ATTENDANCE_FILE):
        df = pd.DataFrame(columns=["Date", "Username", "Name", "Section", "Time", "Status"])
        df.to_csv(ATTENDANCE_FILE, index=False)

# Load authorized users
def load_login_info():
    if not os.path.exists(LOGIN_FILE):
        st.error("logininfo.csv not found.")
        st.stop()
    return pd.read_csv(LOGIN_FILE)

# Match user by username and section
def find_user_info(username, section, login_df):
    login_df["Username"] = login_df["Username"].astype(str).str.zfill(9)
    login_df["Section"] = login_df["Section"].astype(str).str.strip().str.upper()

    username = str(username).zfill(9)
    section = section.strip().upper()

    match = login_df[
        (login_df["Username"] == username) & (login_df["Section"] == section)
    ]
    if not match.empty:
        return match.iloc[0]["Name"]
    return None

# Append a new attendance record with time and status
def log_attendance(username, name, section):
    df = pd.read_csv(ATTENDANCE_FILE)

    now = datetime.datetime.now()
    today = now.date().isoformat()
    time_now = now.strftime("%I:%M:%S %p")
    time_obj = now.time()

    CLASS_START = datetime.time(8, 0)
    PRESENT_CUTOFF = datetime.time(8, 5)
    TARDY_CUTOFF = datetime.time(8, 15)
    CLASS_END = datetime.time(9, 20)

    if CLASS_START <= time_obj <= PRESENT_CUTOFF:
        status = "Present"
    elif PRESENT_CUTOFF < time_obj <= TARDY_CUTOFF:
        status = "Tardy"
    elif TARDY_CUTOFF < time_obj <= CLASS_END:
        status = "Absent"
    else:
        status = "Absent"

    new_entry = {
        "Date": today,
        "Username": username,
        "Name": name,
        "Section": section,
        "Time": time_now,
        "Status": status
    }

    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(ATTENDANCE_FILE, index=False)

# Validate 9-digit username format
def valid_username_format(username):
    return re.fullmatch(r"\d{9}", username)

# Student sign-in page
def student_sign_in():
    st.write("### Student Sign-In")
    st.write("Hello, please sign in to confirm your attendance.")
    login_df = load_login_info()

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    VALID_LECTURE_CODE = "55555"

    if not st.session_state.authenticated and not st.session_state.submitted:
        username = st.text_input("Enter your 9-digit Username:")
        section = st.text_input("Enter your Class Section:")
        lecture_code = st.text_input("Enter the 5-digit Lecture Code:")

        if username and not valid_username_format(username):
            st.error("Username must be a 9-digit number.")
            return

        if st.button("Enter"):
            name = find_user_info(username, section, login_df)
            if lecture_code != VALID_LECTURE_CODE:
                st.error("Invalid lecture code. Please try again.")
            elif name:
                st.session_state.authenticated = True
                st.session_state.name = name
                st.session_state.username = username
                st.session_state.section = section
                st.rerun()
            else:
                st.error("Invalid login. Please check your username and section.")

    elif st.session_state.authenticated and not st.session_state.submitted:
        name = st.session_state.name
        now = datetime.datetime.now()
        today = now.strftime("%B %d, %Y")
        weekday = now.strftime("%A")
        current_time = now.strftime("%I:%M:%S %p")

        st.success(f"Welcome, {name}!")
        st.subheader(f"Are you present for {weekday}, {today}?")
        st.markdown(f"**Current Time:** {current_time}")

        is_present = st.checkbox("Yes, I am present")

        if is_present and st.button("Submit Attendance"):
            log_attendance(st.session_state.username, name, st.session_state.section)
            st.session_state.authenticated = False
            st.session_state.submitted = True
            st.rerun()

    elif st.session_state.submitted:
        st.success("Thank you, you have been logged out and counted present! Enjoy class!")
        if st.button("Click here to go back to the main page"):
            st.session_state.submitted = False
            st.rerun()

# Admin page
def admin_panel():
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False
        st.session_state.admin_name = ""

    if st.session_state.admin_logged_in:
        st.write(f"### Welcome, {st.session_state.admin_name}")
        df = pd.read_csv(ATTENDANCE_FILE, dtype={"Username": str})
        df["Username"] = df["Username"].str.zfill(9)

        if df.empty:
            st.info("No attendance records yet.")
        else:
            st.dataframe(df[["Date", "Name", "Username", "Section", "Time", "Status"]])

        if st.button("Log out"):
            st.session_state.admin_logged_in = False
            st.session_state.admin_name = ""
            st.rerun()

    else:
        st.write("### Admin Panel Login")

        name = st.selectbox("Who are you?", ["", "Joseph Manga", "Jacob Russell"])
        username = st.text_input("Enter your 9-digit Username:")
        section = st.text_input("Enter your Class Section:")
        lecture_code = st.text_input("Enter the 4-digit Lecture Code:")

        ADMIN_CREDENTIALS = {
            "Joseph Manga": "000000040",
            "Jacob Russell": "000000039"
        }
        VALID_SECTION = "324.01"
        VALID_CODE = "55555"

        if st.button("Enter"):
            if name == "" or not username or not section or not lecture_code:
                st.error("Please complete all fields.")
                return

            username = username.zfill(9)
            section = section.strip().upper()
            lecture_code = lecture_code.strip()

            if name not in ADMIN_CREDENTIALS:
                st.error("Invalid name selected.")
            elif username != ADMIN_CREDENTIALS[name]:
                st.error("Username does not match the selected name.")
            elif section != VALID_SECTION:
                st.error("Invalid class section.")
            elif lecture_code != VALID_CODE:
                st.error("Invalid lecture code.")
            else:
                st.session_state.admin_logged_in = True
                st.session_state.admin_name = name
                st.rerun()

# Main landing and routing
def main():
    st.set_page_config(page_title="Attendance Tracker", layout="centered")
    initialize_attendance_csv()

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        st.markdown("<h1 style='text-align: center;'>Welcome to the Attendance Tracker</h1>", unsafe_allow_html=True)
        st.write("")

        col1, col2, col3 = st.columns([2, 1, 2])

        with col1:
            st.markdown("""
                <style>
                div.stButton > button {
                    width: 100%;
                    height: 3em;
                    font-size: 1.2em;
                }
                </style>
            """, unsafe_allow_html=True)
            user_click = st.button("User Log In")

        with col3:
            admin_click = st.button("Administrator Log In")

        if user_click:
            st.session_state.page = "student"
            st.rerun()

        if admin_click:
            st.session_state.page = "admin"
            st.rerun()

    elif st.session_state.page == "student":
        st.button("⬅ Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))
        student_sign_in()

    elif st.session_state.page == "admin":
        st.button("⬅ Back to Home", on_click=lambda: st.session_state.update({"page": "home"}))
        admin_panel()

if __name__ == "__main__":
    main()
