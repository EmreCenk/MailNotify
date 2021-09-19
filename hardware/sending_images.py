

import requests

url = "http://127.0.0.1:5000/"


def send_image(image_name = "test_image.png",
               email ="emrecenk9@gmail.com",
               weight = "12 kg"):
    files = {"image": open(image_name, "rb"),
             # "serial": serial_number
             }
    r = requests.post(url, files=files, data={"email": email,
                                              "weight": weight})
    print(r.status_code)
    return r

def userinfofromapi(email):
    parameters = {"email": email}
    response = requests.get(url + "/userInfo", params = parameters)
    return response.json()


if __name__ == '__main__':
    # send_image()
    # userinfofromapi("emrecenk9@gmail.com")
    pass
