CREATE TABLE locations (
    location_id BIGINT PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100),
    country VARCHAR(100) DEFAULT 'India'
);

CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    full_name VARCHAR(150),
    email VARCHAR(200) UNIQUE,
    phone VARCHAR(30),
    signup_date DATE NOT NULL,
    location_id BIGINT REFERENCES locations(location_id)
);

CREATE TABLE marketing_campaigns (
    campaign_id BIGINT PRIMARY KEY,
    campaign_name VARCHAR(150) NOT NULL,
    channel VARCHAR(80),
    start_date DATE,
    end_date DATE,
    campaign_cost DECIMAL(12,2)
);

CREATE TABLE theatres (
    theatre_id BIGINT PRIMARY KEY,
    theatre_name VARCHAR(150) NOT NULL,
    location_id BIGINT NOT NULL REFERENCES locations(location_id)
);

CREATE TABLE screens (
    screen_id BIGINT PRIMARY KEY,
    theatre_id BIGINT NOT NULL REFERENCES theatres(theatre_id),
    screen_name VARCHAR(80),
    seating_capacity INT
);

CREATE TABLE genres (
    genre_id BIGINT PRIMARY KEY,
    genre_name VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE movies (
    movie_id BIGINT PRIMARY KEY,
    movie_title VARCHAR(200) NOT NULL,
    release_date DATE,
    language VARCHAR(60),
    duration_minutes INT
);

CREATE TABLE movie_genres (
    movie_id BIGINT REFERENCES movies(movie_id),
    genre_id BIGINT REFERENCES genres(genre_id),
    PRIMARY KEY(movie_id, genre_id)
);

CREATE TABLE cast_members (
    cast_id BIGINT PRIMARY KEY,
    cast_name VARCHAR(150) NOT NULL
);

CREATE TABLE movie_cast (
    movie_id BIGINT REFERENCES movies(movie_id),
    cast_id BIGINT REFERENCES cast_members(cast_id),
    role_type VARCHAR(50),
    PRIMARY KEY(movie_id, cast_id, role_type)
);

CREATE TABLE events (
    event_id BIGINT PRIMARY KEY,
    event_title VARCHAR(200) NOT NULL,
    event_type VARCHAR(50) NOT NULL, -- Movie, Play, Concert, Sport
    movie_id BIGINT NULL REFERENCES movies(movie_id)
);

CREATE TABLE shows (
    show_id BIGINT PRIMARY KEY,
    event_id BIGINT NOT NULL REFERENCES events(event_id),
    screen_id BIGINT NOT NULL REFERENCES screens(screen_id),
    show_start_ts TIMESTAMP NOT NULL,
    base_price DECIMAL(10,2) NOT NULL
);

CREATE TABLE bookings (
    booking_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(user_id),
    booking_ts TIMESTAMP NOT NULL,
    booking_status VARCHAR(30) NOT NULL, -- Confirmed, Cancelled, Failed
    campaign_id BIGINT NULL REFERENCES marketing_campaigns(campaign_id),
    total_amount DECIMAL(12,2) NOT NULL,
    discount_amount DECIMAL(12,2) DEFAULT 0
);

CREATE TABLE booking_items (
    booking_item_id BIGINT PRIMARY KEY,
    booking_id BIGINT NOT NULL REFERENCES bookings(booking_id),
    show_id BIGINT NOT NULL REFERENCES shows(show_id),
    seat_number VARCHAR(20),
    ticket_price DECIMAL(10,2) NOT NULL
);

CREATE TABLE payments (
    payment_id BIGINT PRIMARY KEY,
    booking_id BIGINT NOT NULL REFERENCES bookings(booking_id),
    payment_ts TIMESTAMP NOT NULL,
    payment_method VARCHAR(50),
    payment_status VARCHAR(30),
    paid_amount DECIMAL(12,2)
);

CREATE TABLE cancellations (
    cancellation_id BIGINT PRIMARY KEY,
    booking_id BIGINT NOT NULL REFERENCES bookings(booking_id),
    cancellation_ts TIMESTAMP NOT NULL,
    cancellation_reason VARCHAR(200),
    refund_amount DECIMAL(12,2)
);
