from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename
from google.cloud import storage
#from config import bucketName, localFolder, bucketFolder

app = Flask(__name__)

app.config['bucketName']='email_bucket'
#set path as app.config['bucketFolder']='[user-X]/[EmailNumber-Y]/'
app.config['localFolder']='D:\\Python\\'
app.config['UPLOAD_FOLDER'] = 'D:/Python'
app.config["ALLOWED_FILE_EXTENSIONS"] = ["HTML"]

storage_client = storage.Client()# Instantiates a client

bucket = storage_client.get_bucket(app.config['bucketName'])# get the bucket

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
            user_name=request.files["user_name"]
            mailNumber=request.files["mailNumber"]
            app.config['bucketFolder']=user_name/mailNumber/

            if 'file' not in request.files:
                print("No file")
                return redirect(request.url)
            file = request.files["file"]

            if file.filename == "":
                print("No file selected")
                return redirect(request.url)
                #file.filename=xyzFile.extension
            if allowed_file(file.filename):
                localFile = app.config['localFolder'] + file.filename
                blob = bucket.blob(app.config['bucketFolder'] + 'content.html')#content.html is the renamed filename for the original file
                blob.upload_from_filename(localFile)
                print('Uploaded {file.filename} ')
                return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return "<h1>Wrong extension</h1>"

    return '<form action = "http://localhost:5000/" method = "POST" enctype = "multipart/form-data"><input type = "file" name = "file" /><input type = "text" name = "user_name" /><input type = "text" name = "mailNumber" /><input type = "submit"/></form> '
if __name__ == '__main__':
   app.run(debug = True)