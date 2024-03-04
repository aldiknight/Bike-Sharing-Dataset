import streamlit as st
import pandas as pd
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


