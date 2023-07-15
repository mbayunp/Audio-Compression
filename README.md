# Audio-Compression
Program untuk mengenali teks dari suara menggunakan Speech Recognition dan membuat tulisan tangan dari teks tersebut pada gambar latar belakang. Berikut adalah penjelasan dan tahapan proses dalam kode tersebut:

1. Import Library: Pertama, kita mengimpor beberapa library yang diperlukan yaitu `speech_recognition` untuk mengenali teks dari suara, `os` untuk mengakses sistem operasi, `cv2` untuk membaca dan menampilkan gambar, dan `PIL` (Python Imaging Library) untuk memanipulasi gambar.

2. Membuat Objek Recognizer: Kode membuat objek `Recognizer` dari library Speech Recognition menggunakan `sr.Recognizer()`.

3. Menggunakan Microphone sebagai Source Suara: Kode menggunakan microphone sebagai sumber suara menggunakan `sr.Microphone()` sebagai konteks. Selanjutnya, program akan menunggu input suara dari pengguna.

4. Mengenali Teks: Suara yang ditangkap dari microphone akan disimpan dalam variabel `audio`. Program akan mencoba mengenali teks dari audio menggunakan `r.recognize_google(audio, language='id-ID')` dengan menggunakan Google Speech Recognition dan bahasa Indonesia. Hasil teks yang dikenali akan disimpan dalam variabel `text`.

5. Menampilkan Teks yang Dikenali: Hasil teks yang dikenali akan dicetak menggunakan `print()`. Pengguna akan melihat teks yang berhasil dikenali dari suara yang diucapkan.

6. Membaca Gambar Latar Belakang: Kode membuka gambar latar belakang yang disimpan dalam file "polio.png" menggunakan `Image.open("polio.png")` dan menyimpannya dalam variabel `background_image`.

7. Menentukan Ukuran dan Font Tulisan Tangan: Kode menentukan ukuran font dan path font tulisan tangan yang akan digunakan. Ukuran font ditentukan dalam variabel `font_size` dan path font disimpan dalam variabel `font_path`.

8. Menggambar Tulisan Tangan: Kode menggunakan objek `ImageDraw` untuk menggambar teks tulisan tangan di atas gambar latar belakang. Teks tulisan tangan diambil dari teks yang telah dikenali sebelumnya. Koordinat awal posisi tulisan tangan ditentukan oleh `(x, y)`.

9. Menyimpan Gambar Hasil: Gambar hasil dengan teks tulisan tangan akan disimpan dengan nama file "result.png" menggunakan `background_image.save(result_filename)`.

10. Menampilkan Gambar Hasil: Kode menggunakan `cv2` untuk membaca gambar hasil dari file yang disimpan. Gambar hasil akan ditampilkan menggunakan `cv2.imshow()` dengan judul "Tulisan Tangan". Program akan menunggu hingga pengguna menutup jendela gambar.

Demikian penjelasan tentang kode program yang diberikan. Kode tersebut membantu dalam mengenali teks dari suara pengguna, membuat tulisan tangan dari teks tersebut pada gambar latar belakang, dan menampilkan gambar hasil dengan tulisan tangan.
