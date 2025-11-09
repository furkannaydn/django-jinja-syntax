# Furkan Aydın GitHub Projeleri README Koleksiyonu

Bu dosya, Furkan Aydın’ın GitHub projelerinin detaylı README’lerini içerir.  
Her proje için hem Türkçe 🇹🇷 hem İngilizce 🇬🇧 açıklamalar, kullanılan teknolojiler, özellikler ve öğrenilenler yer almaktadır.

---

## 1️⃣ django_sql_project

# 🧩 Django SQL Project  

> 📌 *Demonstrating raw SQL usage inside Django*

---

## 🇹🇷 Türkçe Açıklama  

**Django SQL Project**, Django framework içinde **raw SQL (doğrudan SQL sorguları)** kullanarak veri tabanı işlemleri yapmayı öğreten bir projedir.  
Bu proje, ORM (Object Relational Mapper) yerine SQL sorgularını manuel olarak yazmayı göstererek **daha fazla kontrol ve performans optimizasyonu** sağlar.  

Proje, CRUD işlemlerinin (Create, Read, Update, Delete) SQL ile nasıl yapıldığını, Django ile birlikte nasıl entegre edilebileceğini öğretir. Bu sayede **veritabanı mantığı**, **performans optimizasyonu** ve **backend veri akışı** kavramları daha iyi anlaşılır.

### 🔍 Anahtar Kavramlar  

| Kavram | Açıklama |
|--------|-----------|
| **ORM** | Python sınıflarını veritabanı tablolarına dönüştürür. SQL yazmadan veri işlemlerini sağlar. |
| **Raw SQL** | SQL komutlarını manuel olarak yazmak. Karmaşık sorgular ve performans optimizasyonu için kullanılır. |
| **QuerySet** | Django’nun veritabanı sorgularını temsil eden nesnesi. |
| **Database Layer** | Django’nun farklı veritabanları ile uyumlu çalışmasını sağlayan katman. |

### 🔧 Kullanılan Teknolojiler  

| Teknoloji | Amaç |
|-----------|------|
| Python 🐍 | Backend kodlama |
| Django 🌐 | Web framework |
| SQLite / PostgreSQL 💾 | Veritabanı yönetimi |
| SQL | Veri sorgulama, ekleme, silme, güncelleme |

### ⚙️ Kurulum ve Çalıştırma  

1. Repo’yu klonlayın:  
```bash
git clone https://github.com/furkannaydn/django_sql_project.git

Sanal ortam oluşturun ve aktifleştirin:

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows


Gerekli paketleri yükleyin:

pip install -r requirements.txt


Veritabanını migrate edin:

python manage.py migrate


Sunucuyu çalıştırın:

python manage.py runserver


Tarayıcıdan http://127.0.0.1:8000/ adresine gidin.

🚀 Özellikler / Features

SQL sorgularının Django içinde kullanımı

CRUD işlemleri: veri ekleme, görüntüleme, güncelleme, silme

ORM ve raw SQL karşılaştırması

Performans optimizasyonu ve hata yönetimi

🧠 Öğrenilenler / Learning Outcomes

ORM ve SQL farklarını kavrama

Django ile veritabanı entegrasyonu

SQL sorgularını backend ile bağlama

Veritabanı performansı ve güvenlik önlemleri

🇬🇧 English Description

Django SQL Project is an educational project demonstrating raw SQL queries inside Django.
Instead of using ORM (Object Relational Mapper), it shows how to manually write SQL commands for better control and performance optimization.

The project demonstrates CRUD operations, backend integration with SQL, and teaches database concepts and performance awareness.

🔍 Key Concepts
Concept	Description
ORM	Converts Python classes to database tables. Allows DB operations without SQL.
Raw SQL	Manual SQL queries. Useful for complex operations and optimization.
QuerySet	Django object representing database query results.
Database Layer	Layer that allows Django to interact with different databases seamlessly.
🔧 Technologies
Technology	Purpose
Python 🐍	Backend programming
Django 🌐	Web framework
SQLite / PostgreSQL 💾	Database management
SQL	Data manipulation (SELECT, INSERT, UPDATE, DELETE)
⚙️ Installation

Clone the repo:

git clone https://github.com/furkannaydn/django_sql_project.git


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Run server:

python manage.py runserver


Open browser at http://127.0.0.1:8000/

🚀 Features

SQL queries inside Django

CRUD operations

ORM vs Raw SQL demonstration

Performance optimization and error handling

🧠 Learning Outcomes

Understand difference between ORM and raw SQL

Integrate SQL queries with Django backend

Handle database performance and security

Apply database operations programmatically

