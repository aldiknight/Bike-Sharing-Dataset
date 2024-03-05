import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
hour_df = pd.read_csv("hour.csv")
day_df = pd.read_csv("day.csv")

# Set judul dashboard
st.title('Dashboard Data Sepeda Sharing')

# Deskripsi singkat
st.write("""
Ini adalah dashboard interaktif untuk menganalisis data sepeda sharing.
Anda dapat menyesuaikan pengaturan di sebelah kiri.
""")

# Tambahkan komponen interaktif
option = st.sidebar.selectbox(
    'Pilih jenis data:',
    ('Data per Jam', 'Data per Hari')
)

if option == 'Data per Jam':
    st.write(hour_df)
else:
    st.write(day_df)

# Visualisasikan data
st.write("## Visualisasi Data")

if option == 'Data per Jam':
    # Visualisasi data per jam
    st.line_chart(hour_df['cnt'])
else:
    # Visualisasi data per hari
    st.line_chart(day_df['cnt'])

# Tambahkan dua grafik tambahan
fig1, ax1 = plt.subplots(figsize=(10, 6))
month_usage = day_df.groupby('mnth')['cnt'].mean()
ax1.bar(month_usage.index, month_usage.values, color='skyblue')
ax1.set_title('Tingkat Penggunaan Sepeda Sharing per Bulan')
ax1.set_xlabel('Bulan')
ax1.set_ylabel('Jumlah Peminjaman')
ax1.set_xticks(month_usage.index)

fig2, ax2 = plt.subplots(figsize=(10, 6))
holiday_usage = day_df.groupby('holiday')['cnt'].mean()
ax2.bar(holiday_usage.index, holiday_usage.values, color=['lightgreen', 'lightcoral'])
ax2.set_title('Perbandingan Pola Penggunaan Sepeda Sharing pada Hari Kerja dan Hari Libur')
ax2.set_xlabel('Hari')
ax2.set_ylabel('Jumlah Peminjaman')
ax2.set_xticks(holiday_usage.index)

# Tampilkan grafik-garik menggunakan st.pyplot()
st.pyplot(fig1)
st.pyplot(fig2)
