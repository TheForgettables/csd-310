import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="whatbook_user",
  password="MySQL8IsGreat!"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE whatabook")

DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost'; IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!'
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';
create database whatabook;

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);


CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
     REFERENCES user(user_Id)
);



INSERT INTO store(locale)
    VALUES ('130-1/2 Wickham Ave, Middletown, NY 10940');


INSERT INTO whatabook (book_name, author)
    VALUES ('Finn', 'Mike Geraghty');
INSERT INTO whatabook (book_name, author)
    VALUES ('Preacher', 'Mike Geraghty');
INSERT INTO whatabook (book_name, author) 
    VALUEs ('Liam', 'Mike Geraghty');
INSERT INTO whatabook (book_name, author) 
    VALUES ('Demon', 'Mike Geraghty');
INSERT INTO whatabook (book_name, author) 
    VALUES ('After Midnight', 'Lacy Hart');
INSERT INTO whatabook (book_name, author)
    VALUES ('For What Its Worth', 'Mike Geraghty');
INSERT INTO whatabook (book_name, author)
    VALUES ('Change Up', 'Mike Geraghty')
INSERT INTO whatabook (book_name, author)
    VALUES ('Spring Fever', 'Mike Geraghty');
INSERT INTO whatabook (book_name, author)
    VALUES ('The Sweet SPot', 'Mike Geraghty');

INSERT INTO user(first_name, last_name)
    VALUES ('Finn','OFarrell');
INSERT INTO user(first_name, last_name)
    VALUES ('Cillian', 'Meehan');
INSERT INTO user(first_name, last_name)
    VALUES ('Darryl', 'Garvey');

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE last_name = 'Meehan');
        (SELECT book_id FROM WHERE book_name = 'Finn');
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE last_name = 'OFarrell');
        (SELECT book_id FROM WHERE book_name = 'Preacher');
    );
INSERT INTO wishlist(User_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE last_name = 'Garvey');
        (SELECT book_id FROM user WHERE book_name = 'Demon');
    );
