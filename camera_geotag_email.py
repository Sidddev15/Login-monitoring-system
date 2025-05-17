import os
import cv2
import yagmail
import requests
from datetime import datetime
from dotenv import load_dotenv
import time

time.sleep(15)

load_dotenv()  # Loads credentials from .env file

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# Step 1: Get approximate location based on IP
def get_location():
    try:
        # Using ipinfo.io to get location by IP address
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        city = data.get("city", "Unknown City")
        region = data.get("region", "Unknown Region")
        country = data.get("country", "Unknown Country")
        loc = f"{city}, {region}, {country}"
        return loc
    except Exception as e:
        print(f"Location lookup failed: {e}")
        return "Location lookup failed"

# Step 2: Capture image
def capture_image(filename="capture.jpg"):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Camera not accessible")
        return None
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(filename, frame)
    cam.release()
    return filename if ret else None

# Step 3: Email it
def send_email(image_path, location):
    subject = "📸 Linux Login Detected!"
    body = f"Login time: {datetime.now()}\nLocation: {location}"

    try:
        yag = yagmail.SMTP(EMAIL_SENDER, EMAIL_PASSWORD)
        yag.send(to=EMAIL_RECEIVER, subject=subject, contents=body, attachments=image_path)
        print("✅ Email sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    image_file = capture_image()
    if image_file:
        loc = get_location()
        send_email(image_file, loc)
        os.remove(image_file)
    else:
        print("Failed to capture image")



# For Logging
with open("/tmp/camera_mail_log.txt", "a") as log:
    log.write(f"{datetime.now()} - Script started\n")

image_file = capture_image()
if image_file:
    loc = get_location()
    send_email(image_file, loc)
    os.remove(image_file)
    with open("/tmp/camera_mail_log.txt", "a") as log:
        log.write(f"{datetime.now()} - Email sent with image {image_file}\n")
else:
    with open("/tmp/camera_mail_log.txt", "a") as log:
        log.write(f"{datetime.now()} - Failed to capture image\n")
