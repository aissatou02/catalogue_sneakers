CREATE DATABASE IF NOT EXISTS catalogue_sneakers;
USE catalogue_sneakers;

-- MARQUES

CREATE TABLE marques (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

-- CATEGORIES

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

-- COULEURS

CREATE TABLE couleurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

-- TAILLES

CREATE TABLE tailles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pointure INT NOT NULL
);

-- SNEAKERS

CREATE TABLE sneakers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(150) NOT NULL,
    prix DECIMAL(10,2) NOT NULL,
    image TEXT NOT NULL,

    marque_id INT NOT NULL,
    categorie_id INT NOT NULL,
    couleur_id INT NOT NULL,
    taille_id INT NOT NULL,

    FOREIGN KEY (marque_id) REFERENCES marques(id),
    FOREIGN KEY (categorie_id) REFERENCES categories(id),
    FOREIGN KEY (couleur_id) REFERENCES couleurs(id),
    FOREIGN KEY (taille_id) REFERENCES tailles(id)
);

-- DONNEES

INSERT INTO marques(nom) VALUES
('Nike'),
('Adidas'),
('New Balance'),
('Jordan');

INSERT INTO categories(nom) VALUES
('Running'),
('Lifestyle'),
('Basketball');

INSERT INTO couleurs(nom) VALUES
('Blanc'),
('Noir'),
('Gris');

INSERT INTO tailles(pointure) VALUES
(40),(41),(42),(43),(44);

INSERT INTO sneakers
(nom,prix,image,marque_id,categorie_id,couleur_id,taille_id)
VALUES

('530',129.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dw30a0b6b2/images/hi-res/001600919_102.jpg?sw=400&sh=400&sm=fit',
3,1,3,2),

('Air Max 90',149.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dw86d895a8/images/hi-res/001606079_102.jpg?sw=400&sh=400&sm=fit',
1,1,2,3),

('Air Max Plus',189.99,
'https://images.asos-media.com/products/asics-gel-quantum-360-viii-trainers-in-animal-print/206579531-1-animalprint?$n_640w$&wid=513&fit=constrain',
1,2,1,3),

('Campus 00s',119.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dwaa91cc76/images/hi-res/001517509_102.jpg?sw=400&sh=400&sm=fit',
2,2,2,2),

('9060',189.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dwe7bd8ee3/images/hi-res/001609267_102.jpg?sw=400&sh=400&sm=fit',
3,2,3,3),

('Air Force 1',129.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dwae8460a8/images/hi-res/001602232_102.jpg?sw=400&sh=400&sm=fit',
1,2,1,3),

('Dunk Low',119.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dwa7c27df5/images/hi-res/001605410_102.jpg?sw=400&sh=400&sm=fit',
1,2,2,2),

('Gazelle',109.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dw10217a1a/images/hi-res/001601271_102.jpg?sw=400&sh=400&sm=fit',
2,2,1,3),

('Forum Low',119.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dw8983ddf4/images/hi-res/001608033_102.jpg?sw=400&sh=400&sm=fit',
2,2,1,2),

('550',139.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dw8ac355ac/images/hi-res/001600060_102.jpg?sw=400&sh=400&sm=fit',
3,2,1,3),

('Jordan 1 Low',139.99,
'https://www.courir.com/on/demandware.static/-/Sites-master-catalog-courir/default/dw018da24c/images/hi-res/001601975_102.jpg?sw=400&sh=400&sm=fit',
4,3,1,3);