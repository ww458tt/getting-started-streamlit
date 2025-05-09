import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("การเขียนกราฟฟังก์ชันด้วยภาษาpython")

# page1: เลือกประเภทฟังก์ชัน
function_type = st.selectbox(
    "เลือกประเภทของฟังก์ชันที่ต้องการวาดกราฟ",
    ("ฟังก์ชันเชิงเส้น", "ฟังก์ชันกำลังสอง")
)

# รับค่าพารามิเตอร์ตามประเภท
if function_type == "ฟังก์ชันเชิงเส้น":
    st.subheader("f(x) = ax + b")
    a = st.number_input("ค่า a", value=1.0)
    b = st.number_input("ค่า b", value=0.0)
    
elif function_type == "ฟังก์ชันกำลังสอง":
    st.subheader("f(x) = ax² + bx + c")
    a = st.number_input("ค่า a", value=1.0)
    b = st.number_input("ค่า b", value=0.0)
    c = st.number_input("ค่า c", value=0.0)

# เมื่อกดปุ่ม จะสร้างกราฟ
if st.button("แสดงกราฟ"):
    x = np.linspace(-10, 10, 400)
    
    if function_type == "ฟังก์ชันเชิงเส้น": #ถ้าเลือกฟังก์ชันเชิงเส้น ใช้ฟังก์ชันเชิงเส้น
        y = a * x + b
    else:
        y = a * x**2 + b * x + c # ถ้าไม่ใช่ฟังก์ชังเชิงเส้น ใช้ฟังก์ชันกำลังสอง

    fig, ax = plt.subplots()
    ax.plot(x, y, label="graph line")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)



