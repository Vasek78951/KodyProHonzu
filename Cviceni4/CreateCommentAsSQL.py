import re
def username_check(username):
    if not re.match(r"^[a-zA-Z0-9\s.,?!_-]{1,100}", username):
        raise ValueError ("Nickname obsahuje nepovolené znaky.")

def create_command(username, text):
    username_check(username)
    if not re.match(r"^[a-zA-Z0-9\s.,?!_-]+$", text):
        return "Text obsahuje nepovolené znaky."
    sql_command = f"INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES ('{username}', '{text}');"
    return sql_command

def password_policy_check(username, password):
    if len(password) < 10:
        return "Heslo musi byt minimalne 10 znaku dlouhe"
    if not re.search(r'\d', password):
        return "Heslo musi obsahovat alespon jednu cislici"
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return "Heslo musi obsahovat alespon jedno velke a male pismeno"
    if not re.search(r"[^\w\s]", password):
        return "Heslo musi obsahovat alespon jeden specialni znak"
    if username in password:
        return "heslo nesmi obsahovat username"
    for i in range(len(username) - 3):
        sub_str = username[i:i + 4]
        if sub_str.lower() in password.lower():
            return f"Heslo nesmi obsahovat podretezec uzivatelskeho jmena: {sub_str}"
    return "Heslo odpodivda pozadavkum"

def mobie_phone_number_create_command(username, mobie_phone_number):
    username_check(username)
    no_space_number = mobie_phone_number.replace(" ", "")
    if not re.match(r"^[0-9]{9}", no_space_number):
        raise ValueError ("Spatny tvar cisla")
    sql_command = f"UPDATE USERS SET PHONE_NUMBER = '{no_space_number}' WHERE USERNAME = '{username}';"
    return sql_command
def email_edit_command(username, email):
    username_check(username)
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        raise ValueError("spatny tvar emailu")
    sql_command = f"UPDATE ACCOUNT SET EMAIL = '{email}' WHERE USERNAME = '{username}';"
    return sql_command
username = "Uzivatel"
text = "novu prispevek"
password = "Heslo12345-"
number = "486 532 754"
email = "muj.email98@gmail.com"

print(create_command(username, text))
print(password_policy_check(username, password))
print(mobie_phone_number_create_command(username, number))
print(email_edit_command(username, email))


