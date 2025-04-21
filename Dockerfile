# 1. Imagen base con Python
FROM python:3.11-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar sólo los archivos de dependencias primero
#    Esto ayuda a aprovechar la caché de Docker si no cambian tus requirements
COPY requirements.txt .

# 4. Instalar las dependencias en el entorno del contenedor
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto de tu código al contenedor
COPY . .

# 6. Exponer el puerto en el que tu aplicación escucha
EXPOSE 8000

# 7. Comando por defecto al iniciar el contenedor:
#    Primero podrías aplicar migraciones o cualquier script, 
#    pero si sólo quieres arrancar tu API:
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
