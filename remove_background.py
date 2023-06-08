import cv2
import numpy as np

def remove_background(image_path, output_path, canny_low, canny_high, dilate_iter, erode_iter):
    # Resmi oku
    image = cv2.imread(image_path)

    # Resmi GRAYSCALE'e dönüştür
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Kenar tespiti için Canny uygula
    canny = cv2.Canny(gray, canny_low, canny_high)

    # Kenarları genişletmek için bir çekirdek tanımla
    kernel = np.ones((3, 3), np.uint8)

    # Genişletme ve erozyon işlemlerini uygula
    dilated = cv2.dilate(canny, kernel, iterations=dilate_iter)
    eroded = cv2.erode(dilated, kernel, iterations=erode_iter)

    # Konturları bul
    contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Konturların alanını hesapla ve en büyük olanı seç
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour

    # Maske oluştur
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [max_contour], -1, (255), thickness=cv2.FILLED)

    # Alfa kanalı oluştur
    alpha = np.ones(image.shape[:2], dtype=np.uint8) * 255
    alpha = cv2.bitwise_and(alpha, alpha, mask=mask)

    # RGB renk uzayında transparan kanalı eklemek için resmi dönüştür
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # Alfa kanalını ekle
    image[:, :, 3] = alpha

    # Resmi kaydet
    cv2.imwrite(output_path, image)

# Test
image_path = 'input.jpg'
output_path = 'output.png'
canny_low = 20  # Kenar algılama için alt eşik değeri (düşük kontrastlı kenarları tespit etmek için)
canny_high = 0.9  # Kenar algılama için üst eşik değeri (yüksek kontrastlı kenarları tespit etmek için)
dilate_iter = 10  # Kenarları genişletmek için tekrarlama sayısı (keskin kenarları tamamlamak için)
erode_iter = 11  # Kenarları aşındırmak için tekrarlama sayısı (gürültüyü azaltmak için)

remove_background(image_path, output_path, canny_low, canny_high, dilate_iter, erode_iter)

