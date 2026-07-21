# Analisis Data Penyewaan Sepeda (Bike Sharing) 2011-2012

Proyek ini adalah analisis data komprehensif mengenai sistem penyewaan sepeda (bike sharing) selama periode 2011 hingga 2012 yang bertujuan untuk menggali wawasan strategis terkait pola perilaku pengguna, pengaruh faktor lingkungan (cuaca dan musim), serta segmentasi permintaan untuk membantu optimalisasi operasional bisnis.

---

## Dataset

Analisis ini menggunakan **Bike Sharing Dataset**, yaitu data historis penyewaan sepeda dari sistem *Capital Bikeshare* (Washington D.C.) yang mencakup catatan agregat per jam dan per hari selama tahun 2011 hingga 2012, lengkap dengan informasi musim dan parameter cuaca.

* **Link/Sumber:** [Kaggle - Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

---

## Tech Stack

Proyek ini dibangun dan dianalisis menggunakan ekosistem Python berikut:

*   **Pandas:** Untuk manipulasi dan pembersihan data.
*   **NumPy:** Untuk komputasi numerik dan operasi array.
*   **Matplotlib & Seaborn:** Untuk pembuatan visualisasi data yang statis dan informatif.
*   **Streamlit:** Untuk membangun *dashboard* interaktif yang menampilkan hasil analisis.

---

## Pertanyaan Bisnis

Analisis ini difokuskan untuk menjawab lima pertanyaan kunci berikut:

1. Pada musim apakah terjadi rata-rata penyewaan sepeda tertinggi di tahun 2011-2012?
2. Bagaimana kondisi cuaca pada tahun 2011-2012 dapat memengaruhi jumlah penyewaan sepeda?
3. Bagaimana perbedaan jumlah penyewaan sepeda pada hari kerja (*weekday*) dan akhir pekan (*weekend*) pada tahun 2011-2012?
4. Bagaimana pengaruh parameter cuaca terhadap jumlah penyewaan sepeda pada tahun 2011-2012?
5. Bagaimana perbedaan perilaku pengguna *casual* dan *registered* ketika menyewa sepeda di tahun 2011-2012?

---

## Analisis Lanjutan

Selain menjawab pertanyaan dasar, analisis ini juga mencakup **Segmentasi Demand Berdasarkan Musim dan Cuaca**. Pendekatan ini digunakan untuk memetakan kondisi spesifik kapan permintaan berada pada titik tertinggi (*peak*) dan terendah (*drop*), sehingga strategi alokasi sepeda dapat disesuaikan secara dinamis berdasarkan prakiraan cuaca.

---

## Hasil Analisis

Berdasarkan analisis yang telah dilakukan, berikut adalah wawasan bisnis yang ditemukan:

*   **Pola Musiman (Seasonality):** Siklus bisnis *bike sharing* sangat dipengaruhi oleh perubahan musim. Musim Gugur (*Fall*) merupakan periode emas (*peak season*) dengan performa tertinggi akibat suhu yang ideal. Sebaliknya, Musim Semi (*Spring*) menjadi titik terendah bisnis (*low season*) karena kendala suhu transisi yang dingin dan infrastruktur jalan yang basah/becek.
*   **Dampak Cuaca:** Kondisi cuaca cerah (*Clear/Partly Cloudy*) adalah pemicu mutlak (*key driver*) untuk mencapai target penjualan tertinggi (*High Demand*). Sebaliknya, cuaca buruk seperti mendung, hujan lebat, atau salju secara signifikan melumpuhkan minat bersepeda, sehingga performa bisnis anjlok ke level paling rendah.
*   **Dikotomi Hari (Weekday vs Weekend):** Terdapat perbedaan fungsi penggunaan sepeda yang sangat jelas. Pada hari kerja (*Weekday*), sepeda berfungsi sebagai transportasi komuter yang kaku (terpusat pada jam masuk/pulang kantor pukul 08:00 dan 17:00). Pada akhir pekan (*Weekend*), fungsi bergeser total menjadi moda rekreasi fleksibel dengan aktivitas puncak di siang hari (12:00–16:00).
*   **Parameter Cuaca Ideal (Comfort Zone):** Tingkat penyewaan sepeda mencapai titik optimal hanya ketika berada pada zonasi nyaman termal manusia: suhu udara hangat (25-30°C), kelembapan moderat (40-50%), dan kecepatan angin sepoi-sepoi (10-20 km/jam). Penyimpangan ekstrem (terlalu dingin, gerah, atau angin kencang) otomatis menurunkan volume penyewaan.
*   **Perilaku Pengguna:** Basis pengguna *Registered* adalah penggerak roda bisnis utama di hari kerja, menggunakan sepeda untuk utilitas harian (bekerja/sekolah). Sebaliknya, pengguna *Casual* adalah pasar potensial musiman yang sangat bergantung pada momentum hari libur untuk aktivitas rekreasi dan olahraga.

---

## Rekomendasi

Berdasarkan hasil analisis, berikut adalah rekomendasi yang dapat diberikan

### 1.  Manajemen Armada dan Operasional
*   **Optimalisasi Musim Gugur**: Lakukan pemeliharaan menyeluruh sebelum musim gugur agar seluruh unit siap beroperasi guna menyerap volume permintaan tertinggi.
*   **Efisiensi Musim Semi**: Jadwalkan perawatan besar dan pergudangan sebagian armada pada musim semi untuk menekan biaya operasional saat permintaan sepi.
Fasilitas Tambahan: Lengkapi sepeda dengan penahan cipratan air (spakbor) untuk mengantisipasi jalur yang basah akibat pencairan salju di musim semi.
### 2.  Distribusi Armada Berbasis Waktu
*   **Logistik Hari Kerja**: Pastikan ketersediaan unit di area perumahan sebelum pukul 08:00, lalu geser distribusi ke area perkantoran menjelang pukul 17:00.
*   **Logistik Akhir Pekan**: Alihkan konsentrasi armada dari kawasan bisnis ke pusat wisata, taman, dan area olahraga sebelum pukul 12:00 hingga 16:00.
### 3.  Strategi Pemasaran dan Segmentasi
*   **Retensi Pengguna Terdaftar**: Tawarkan program loyalitas atau paket khusus korporasi/kampus untuk menjaga konsistensi transaksi pada hari kerja.
*   **Aktivasi Pengguna Kasual**: Sediakan paket khusus akhir pekan yang diintegrasikan dengan rute wisata kota untuk menarik minat pesepeda rekreasi.
### 4.  Promosi Berbasis Kondisi Cuaca
*   **Notifikasi Kontekstual**: Kirimkan promosi otomatis melalui aplikasi saat indikator cuaca menunjukkan kondisi cerah dan suhu berada di zona nyaman.
*   **Insentif Cuaca Redup**: Berikan potongan harga atau poin ekstra pada hari mendung untuk merangsang permintaan dan menjaga stabilitas transaksi.

---

## 🚀 Cara Menjalankan Dashboard

### Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal
```
mkdir bike_sharing_analysis
cd bike_sharing_analysis
pipenv install
pipenv shell
pip install -r requirements.txt
```

### Run steamlit app
```
streamlit run dashboard.py
```