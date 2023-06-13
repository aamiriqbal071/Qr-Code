import qrcode

def generate_qrocde(text):
    qr=qrcode.QRCode(
    version=1,
    error_correction= qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color= "red", back_color="White")
    img.save("qrr.png")


generate_qrocde("MAAAALLIIIIIKKKKK !!!!!! MAAAAKIIIIILLLLLKKKK!!!! Iphone Mallliikkkkk!!! ")