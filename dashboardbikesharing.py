import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # Import matplotlib

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
plt.figure(figsize=(10, 6))

# Grafik pertama: Tingkat Penggunaan Sepeda Sharing per Bulan
month_usage = day_df.groupby('mnth')['cnt'].mean()
plt.bar(month_usage.index, month_usage.values, color='skyblue')
plt.title('Tingkat Penggunaan Sepeda Sharing per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Peminjaman')
plt.xticks(rotation=0)
st.pyplot()

# Grafik kedua: Perbandingan Pola Penggunaan Sepeda Sharing pada Hari Kerja dan Hari Libur
plt.figure(figsize=(10, 6))
holiday_usage = day_df.groupby('holiday')['cnt'].mean()
plt.bar(holiday_usage.index, holiday_usage.values, color=['lightgreen', 'lightcoral'])
plt.title('Perbandingan Pola Penggunaan Sepeda Sharing pada Hari Kerja dan Hari Libur')
plt.xlabel('Hari')
plt.ylabel('Jumlah Peminjaman')
plt.xticks(rotation=0)
st.pyplot()
