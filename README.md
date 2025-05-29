## Penjelasan 
ini adalah script simpel yang digunakan untuk mengunduh audio/video TikTok, hanya cukup dengan menginput url.

![Foto](https://files.catbox.moe/yy196m.jpg)

### Instalsi Di Termux
1. Unduh paket penting
```
pkg update && pkg upgrade -y
pkg install git -y
pkg install python -y
pip install requests urllib3
```
2. Izinkan akses file
```
termux-setup-storage
```
3. Clone repository dan jalankan
```
git clone https://github.com/HanX-ID/ttdown
cd ttdown
python main.py
```

Author [HanX](https://github.com/HanX-ID)
