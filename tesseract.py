import pytesseract
import cv2
#import pspTrans as pT

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract64\tesseract'

img_cv = cv2.imread('./result_subway/wordA.png')
reversalOut = 255-img_cv

#img_cv = pT.Result
cv2.imshow('pTimage', reversalOut)
# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
img_rgb = cv2.cvtColor(reversalOut, cv2.COLOR_BGR2RGB)

#print(pytesseract.image_to_string(img_rgb, lang='kor+eng'))

print('psm-1')
custom_oem_psm_config = r'--oem 3 --psm 1' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-3(default)')
custom_oem_psm_config = r'--oem 3 --psm 3' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-4')
custom_oem_psm_config = r'--oem 3 --psm 4' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-5 (vertical)')
custom_oem_psm_config = r'--oem 3 --psm 5' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-6')
custom_oem_psm_config = r'--oem 3 --psm 6' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-7')
custom_oem_psm_config = r'--oem 3 --psm 7' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-8')
custom_oem_psm_config = r'--oem 3 --psm 8' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-9')
custom_oem_psm_config = r'--oem 3 --psm 9' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-10(single character)')
custom_oem_psm_config = r'--oem 3 --psm 10' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-11')
custom_oem_psm_config = r'--oem 3 --psm 11' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-12')
custom_oem_psm_config = r'--oem 3 --psm 12' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

print('psm-13')
custom_oem_psm_config = r'--oem 3 --psm 13' #3(default), 7(single line), 8(signle word)
print(pytesseract.image_to_string(
     img_rgb, lang='kor', config=custom_oem_psm_config))

cv2.waitKey()
cv2.destroyAllWindows()
