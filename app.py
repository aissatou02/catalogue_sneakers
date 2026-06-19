from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sneakers_db"
)

@app.route('/')
def index():

    search = request.args.get('search', '')

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT s.id,s.nom,s.prix,s.image,
           m.nom AS marque,
           c.nom AS categorie,
           co.nom AS couleur,
           t.pointure
    FROM sneakers s
    JOIN marques m ON s.marque_id = m.id
    JOIN categories c ON s.categorie_id = c.id
    JOIN couleurs co ON s.couleur_id = co.id
    JOIN tailles t ON s.taille_id = t.id
    """

    if search:
        query += " WHERE s.nom LIKE %s"
        cursor.execute(query, ('%' + search + '%',))
    else:
        cursor.execute(query)

    sneakers = cursor.fetchall()

    return render_template(
        'index.html',
        sneakers=sneakers
    )

@app.route('/add')
def add_page():

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM marques")
    marques = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM couleurs")
    couleurs = cursor.fetchall()

    cursor.execute("SELECT * FROM tailles")
    tailles = cursor.fetchall()

    return render_template(
        'add.html',
        marques=marques,
        categories=categories,
        couleurs=couleurs,
        tailles=tailles
    )

@app.route('/insert', methods=['POST'])
def insert():

    cursor = db.cursor()

    cursor.execute("""
    INSERT INTO sneakers
    (nom,prix,image,marque_id,categorie_id,couleur_id,taille_id)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """,(
        request.form['nom'],
        request.form['prix'],
        request.form['image'],
        request.form['marque'],
        request.form['categorie'],
        request.form['couleur'],
        request.form['taille']
    ))

    db.commit()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM sneakers WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/edit/<int:id>')
def edit(id):

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM sneakers WHERE id=%s",
        (id,)
    )

    sneaker = cursor.fetchone()

    cursor.execute("SELECT * FROM marques")
    marques = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM couleurs")
    couleurs = cursor.fetchall()

    cursor.execute("SELECT * FROM tailles")
    tailles = cursor.fetchall()

    return render_template(
        'edit.html',
        sneaker=sneaker,
        marques=marques,
        categories=categories,
        couleurs=couleurs,
        tailles=tailles
    )
@app.route('/update/<int:id>', methods=['POST'])
def update(id):

    cursor = db.cursor()

    cursor.execute("""
    UPDATE sneakers
    SET nom=%s,
        prix=%s,
        image=%s,
        marque_id=%s,
        categorie_id=%s,
        couleur_id=%s,
        taille_id=%s
    WHERE id=%s
    """,(
        request.form['nom'],
        request.form['prix'],
        request.form['image'],
        request.form['marque'],
        request.form['categorie'],
        request.form['couleur'],
        request.form['taille'],
        id
    ))

    db.commit()

    return redirect('/')