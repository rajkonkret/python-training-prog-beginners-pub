# Wczytaj host, port i hasło z pliku properties.xml i wypisz je na standardowe wyjście w postaci: "host:port -p hasło"
# np. "127.0.0.1:5000 -p encrypted_password". Jeżeli jest ustwaiona któraś ze zmiennych środowiskowych APP_DATABASE_HOST,
# APP_DATABASE_PORT, APP_DATABASE_PASSWORD, to odpowiednio wartość odpowiednio hosta, portu czy hasła jest używana
# zamiast tej z pliku xml.
import os
import xml.etree.ElementTree as ET

document: ET = ET.parse("properties.xml")
databaseET: ET = document.find("database")

host: str = databaseET.find("host").text
port: str = databaseET.find("port").text
password: str = databaseET.find("password").text

host = os.environ.get("APP_DATABASE_HOST", host)
port = os.environ.get("APP_DATABASE_PORT", port)
password = os.environ.get("APP_DATABASE_PASSWORD", password)

print(f"{host}:{port} -p {password}")
