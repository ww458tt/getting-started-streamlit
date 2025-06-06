import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("การเขียนกราฟฟังก์ชันด้วยภาษาpython")

# page1: เลือกประเภทฟังก์ชัน
function_type = st.selectbox(
    "เลือกประเภทของฟังก์ชันที่ต้องการวาดกราฟ",
    ("ฟังก์ชันเชิงเส้น", "ฟังก์ชันกำลังสอง")
)

# กรอกค่าพารามิเตอร์ตามประเภท
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
    x = np.linspace(-10, 10, 200)
    
    fig, ax = plt.subplots()
    
    if function_type == "ฟังก์ชันเชิงเส้น": #ถ้าเลือกฟังก์ชันเชิงเส้น ใช้ฟังก์ชันเชิงเส้น
        y = a * x + b
        ax.plot(x, y, label=f"y = {a}x + {b}", color='blue')

        # เส้นแกน x, y
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
    else:
        y = a * x**2 + b * x + c # ถ้าไม่ใช่ฟังก์ชังเชิงเส้น ใช้ฟังก์ชันกำลังสอง
        xv = -b / (2 * a)
        yv = a * xv**2 + b * xv + c
        directrix_y = yv - 1 / (4 * a)
        latus_len = 1 / abs(a)

        ax.plot(x, y, label=f"y = {a}x² + {b}x + {c}", color='blue')

        # จุดยอด
        ax.plot(xv, yv, 'ro', label='Vertex')
        # แกนสมมาตร
        ax.axvline(xv, linestyle='dashed', color='green', label='axis of symmetry')
        # เส้นไดเรกตริกซ์
        ax.axhline(directrix_y, linestyle='dotted', color='red', label='Directrix')
        # ลาตัสเรกตัม
        ax.hlines(yv, xv - latus_len / 2, xv + latus_len / 2, color='purple', linestyle='dashed', label='Latus Rectum')


    # ค่าร่วม
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)




