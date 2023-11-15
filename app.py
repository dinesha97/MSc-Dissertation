from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from main import getPredictions
import os

UPLOAD_FOLDER = 'static/images/'
 
app = Flask(__name__, static_folder="static")
app.secret_key = "newsec"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def imagesubmission():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)  
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            label = getPredictions(filename)
            flash(label)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash(full_filename)
            return redirect('/')


if __name__ == "__main__":
    app.run()