# Proyek Analisis Data Bike Sharing

## Tujuan Proyek
Tujuan dari proyek ini adalah untuk menganalisis data sepeda sharing dan menjawab beberapa pertanyaan bisnis terkait pola penggunaan sepeda sharing dari bulan ke bulan dan antara hari kerja dan hari libur.

## 1. Memuat Data
Data diambil dari dua file CSV: `hour.csv` dan `day.csv`. Data dimuat ke dalam DataFrame menggunakan library pandas di Python.

## 2. Pemahaman Data
Kedua DataFrame, `hour_df` dan `day_df`, diperiksa struktur, tipe data, dan ringkasan statistiknya untuk memahami dataset tersebut.

## 3. Pemrosesan Data
Tipe data kolom tanggal (dteday) diubah menjadi tipe data datetime dan kolom baru untuk menunjukkan bulan dan hari kerja/libur ditambahkan ke dalam DataFrame.

## 4. Visualisasi Data
Visualisasi data dilakukan untuk membandingkan tingkat penggunaan sepeda sharing dari bulan ke bulan dan antara hari kerja dan hari libur menggunakan grafik bar plot.

## Kesimpulan
Berdasarkan analisis data, dapat disimpulkan bahwa terdapat pola musiman dalam penggunaan sepeda sharing dan perbedaan pola penggunaan antara hari kerja dan hari libur.

## Referensi
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
