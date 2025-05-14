import urllib.parse

username = "itskashyap26"
password = "@gitartham1"
encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)
mdb_connection_string = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.swuj2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
