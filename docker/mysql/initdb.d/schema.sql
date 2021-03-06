CREATE TABLE user (
    id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    sex VARCHAR(10) NOT NULL,
    email VARCHAR(256) NOT NULL,
    prefecture VARCHAR(10) NOT NULL,
    birthday DATE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)
);


CREATE TABLE points (
    id INT NOT NULL,
    user_id INT  NOT NULL,
    total_point INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id),
    FOREIGN KEY fk_id(user_id) REFERENCES user(id)
);
