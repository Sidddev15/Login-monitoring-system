# 🔐 BootCam - Capture Image and Geolocation on Linux Startup

BootCam is a lightweight Python-based tool that runs on Linux systems. Every time your system boots up, it silently captures a webcam snapshot, grabs the current location using IP-based geolocation, and sends it all to your email.

---

## 📸 Features

- 📷 Captures image from your webcam on startup
- 🌍 Gets approximate location using IP geolocation
- 📧 Sends an automated email with image + location + timestamp
- 🐧 Designed for Linux startup automation using systemd
- 🔒 Great for personal device tracking and unauthorized access detection

---

## 🛠 Technologies Used

- Python 3
- `OpenCV` for camera access
- `yagmail` for sending emails
- `requests` for IP-based location
- `dotenv` for secure credentials
- `systemd` for Linux auto-start setup

---

## 🚀 How to Use

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/bootcam.git
cd bootcam
