import os
from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'D:/Python'
app.config["ALLOWED_FILE_EXTENSIONS"] = ["HTML"]

def allowed_file(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":

            if 'file' not in request.files:
                print("No file")
                return redirect(request.url)
            file = request.files["file"]

            if file.filename == "":
                print("No file selected")
                return redirect(request.url)

            if allowed_file(file.filename):
                filename = secure_filename(file.filename)

                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                print("file saved")

                return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return "<h1>Wrong extension</h1>"

    return '<form action = "http://localhost:5000/" method = "POST" enctype = "multipart/form-data"><input type = "file" name = "file" /><input type = "submit"/></form> '
if __name__ == '__main__':
   app.run(debug = True)