CREATE TABLE ac_device (
    ac_id INT AUTO_INCREMENT PRIMARY KEY,
    ac_name VARCHAR(50),
    location VARCHAR(100),
    rated_power INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sensor_readings (
    reading_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    ac_id INT,
    voltage FLOAT,
    current FLOAT,
    power FLOAT,
    energy FLOAT,
    frequency FLOAT,
    power_factor FLOAT,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ac_id) REFERENCES ac_device(ac_id)
);

CREATE TABLE processed_readings (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    ac_id INT,
    avg_power FLOAT,
    energy_kwh FLOAT,
    efficiency FLOAT,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ac_id) REFERENCES ac_device(ac_id)
);

CREATE TABLE ml_predictions (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    ac_id INT,
    predicted_energy FLOAT,
    prediction_time DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ac_id) REFERENCES ac_device(ac_id)
);

CREATE TABLE optimization_results (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    ac_id INT,
    recommended_temp FLOAT,
    expected_savings FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ac_id) REFERENCES ac_device(ac_id)
);
