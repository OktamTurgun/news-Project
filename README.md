# 📰 News Project

Django asosida yaratilgan professional yangiliklar sayti loyihasi.  
Bu loyiha orqali foydalanuvchilar yangiliklarni ko'rishlari, kategoriyalar bo'yicha saralashlari, ro'yxatdan o'tishlari va batafsil ma'lumot olishlari mumkin.

## 🚀 Asosiy imkoniyatlar

- ✨ Yangiliklarni qo'shish, o'chirish va tahrirlash (admin panel orqali)
- 👤 Foydalanuvchi autentifikatsiyasi (ro'yxatdan o'tish, kirish, chiqish)
- 📱 Responsive (moslashuvchan) frontend dizayn
- 🗂 Kategoriyalar bo'yicha yangiliklarni saralash
- 🌐 Ko'p tilli qo'llab-quvvatlash (i18n / translations)
- 🏠 Bosh sahifada barcha yangiliklar ko'rinishi
- 🖼 Media fayllar bilan ishlash (rasmlar)
- ☁️ Cloud storage orqali media saqlash (Backblaze B2)
- 📞 Aloqa formasi
- 🔍 Qidiruv imkoniyati

## 🛠 Texnologiyalar

- **Backend:** Python 3.13+, Django 5.2
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Database:** PostgreSQL (production), SQLite (development)
- **Storage:** Backblaze B2 (django-storages + boto3)
- **Server:** Gunicorn + WhiteNoise
- **Media:** Pillow
- **Translation:** django-modeltranslation, deep-translator
- **Forms:** django-widget-tweaks

## ⚙️ O'rnatish va ishga tushirish

### 1. Repozitoriyani klonlash
```bash
git clone https://github.com/OktamTurgun/news-Project.git
cd news-Project
```

### 2. Virtual muhit yaratish
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Zarur kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4. Muhit o'zgaruvchilarini sozlash
`.env` fayl yarating va quyidagilarni kiriting:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url

# Backblaze B2 (ixtiyoriy, production uchun)
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_STORAGE_BUCKET_NAME=your_bucket
AWS_S3_ENDPOINT_URL=your_endpoint
```

### 5. Ma'lumotlar bazasini sozlash
```bash
python manage.py migrate
```

### 6. Superuser yaratish
```bash
python manage.py createsuperuser
```

### 7. Serverni ishga tushirish
```bash
python manage.py runserver
```

### 8. Saytni ko'rish
Brauzeringizda quyidagi manzilni oching: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## 📂 Loyiha tuzilmasi

```
news-Project/
├── manage.py
├── requirements.txt
├── README.md
├── LICENSE
├── news_backup.json
│
├── news_project/          # Asosiy loyiha sozlamalari
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── news_app/              # Yangiliklar ilovasi
│   ├── models.py          # Ma'lumotlar modellari
│   ├── views.py           # Ko'rinishlar
│   ├── urls.py            # URL marshrutlari
│   ├── forms.py           # Formalar
│   └── admin.py           # Admin panel sozlamalari
│
├── accounts/              # Foydalanuvchi autentifikatsiyasi
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── locale/                # Tarjima fayllari (i18n)
│
├── templates/             # HTML shablonlari
│   ├── base.html
│   ├── home.html
│   ├── news_detail.html
│   ├── category_detail.html
│   └── accounts/
│
├── static/                # Statik fayllar
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
│
└── media/news/images/     # Yuklangan rasmlar (local)
```

## 🎯 Asosiy funksiyalar

### Models
- **News** - Yangiliklar modeli
- **Category** - Kategoriyalar modeli
- **Contact** - Aloqa so'rovlari modeli

### Views
- Bosh sahifa
- Yangilik tafsilotlari
- Kategoriya bo'yicha yangliklarni ko'rish
- Aloqa sahifasi
- Foydalanuvchi ro'yxatdan o'tish / kirish / chiqish

### Admin Panel
Admin panel orqali quyidagilarni boshqarish mumkin:
- Yangiliklarni qo'shish, tahrirlash, o'chirish
- Kategoriyalarni boshqarish
- Foydalanuvchi so'rovlarini ko'rish
- Foydalanuvchilarni boshqarish

## 🌐 Ko'p tillilik (i18n)

Loyiha `django-modeltranslation` va `deep-translator` yordamida ko'p tillilikni qo'llab-quvvatlaydi. Tarjima fayllari `locale/` papkasida joylashgan.

Tarjima fayllarini yangilash:
```bash
python manage.py makemessages -l uz
python manage.py compilemessages
```

## 🔧 Sozlash

### Media fayllar
Production muhitida media fayllar **Backblaze B2** cloud storage orqali saqlanadi (`django-storages` + `boto3`). Development uchun fayllar `media/news/images/` papkasida saqlanadi.

### Static fayllar
Development muhitida Django static fayllarni avtomatik xizmat qiladi. Production uchun:
```bash
python manage.py collectstatic
```
Static fayllar **WhiteNoise** middleware orqali xizmat qilinadi.

## 📱 Responsive dizayn

Sayt barcha qurilmalarda (desktop, tablet, mobil) to'g'ri ishlaydi va Bootstrap framework asosida yaratilgan.

## 🚀 Production ga deploy qilish

Production muhiti uchun `gunicorn` web server ishlatiladi:
```bash
gunicorn news_project.wsgi:application
```

`python-decouple` yordamida maxfiy ma'lumotlarni `.env` fayldan oling.

## 🤝 Hissa qo'shish

1. Fork qiling
2. Feature branch yarating (`git checkout -b feature/AmazingFeature`)
3. O'zgarishlaringizni commit qiling (`git commit -m 'Add some AmazingFeature'`)
4. Branch'ni push qiling (`git push origin feature/AmazingFeature`)
5. Pull Request oching

## 🐛 Xatoliklar haqida xabar berish

Agar xatolik topsangiz, GitHub Issues bo'limida xabar bering.

## 👨‍💻 Muallif

**Uktam Turg'unov**
- GitHub: [@OktamTurgun](https://github.com/OktamTurgun)
- Email: uktamturgunov30@gmail.com

## 📄 Litsenziya

Ushbu loyiha MIT litsenziyasi asosida tarqatiladi. Batafsil ma'lumot uchun [LICENSE](LICENSE) faylini ko'ring.

## Minnatdorchilik

- Django jamoasiga framework uchun
- Bootstrap jamoasiga UI components uchun
- Barcha open-source kutubxona mualliflariga

---

⭐ Agar loyiha sizga yoqsa, star bosishni unutmang!