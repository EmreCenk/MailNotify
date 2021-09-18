

import requests

def send_image(image_name = "test_image.png", serial_number = "12344567"):
    files = {"image": open(image_name, "rb"),
             # "serial": serial_number
             }
    url = "http://127.0.0.1:5000/"
    r = requests.post(url, files=files, data={"serial": serial_number})
    print(r.status_code)
    return r


if __name__ == '__main__':
    send_image()