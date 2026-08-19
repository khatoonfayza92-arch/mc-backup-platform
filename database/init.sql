CREATE TABLE IF NOT EXISTS backups (
    id SERIAL PRIMARY KEY,
    cloud_name VARCHAR(50) NOT NULL,
    backup_status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO backups (cloud_name, backup_status)
VALUES
('AWS', 'Completed'),
('Azure', 'Completed'),
('Google Cloud', 'Completed');