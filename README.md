# ANALISIS SENTIMEN RESPONS MASYARAKAT TERHADAP PENGGUNAAN CHATGPT MENGGUNAKAN KOMBINASI METODE VADER DAN ROBERTA PADA MEDIA SOSIAL TWITTER
Sebuah studi kuantitatif pada lebih dari 2 ribu tweet tentang ChatGPT, dimulai dari data crawling, data preprocessing, feature engineering, modelling, sentiment analysis, dan deployment.

## PEMBUAT
Name : Yogi Saputra

## DAFTAR ISI
- [Latar Belakang]
- [Objek]
- [Metodologi]
  - [Alat]
  - [Data Aqcuisition]
  - [Data Preprocessing]
  - [Feature Engineering]
  - [Data Modeling]
  - [Sentiment Analysis]
  - [Data Visualization]
- [Kesimpulan]
- [Referensi]

<hr>

## LATAR BELAKANG
ChatGPT adalah chatbot kecerdasan buatan yang dikembangkan oleh OpenAI dan diluncurkan pada November 2022. Chatbot ini dibangun di atas rangkaian model bahasa besar keluarga GPT-3 OpenAI dan telah disempurnakan (sebuah pendekatan untuk pembelajaran transfer) menggunakan teknik pembelajaran yang diawasi dan penguatan. . Mengingat keunggulan ChatGPT dibandingkan chatbot tradisional, ChatGPT telah menarik lebih dari 1 juta pengguna dalam 5 hari dan 100 juta pengguna dalam 2 bulan setelah diluncurkan, meninggalkan platform online populer lainnya seperti Netflix, Facebook, dan Instagram dalam hal adopsi. tarif. Beberapa pengguna awal ChatGPT percaya bahwa hal ini pada akhirnya akan menghilangkan beberapa profesi yang berkaitan dengan pembuatan konten. telah dibuktikan bahwa ChatGPT mampu menghasilkan respons berkualitas tinggi terhadap berbagai tantangan, termasuk memecahkan tantangan pengkodean dan menghasilkan respons akurat terhadap pertanyaan ujian.

<hr>

## OBJEK
Analisis tweet dari Agustus 2023 hingga Oktober 2023 yang menyebutkan ChatGPT dan mengungkapkan opini yang beragam dan tidak terstruktur. Identifikasi topik dan sentimen utama percakapan dan periksa persepsi pengguna awal ChatGPT. Kami menegaskan identifikasi ini akan memungkinkan kami memahami dan menilai kemampuan, efektivitas, dan tantangan ChatGPT. 

**RUMUSAN MASALAH**
- **RM1** Bagaimana mengimplementasikan kombinasi metode VADER dan RoBERTa
untuk analisis sentimen yang terkait dengan tweet-tweet tentang ChatGPT?
- **RM2** Bagaimana tingkat akurasi dan performa metode VADER dan RoBERTa
dalam menganalisis sentimen yang terkait dengan tweet-tweet tentang
ChatGPT?
<hr>

## METODOLOGI

### ALAT
<table style="width:100%">
  <tr>
    <th>Tugas</th>
    <th>Deskripsi</th> 
    <th>Alat / Paket</th>
  </tr>
  <tr>
    <td>Data Acquisition</td>
    <td>Crawling tweet-tweet dari
Twitter </td> 
    <td>Harvest</td>
  </tr>
  <tr>
    <td>Data Preprocessing</td>
    <td>Duplicate removal, cleansing,
case folding, tokenizing, stop
words removal, lemmatization</td> 
    <td>re, NLTK, pandas, numpy</td>
  </tr>
  <tr>
    <td>Feature Engineering</td>
    <td>Topic modelling menggunakan
LDA </td> 
    <td>pyLDAvis, gensim</td>
  </tr>
  <tr>
    <td>Sentiment Analysis</td>
    <td>Analisis sentimen kuantitatif
dari setiap topik melalui model
berbasis aturan dan model
berbasis deep learning</td> 
    <td>VADER,
roBERTa, scipy,
torch</td>
  </tr>
  <tr>
    <td>Data Visualization</td>
    <td>Multi-attribute plots</td> 
    <td>matplotlib, seaborn</td>
  </tr>
  <tr>
    <td>Environments & Platforms</td>
    <td> </td> 
    <td>Google Colab, VS Code, Jupyter Notebook, Twitter, Flask</td>
  </tr>
</table><br>

<h4> Data Acquisition: Bahan Penelitian </h4>

<li>Paket yang digunakan: harvest</li>
<li>Bahasa: Inggris</li>
<li>Kata kunci: ChatGPT</li>
<li>Waktu: 1 Agustus hingga 31 Oktober 2023</li>
<li>Struktur: User Name, Tweet Text, Date, dan Language</li>
<li>Jumlah yang dikumpulkan = 2012 tweet</li>
<hr>

### DATA-PREPROCESSING
- Menghapus tweet duplikat.
- Menghapus karakter yang tidak perlu.
- Menjadikan huruf menjadi kecil semua
- Tokenisasi
- Menghapus kata umum atau kata penghubung
- Menjadikan kata yang digunakan menjadi kata baku sesuai maknanya.


**Feature Engineering**
Pada penelitian ini menggunakan teknik pemodelan Latent Dirichlet Allocation (LDA) yang tidak terawasi digunakan untuk
mengekstraksi sejumlah topik utama dari tweet yang dikumpulkan. Dibuat kamus dan korpus yang berisi semua teks tweet, dengan menyaring katakata ekstrem yang muncul dengan frekuensi rendah atau tinggi (muncul dalam kurang dari 10 tweet atau lebih dari 50% tweet). Proses ini menerapkan LDA menggunakan modul LdaMulticore dalam library Gensim. Kemudian melakukan serangkaian eksperimen dengan variasi jumlah topik (N) dari 2 hingga 40, dan memperoleh skor kohesi yang
relatif tinggi untuk rentang 4 hingga 7 topik. Setelah itu, menjalankan LDA dengan N=4 dan mengidentifikasi 4 topik berdasarkan tweet yang sangat relevan untuk setiap topik.


### DATA-MODELING
Modelling merupakan fase dalam pengembangan analisis sentimen di mana dilakukan proses pemodelan model yang mampu melakukan pelabelan data tweet kemudian mengklasifikasikan tweet tersebut ke dalam kategori sentimen yang sesuai. Data yang digunakan sebagai pelatihan untuk model ini adalah data yang telah melalui tahapan sebelumnya. Pemodelan dilakukan dengan kombinasi dua metode yaitu menggunakan VADER dan RoBERTa. 

**Sentiment Analysis**
Setelah berhasil melatih model kombinasi VADER dan RoBERTa pada data sentimen terkait ChatGPT, langkah selanjutnya adalah melakukan analisis terhadap hasilnya. Pada tahap ini adalah bagian mengeksplorasi pola-pola sentimen yang terungkap dari tweet-tweet yang dihasilkan oleh pengguna terkait ChatGPT. Hasil analisis ini memberikan wawasan mendalam mengenai bagaimana masyarakat merespons penggunaan ChatGPT di media sosial Twitter dari dataset yang telah
diambil. Dalam penelitian ini, menggunakan metode VADER (rule-based model) dari perpustakaan NLTK yang dikombinasikan dengan Twitter roBERTa (deep learning based) dari paket TRANSFORMERS untuk mengeksplorasi sikap pengguna terhadap ChatGPT. 

<hr>

## DATA VISUALIZATION
Data Visualisasi ini untuk membantu memahami hasil analisis sentimen. Beberapa teknik visualisasi yang umum digunakan termasuk plot grafik untuk menunjukkan seberapa baik model bekerja dalam mengklasifikasikan sentimen positif, negatif, atau netral, atau word clouds untuk menunjukkan kata-kata yang paling sering muncul dalam dataset. Dalam penelitian ini, visualisasi data selain memakai library dari python juga yaitu menggunakan flask agar dapat membantu deployment secara sederhana untuk memudahkan menggunakan model yang telah dibuat serta mengidentifikasi pola dan tren dalam data teks dan membantu mengambil keputusan yang lebih baik berdasarkan hasil analisis. Selain itu, integrasi dengan Flask memungkinkan pengguna untuk berinteraksi dengan visualisasi melalui antarmuka web yang user-friendly, sehingga analisis dapat diakses lebih mudah yang lebih luas tanpa memerlukan pengetahuan teknis yang mendalam. Dengan demikian, visualisasi data tidak hanya meningkatkan interpretabilitas hasil analisis tetapi juga memainkan peran kunci dalam menyampaikan temuan kepada pemangku kepentingan dan mendukung pengambilan keputusan yang didasarkan pada data.

## CONCLUSION
Penerapan Latent Dirichlet Allocation untuk mengidentifikasi topik dan
kombinasi metode VADER dengan algoritma RoBERTa untuk pembuatan sistem
model analisis sentimen sebagai model untuk mengetahui respons masyarakat
terhadap ChatGPT. Hal ini ditunjukkan dengan proses pengambilan dan
pengolahan data dengan jumlah 984 data memberikan informasi respons
masyarakat terhadap teknologi ChatGPT. Pengukuran akurasi dilakukan dengan
menggunakan confusion matrix sebanyak dua metode, yaitu secara manual dan
otomatis. Pada metode manual, data uji sebanyak 25 data dipilih secara manual
untuk diuji terhadap dataset. Sementara itu, metode otomatis menggunakan
dataset lebih besar dari kaggle sebesar 2000 data. Hasil pengujian manual
menunjukkan akurasi sebesar 92%, dengan total prediksi benar sebanyak 23 dari
25 data. Sementara pada pengujian otomatis dengan data sebanyak 2000 data,
akurasi mencapai 98%. Rata-rata akurasi dari kedua metode ini adalah 95%,
menunjukkan bahwa sistem model ini menghasilkan kinerja yang sangat baik
dalam melakukan prediksi 

<hr>

## REFERENSI
- Chandrasekaran, Ranganathan, et al. "Examining public sentiments and attitudes toward COVID-19 vaccination: infoveillance study using Twitter posts." JMIR infodemiology 2.1 (2022): e33909.
- Haque, Mubin Ul, et al. "" I think this is the most disruptive technology": Exploring Sentiments of ChatGPT Early Adopters using Twitter Data." arXiv preprint arXiv:2212.05856 (2022).
- Scraping Tweets with snscrape: https://github.com/rashidesai24/Analyzing-Twitter-Trends-On-COVID-19-Vaccinations#-data-coverage-
- Topic Modeling: https://medium.com/@kurtsenol21/topic-modeling-lda-mallet-implementation-in-python-part-1-c493a5297ad2
- Sentiment Analysis: https://medium.com/@amanabdulla296/sentiment-analysis-with-vader-and-twitter-roberta-2ede7fb78909

<hr>
