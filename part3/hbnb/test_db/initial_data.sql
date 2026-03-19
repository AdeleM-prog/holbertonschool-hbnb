
INSERT INTO users (id, first_name, last_name, email, password, is_admin) VALUES
    ('36c9050e-ddd3-4c3b-9731-9f487208bbc1', 'Admin', 'HBnB', 'admin@hbnb.io', '$2b$12$A/.NcLp/4koq.tBy53OHdOfOtYr6RZibSMkladWruPLJq0E0vwU4K', TRUE),
    ('cf6ec6c2-44fb-4380-8d2c-a904a9b2ad91', 'Alice', 'Smith', 'alice@hbnb.io', '$2b$12$2UYYz33JHj/ryCEnAwnJoOu.VAWJ9/umIPGEnz4uJpobex2mYQZ0W', FALSE),
    ('c11bd7a3-5f31-414f-99a0-af65588bbd27',   'Bob',   'Jones', 'bob@hbnb.io',   '$2b$12$l1VT7IoE61m8mGfyPXb8VO.X3keMcxNq4mSIg0.sON/55Hrbtq8nS',   FALSE);

INSERT INTO amenities (id, name) VALUES
    ('dbf39fe4-19b6-4ed0-8ac1-03b2426add56', 'WiFi'),
    ('bc5c282f-70cd-4ffa-abf1-4af88b8d835e', 'Swimming Pool'),
    ('252f0970-af26-400a-a638-30ea4a1d8973',   'Air Conditioning');

INSERT INTO places (id, title, description, price, latitude, longitude, owner_id) VALUES
    ('654ed3e4-4e13-414c-9663-7ca36d286c36', 'Alice Cottage',  'A cozy cottage by the sea', 85.00,  48.8566,  2.3522, 'cf6ec6c2-44fb-4380-8d2c-a904a9b2ad91'),
    ('f3062c09-9319-421a-bc43-bef7fe334485', 'Bob Apartment',  'A modern flat downtown',    120.00, 51.5074, -0.1278, 'c11bd7a3-5f31-414f-99a0-af65588bbd27');

-- Alice's place has WiFi + Pool, Bob's place has WiFi + AC
INSERT INTO place_amenity (place_id, amenity_id) VALUES
    ('654ed3e4-4e13-414c-9663-7ca36d286c36', 'dbf39fe4-19b6-4ed0-8ac1-03b2426add56'),
    ('654ed3e4-4e13-414c-9663-7ca36d286c36', 'bc5c282f-70cd-4ffa-abf1-4af88b8d835e'),
    ('f3062c09-9319-421a-bc43-bef7fe334485', 'dbf39fe4-19b6-4ed0-8ac1-03b2426add56'),
    ('f3062c09-9319-421a-bc43-bef7fe334485', '252f0970-af26-400a-a638-30ea4a1d8973');

-- Bob reviews Alice's place
INSERT INTO reviews (id, text, rating, user_id, place_id) VALUES
    ('2b065c80-8aaf-4e4b-b161-a16e9c707f2b', 'Lovely place, very peaceful!', 5, 'c11bd7a3-5f31-414f-99a0-af65588bbd27', '654ed3e4-4e13-414c-9663-7ca36d286c36');
