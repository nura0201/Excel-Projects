
# Importing ToolKits
import pandas as pd
import numpy as np
import plotly.express as px


import streamlit as st
import warnings

# ----------------------------------------------------
# BAGIAN UTAMA APLIKASI STREAMLIT
# ----------------------------------------------------

# 1. Konfigurasi Halaman (Optional, tapi disarankan)
st.set_page_config(layout="wide", page_title="Dashboard Analisis Data")

# 2. Asumsi Anda punya file data bernama 'your_data.csv'
try:
    # Ganti 'your_data.csv' dengan nama file data Anda yang sebenarnya
    df = pd.read_csv("cleaned_sales_data.csv") 
except FileNotFoundError:
    st.error("File 'your_data.csv' tidak ditemukan. Pastikan file data ada di direktori yang sama.")
    st.stop() # Menghentikan eksekusi jika file tidak ditemukan

# 3. Menampilkan Hasil Visualisasi

st.title("Visualisasi Korelasi Data")

# Memanggil fungsi create_heat_map
# Pastikan data yang dimasukkan (df) adalah DataFrame yang valid
fig_heatmap = create_heat_map(df) 

# Menampilkan grafik ke Streamlit
st.plotly_chart(fig_heatmap, use_container_width=True)

# Contoh memanggil fungsi lain
st.header("Matriks Scatter")
fig_scatter = create_scatter_matrix(df)
st.plotly_chart(fig_scatter, use_container_width=True)

st.write("Aplikasi berhasil dijalankan!")