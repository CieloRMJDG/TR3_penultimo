# Aplicar migraciones antes de iniciar el servidor
echo "Aplicando migraciones a MongoDB..."
python manage.py migrate --no-input

# Recolectar archivos estáticos para Whitenoise (CSS, JS, etc.)
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --no-input

# Iniciar el servidor Gunicorn
echo "Iniciando Gunicorn..."
# La sintaxis de Gunicorn debe apuntar a tu proyecto: [nombre_del_proyecto].wsgi:application
gunicorn TR3_penultimo.wsgi:application