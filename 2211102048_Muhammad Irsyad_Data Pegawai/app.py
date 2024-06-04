from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_pegawai'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pegawai")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', pegawai=data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        nama = request.form['nama']
        nip = request.form['nip']
        tgl_lahir = request.form['tgl_lahir']
        pangkat = request.form['pangkat']
        golongan = request.form['golongan']
        jabatan = request.form['jabatan']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pegawai (nama, nip, tgl_lahir, pangkat, golongan, jabatan) VALUES (%s, %s, %s, %s, %s, %s)",
                    (nama, nip, tgl_lahir, pangkat, golongan, jabatan))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['DELETE'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM pegawai WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/update', methods= ['PUT', 'GET'])
def update():
    if request.method == 'PUT':
        id_data = request.form['id']
        nama = request.form['nama']
        nip = request.form['nip']
        tgl_lahir = request.form['tgl_lahir']
        pangkat = request.form['pangkat']
        golongan = request.form['golongan']
        jabatan = request.form['jabatan']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE pegawai SET nama=%s, nip=%s, tgl_lahir=%s, pangkat=%s, golongan=%s, jabatan=%s
        WHERE id=%s
        """, (nama, nip, tgl_lahir, pangkat, golongan, jabatan, id_data))
        mysql.connection.commit()
        flash("Data Updated Successfully")
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)