from flask import request, jsonify
from models import SessionLocal, Product

def register_routes(app):

    @app.route("/products", methods=["GET"])
    def get_products():
        session = SessionLocal()
        products = session.query(Product).all()
        result = []

        for p in products:
            result.append({
                "id": p.id,
                "name": p.name,
                "brand": p.brand,
                "price": p.price,
                "image": p.image,
                "description": p.description
            })

        session.close()
        return jsonify(result)

    @app.route("/products", methods=["POST"])
    def add_product():
        data = request.json
        session = SessionLocal()

        new_product = Product(
            name=data["name"],
            brand=data["brand"],
            price=data["price"],
            image=data["image"],
            description=data["description"]
        )

        session.add(new_product)
        session.commit()
        session.close()

        return jsonify({"message": "Produit ajouté"})


    @app.route("/products/<int:id>", methods=["DELETE"])
    def delete_product(id):
        session = SessionLocal()
        product = session.query(Product).get(id)

        if not product:
            return jsonify({"error": "Produit introuvable"}), 404

        session.delete(product)
        session.commit()
        session.close()

        return jsonify({"message": "Produit supprimé"})