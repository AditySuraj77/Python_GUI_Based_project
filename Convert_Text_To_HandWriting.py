
import pywhatkit as pw

user = input('Write here to Convert your Docs into HandWriting : ')

pw.text_to_handwriting(user,'hand_write.jpg')
print('Finished')