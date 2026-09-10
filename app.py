import streamlit as st

# Thiết lập cấu hình trang Streamlit
st.set_page_config(
    page_title="Công cụ tính tiền tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# Tiêu đề ứng dụng
st.title("💰 Công Cụ Tính Tiền Tiết Kiệm")
st.write("Ứng dụng giúp bạn dễ dàng tính toán số tiền nhận được khi gửi tiết kiệm theo **Lãi đơn** hoặc **Lãi kép**.")

st.markdown("---")

# --- KHU VỰC NHẬP DỮ LIỆU ---
st.subheader("📝 Nhập thông tin gửi tiết kiệm")

col1, col2 = st.columns(2)

with col1:
    # Nhập số tiền gửi (VND)
    so_tien_gui = st.number_input(
        "Số tiền gửi ban đầu (VNĐ):",
        min_value=0,
        value=100000000,
        step=1000000,
        format="%d"
    )
    
    # Chọn loại lãi suất
    loai_lai = st.radio(
        "Hình thức tính lãi:",
        ["Lãi đơn", "Lãi kép"]
    )

with col2:
    # Nhập thời gian gửi (Tháng)
    so_thang = st.number_input(
        "Thời gian gửi (Số tháng):",
        min_value=1,
        value=12,
        step=1
    )
    
    # Nhập lãi suất (% / năm)
    lai_suat_nam = st.number_input(
        "Lãi suất (% / năm):",
        min_value=0.0,
        value=6.0,
        step=0.1,
        format="%.2f"
    )

# --- XỬ LÝ TÍNH TOÁN ---
# Đổi lãi suất năm sang lãi suất tháng
r_thang = (lai_suat_nam / 100) / 12

if loai_lai == "Lãi đơn":
    # Công thức lãi đơn: P_mới = P_đầu + (P_đầu * r_tháng * số_tháng)
    tien_lai = so_tien_gui * r_thang * so_thang
    tong_tien = so_tien_gui + tien_lai
else:
    # Công thức lãi kép: P_mới = P_đầu * (1 + r_tháng) ^ số_tháng
    tong_tien = so_tien_gui * ((1 + r_thang) ** so_thang)
    tien_lai = tong_tien - so_tien_gui

# --- HIỂN THỊ KẾT QUẢ ---
st.markdown("---")
st.subheader("📊 Kết quả tính toán")

# Nút thực hiện tính toán (hoặc ứng dụng tự động cập nhật khi đổi số)
col_res1, col_res2, col_res3 = st.columns(3)

with col_res1:
    st.metric(
        label="Số tiền gốc",
        value=f"{so_tien_gui:,.0f} VNĐ"
    )

with col_res2:
    st.metric(
        label="Tiền lãi nhận được",
        value=f"{tien_lai:,.0f} VNĐ"
    )

with col_res3:
    st.metric(
        label="Tổng tiền thu về",
        value=f"{tong_tien:,.0f} VNĐ"
    )

# Giải thích công thức áp dụng
st.info(
    f"""
    💡 **Thông tin tính toán:**
    - **Lãi suất mỗi tháng:** {r_thang * 100:.4f}%
    - **Hình thức áp dụng:** {loai_lai}
    - {"Công thức lãi đơn: $T = P + (P \\times r \\times n)$" if loai_lai == "Lãi đơn" else "Công thức lãi kép (dồn gốc theo tháng): $T = P \\times (1 + r)^n$"}
    """
)
