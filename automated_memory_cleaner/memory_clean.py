import time
import logging
import subprocess

# Set up logging
logging.basicConfig(filename='service_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# Main functionality or tasks that need to run persistently
def main():
    while True:
        try:
            # Replace this with your specific functionality or tasks
            # For instance, you could perform data processing, monitoring, etc.
            logging.info("Service is running...")  # Logging service activity

            # Add the steps for cleaning the system
            logging.info("Cleaning the system...")

            # Limpiar cachés de paquetes
            subprocess.run(['sudo', 'apt-get', 'clean'])
            subprocess.run(['sudo', 'apt-get', 'autoclean'])

            # Eliminar paquetes obsoletos
            subprocess.run(['sudo', 'apt-get', 'autoremove'])

            # Limpiar registros antiguos
            subprocess.run(['sudo', 'journalctl', '--vacuum-time=7d'])

            # Verificar y eliminar archivos temporales (cuidado al usar rm - ajusta según tus necesidades)
            subprocess.run(['sudo', 'du', '-h', '/var/log'])
            subprocess.run(['sudo', 'rm', '/var/log/*'])

            # Limpiar la caché de thumbnails (miniaturas)
            subprocess.run(['rm', '-rf', '~/.cache/thumbnails'])

            # Desactivar y reactivar la swap
            subprocess.run(['sudo', 'swapoff', '-a'])
            subprocess.run(['sudo', 'swapon', '-a'])

            # Simulating some task; replace this with your actual logic
            time.sleep(5)
        except Exception as e:
            logging.error(f"Error occurred: {str(e)}")
            # Implement proper error handling here

if __name__ == "__main__":
    main()
