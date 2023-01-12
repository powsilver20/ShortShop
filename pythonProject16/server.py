from flask import Flask, request, render_template , redirect , url_for
import sqlite3
import uuid
app = Flask(__name__)
import base64

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return "No selected file"
        if file:
            # save the file to a database

            conn = sqlite3.connect("database/product.db")
            cursor = conn.cursor()
            id = str(uuid.uuid4())
            data = file.read()
            data = base64.b64encode(data).decode()

            cursor.execute(f"INSERT INTO Products (id, image) VALUES (?, ?)",(id , data))
            conn.commit()
            # get the id of the inserted image

            conn.close()
            # redirect to the display page
            return render_template('upload.html')
    return render_template('upload.html')


@app.route('/')
def display_data():
    # Connect to the database
    conn = sqlite3.connect('database/product.db')
    c = conn.cursor()

    # Retrieve the data from the 'example' table
    c.execute('SELECT id, image FROM Products')
    data = c.fetchall()

    # Close the connection
    conn.close()

    # Render the data in a table on an HTML page
    return render_template('display.html', data=data)
if __name__ == "__main__":
    app.run(debug=True)
