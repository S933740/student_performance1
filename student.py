import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
df = pd.read_csv("student_perf.csv")

# Streamlit App Title
st.title("🎓 Student Performance Dashboard")
st.write("Interactive analytics for marks & attendance")

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Sidebar Menu
menu = st.sidebar.radio(
    "Select an Option",
    ["View Dataset", "Search by Student ID", "Search by Student Name",
     "Filter by Minimum Marks", "Filter by Minimum Attendance",
     "Scatter Plot (Marks vs Attendance)", "Pie Chart (Class Distribution)"]
)

# --------------- MENU FUNCTIONS -----------------

# View dataset
if menu == "View Dataset":
    st.subheader("📁 Full Dataset")
    st.dataframe(df)

# Search by Student ID
elif menu == "Search by Student ID":
    sid = st.number_input("Enter Student ID", min_value=1)
    result = df[df["StudentID"] == sid]
    if not result.empty:
        st.success("✔ Student Found")
        st.table(result)
    else:
        st.error("❌ Student Not Found")

# Search by Student Name
elif menu == "Search by Student Name":
    name = st.text_input("Enter Name or Keyword")
    if name:
        result = df[df["Name"].str.lower().str.contains(name.lower())]
        if not result.empty:
            st.success("✔ Match Found")
            st.table(result)
        else:
            st.error("❌ No matching student found")

# Filter by Marks
elif menu == "Filter by Minimum Marks":
    min_marks = st.slider("Select Minimum Marks", 0, 100, 50)
    result = df[df["Marks"] >= min_marks]
    st.write(f"Showing students with marks ≥ {min_marks}")
    st.table(result)

# Filter by Attendance
elif menu == "Filter by Minimum Attendance":
    min_att = st.slider("Select Minimum Attendance %", 0, 100, 75)
    result = df[df["Attendance"] >= min_att]
    st.write(f"Showing students with attendance ≥ {min_att}%")
    st.table(result)

# Scatter Chart
elif menu == "Scatter Plot (Marks vs Attendance)":
    fig = px.scatter(
        df,
        x="Marks",
        y="Attendance",
        text="Name",
        size="Marks",
        color="Class",
        title="Student Performance (Marks vs Attendance)"
    )
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig)

# Pie Chart
elif menu == "Pie Chart (Class Distribution)":
    fig = px.pie(
        df,
        names="Class",
        title="Class-wise Student Distribution",
        hole=0.3
    )
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.write("Developed using *Streamlit & Plotly* 🚀")
