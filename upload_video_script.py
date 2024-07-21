from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time

# ChromeDriver'ı otomatik olarak yükle ve güncelle
chromedriver_autoinstaller.install()

# YouTube'da giriş yapmanız için gerekli kullanıcı adı ve şifre
youtube_username = "usurname@gmail.com"
youtube_password = "**********"

# Yüklenecek video dosyasının yolu
video_path = r"C:\Users\kullanıcı adı\Desktop\klasoradı"

# WebDriver'ı başlatma
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/?app=desktop&hl=tr")

# Giriş yapma
try:
    sign_in_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Giriş yap"]'))
    )
    sign_in_button.click()

    # Kullanıcı adını girme
    email_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    )
    email_input.send_keys(youtube_username)
    email_input.send_keys(Keys.RETURN)

    # Şifreyi girme
    password_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
    password_input.send_keys(youtube_password)
    password_input.send_keys(Keys.RETURN)
    
    # Giriş yapma işlemi tamamlanana kadar bekleme
    WebDriverWait(driver, 30).until(
        EC.url_contains("https://www.youtube.com")
    )
    
    # Video yükleme sayfasına gitme
    driver.get("https://www.youtube.com/upload")

    # Video dosyasını yükleme
    upload_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
    )
    upload_input.send_keys(video_path)

    # Video başlığını ve açıklamasını girme
    title_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="title"]'))
    )
    title_input.send_keys("Video Başlığı")

    description_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@name="description"]'))
    )
    description_input.send_keys("Video Açıklaması")

    # Yayınla butonuna tıklama
    publish_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="done-button"]'))
    )
    publish_button.click()

finally:
    # İşlemi bitirmek için bekleme ve tarayıcıyı kapatma
    time.sleep(10)
    driver.quit()
