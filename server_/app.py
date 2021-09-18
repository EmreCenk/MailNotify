
from flask import Flask, request, redirect
import os
from datetime import datetime
def valid_serial(serial_number):
    #TODO: Check if the serial number is registered in the serial number database
    return True

def save_image():
    serial_num = request.values["serial"]

    if not valid_serial(serial_num):
        return ""

    image = request.files["image"]
    print("image name:", image)

    proper_date = str(datetime.now()).replace(".", "-").replace(":", "-")

    path_to_save = os.path.join(app.config["IMAGE_UPLOADS"],
                                str(serial_num),
                                )

    if not os.path.exists(path_to_save):
        print("creating:", path_to_save)
        os.mkdir(path_to_save)
        print("yuh")

    original = os.getcwd()
    os.chdir(path_to_save)
    # path_to_save = os.path.join(path_to_save, str(datetime.now())+".png")
    image.save(proper_date + ".png")
    os.chdir(original)

app = Flask(__name__, template_folder="", static_folder="")
app.config["IMAGE_UPLOADS"] = "uploads"


@app.route('/', methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        save_image()
        return ""
    else:
        return redirect(request.url)

@app.route("/retreive_images", methods = ["GET"])
def get_images():
    pass


if __name__ == '__main__':
    #for testing
    app.run(debug=True)
