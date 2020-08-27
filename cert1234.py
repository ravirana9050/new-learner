import cv2

def generate_certificate(img,name):
    copy_img = img.copy()
    font=cv2.FONT_HERSHEY_COMPLEX
    cordinates = (700,750)
    font_size = 3.5
    font_color = (51,51,51)
    font_thickness = 10
    cv2.putText(copy_img,name,cordinates,font,font_size,font_color,font_thickness)
    return copy_img

def save_img(copy_img,name):
    path="cert-{}.jpg".format(name)
    cv2.imwrite(path,copy_img)

img=cv2.imread('CertificateTemplate.jpg')
name=input("enter the you want in that certificate: ")

new_img=generate_certificate(img,name)
save_img(new_img,name)

