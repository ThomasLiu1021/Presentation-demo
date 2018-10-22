import time
import requests
import os

counter = 1
while True:
   # URL = 'http://192.168.1.1:5000/image.jpg'
    URL = 'http://google.com/favicon.ico'
    CWD_PATH = os.getcwd()
    current_image_name = 'image_' + str(counter) + '.jpg'
    INPUT_FOLDER = "input_images"
    input_path = os.path.join(CWD_PATH,INPUT_FOLDER,current_image_name)
    # download the image from url
    # rename
    # write the content
    r = requests.get(URL)
    open(input_path, 'wb').write(r.content)
    command = 'python Object_detection_image.py ' + current_image_name
    print(command)
    os.system(command)

    counter = counter + 1
    
    print('running again')
    time.sleep(10)
