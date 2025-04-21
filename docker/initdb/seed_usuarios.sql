-- docker/initdb/seed_usuarios.sql

-- Crear tabla si no existe (por si arrancas en limpio)
CREATE TABLE IF NOT EXISTS usuarios (
  id SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL
);

-- Insertar datos de semilla
INSERT INTO usuarios (nombre, email) VALUES
  ('Admin', 'admin@miapp.com'),
  ('Invitado', 'guest@miapp.com')
ON CONFLICT (email) DO NOTHING;  -- evita duplicados si vuelves a levantar