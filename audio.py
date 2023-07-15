import speech_recognition as sr
import os
import cv2
from PIL import Image, ImageDraw, ImageFont

# Membuat objek Recognizer
r = sr.Recognizer()

# Menggunakan microphone sebagai source suara
with sr.Microphone() as source:
    print("Silakan mulai berbicara...")
    audio = r.listen(source)

    try:
        print("Mengenali teks...")
        # Menggunakan Google Speech Recognition untuk mengenali teks dari audio dengan bahasa Indonesia
        text = r.recognize_google(audio, language='id-ID')
        print("Teks yang dikenali:")
        print(text)
    except sr.UnknownValueError:
        print("Maaf, Tidak dapat mengenali suara.")
    except sr.RequestError as e:
        print(f"Terjadi kesalahan pada Speech Recognition service: {e}")

# Membaca gambar latar belakang (polio.png)
background_image = Image.open("polio.png")

# Menentukan ukuran dan font tulisan tangan
font_size = 10
font_path = "hand.ttf"  # Ganti dengan path font yang Anda miliki
font = ImageFont.truetype(font_path, font_size)

# Mengatur posisi awal tulisan tangan
x, y = 50, 50

# Membuat objek ImageDraw dan menggambar teks tulisan tangan di atas gambar latar belakang
draw = ImageDraw.Draw(background_image)
draw.text((x, y), text, font=font, fill=(0, 0, 0))  # Menggunakan warna hitam untuk teks

# Menyimpan gambar hasil dengan teks tulisan tangan
result_filename = "result.png"
background_image.save(result_filename)

# Menampilkan pesan berhasil dan nama file hasil
print(f"Tulisan tangan berhasil dibuat dan disimpan dalam file: {result_filename}")

# Menampilkan gambar hasil
image = cv2.imread(result_filename)
cv2.imshow("Tulisan Tangan", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
