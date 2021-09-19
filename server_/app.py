
from flask import Flask, request, redirect, Response, send_file
import os
from datetime import datetime
from cockroach_db.cockroach_db import db
import psycopg2
from flask_cors import CORS
from handling_emails.emailhandler import email as email_sender
from sms.twilosms import sms as twilio_sms_sender
def valid_serial(serial_number):
    #TODO: Check if the serial number is registered in the serial number database
    return True

def save_image():

    email = request.values["email"]
    email = email.replace("@gmail.com", "")

    if not valid_serial(email):
        return ""

    image = request.files["image"]
    print("image name:", image)

    proper_date = str(datetime.now()).replace(".", "-").replace(":", "-")

    path_to_save = os.path.join(app.config["IMAGE_UPLOADS"],
                                str(email),
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
    return path_to_save, proper_date

def save_to_cockroach(date_string):
    email = request.values["email"]
    weight = request.values["weight"]
    email = email.replace("@gmail.com", "")
    print("email:", email, "weight:", weight)

    connection_string = os.environ["CONNECTION_STRING_TO_COCKROACHDB"]
    conn = psycopg2.connect(connection_string)

    if not db.check_if_table_exists(conn, email):
        db.create_client_table(conn, email)
        print('created new')

    print("inserting")
    db.insert_to_table(conn, email, date_string, weight)
    print("inserted to table")
    conn.commit()
    conn.close()

def get_user_info(email):
    email = email.replace("@gmail.com", "")
    connection_string = os.environ["CONNECTION_STRING_TO_COCKROACHDB"]
    conn = psycopg2.connect(connection_string)
    result = db.get_table(conn, email)
    conn.close()
    return result


app = Flask(__name__, template_folder="", static_folder="")
CORS(app, resources=r'/*', supports_credentials=True)
app.config["IMAGE_UPLOADS"] = "uploads"


@app.route('/', methods=["GET", "POST"])
def upload():

    if request.method == "POST":
        #NEW ENTRY 
        path_to_save, proper_date = save_image() # saves image
        save_to_cockroach(proper_date) # saves info to cockroach db

        email_sender.send(request.values["email"], os.path.join(path_to_save, proper_date + ".png"))


        current_image_url = request.url_root + "/" + "uploads" + "/" + request.values["email"].replace("@gmail.com", "") + "/" + proper_date + ".png"
        current_image_url = current_image_url.replace(" ", "%20")
        phone_number = db.get_phone_number(request.values["email"])
        print("sms image url:", current_image_url)
        print("sms sending phone:", phone_number)
        twilio_sms_sender.send(phone_number, current_image_url)
        return ""
    else:
        xml = request.url

        return send_file(xml, as_attachment=True, attachment_filename=xml, mimetype="image/png")

@app.route("/userInfo", methods = ["GET"])
def get_images():
    email = request.args["email"].replace("@gmail.com", "")
    print("email received:",email)
    path_to_save = os.path.join(app.config["IMAGE_UPLOADS"],
                                str(email),

                                )
    image_list = os.listdir(os.path.join(os.getcwd(), path_to_save))

    userInfo = {}
    table = get_user_info(email)
    for i in range(len(table)):
        image_url = os.path.join(path_to_save, image_list[i]).replace(r"\ "[:-1], "/")
        id_, date_string, weight_string = table[i]
        userInfo[id_] = {"date_string": date_string,
                         "weight_string": weight_string,
                         "image_url": image_url}

    return userInfo


if __name__ == '__main__':
    #for testing
    app.run(debug=True)
    # print(get_user_info("emrecenk9@gmail.com"))