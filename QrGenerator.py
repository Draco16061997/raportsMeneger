import qrcode
import os

def CreateQr(data, path = "./",name = "my_qr_code.png"):
    # Создайте объект QRCode
    qr = qrcode.QRCode(
        version=1,  # Размер QR-кода (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок (L, M, Q, H)
    )

    # Добавьте данные в QR-код
    qr.add_data(data)
    qr.make(fit=True)

    # Создайте изображение QR-кода (в этом случае, с использованием библиотеки Pillow)
    img = qr.make_image(fill_color="black", back_color="white")



    try:
        img.save(path + name)
    except:
        os.mkdir(path)
        img.save(path + name)



CreateQr("re","./QR/")

if __name__ == "__main__":
    pass