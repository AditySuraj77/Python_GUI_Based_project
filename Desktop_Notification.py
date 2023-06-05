from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
                         title='SMILE',
                         message='इसलिए मत रो की सब ख़त्म हो गया, मुस्कुराओ कि ऐसा हुआ।',
                         #app_icon='smile_smile.jfif',
                         timeout=2)
        time.sleep(10)