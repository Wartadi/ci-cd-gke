# 🚀 Deploy FastAPI dengan CI/CD ke GKE

Proyek ini merupakan implementasi pipeline **CI/CD** untuk melakukan deployment aplikasi **FastAPI** ke **Google Kubernetes Engine (GKE)** menggunakan **Cloud Build** dan **Artifact Registry**.

---

## 📁 Struktur Proyek

```
.
├── app/                        # Aplikasi FastAPI
│   └── main.py
├── kubernetes/
│   ├── deployment.yaml         # Konfigurasi deployment Kubernetes
│   └── service.yaml            # Service type LoadBalancer
├── Dockerfile                  # Konfigurasi container Docker
├── cloudbuild.yaml             # Pipeline CI/CD dengan Cloud Build
├── requirements.txt            # Dependensi aplikasi
└── README.md                   # Dokumentasi proyek
```

---

## 🎯 Tujuan

- Membangun image Docker dari aplikasi FastAPI
- Push image ke Artifact Registry
- Deploy otomatis ke GKE saat push ke GitHub
- Menampilkan dokumentasi Swagger UI FastAPI secara publik

---

## ⚙️ Langkah-Langkah

### 1. Build & Push Image Otomatis

File `cloudbuild.yaml` akan:
- Build image:
  ```
  us-central1-docker.pkg.dev/upbeat-polygon-461418-g5/fastapi-repo/fastapi-app:latest
  ```
- Push ke Artifact Registry

### 2. Deployment ke GKE

Cloud Build akan:
- Autentikasi ke cluster `ci-cd-cluster` di zona `us-central1-a`
- Deploy ke GKE menggunakan:
  - `kubernetes/deployment.yaml`
  - `kubernetes/service.yaml`

---

## 🔁 Trigger CI/CD

Trigger otomatis berjalan saat ada push ke branch `main` pada repo GitHub ini.

---

## 🌐 Akses API FastAPI

Setelah deploy berhasil, buka:
```
http://[EXTERNAL-IP]/docs
```

Untuk mendapatkan IP publik:
```bash
kubectl get service
```

---

## 💰 Budget Alert GCP

Sebagai bagian dari praktik monitoring, budget alert telah dibuat di akun billing GCP untuk mencegah pembengkakan biaya.

📸 Screenshot Budget Alert:

![Budget Alert](assets/budget_alert.png)

Gambar ini menunjukkan konfigurasi alert batas anggaran pada project GCP untuk mencegah kelebihan biaya.

---

## 🛡️ Hak Akses IAM

Service account berikut telah diberi role:

- `Cloud Build`:  
  `302297244128@cloudbuild.gserviceaccount.com`  
  ✅ `Artifact Registry Writer`  
  ✅ `Kubernetes Engine Developer`  
  ✅ `Service Account User`

- `GKE Node`:  
  `302297244128-compute@developer.gserviceaccount.com`  
  ✅ `Artifact Registry Reader`

---

## 👨‍💻 Dibuat oleh

**Wartadi AI Engineer Fellowship**