from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def hash_password(password):
    return str(pwd_context.hash(password))


def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

# parol="salom12"
# print(verify_password(parol,"$2b$12$BVr3FQdo0vfWSgrwVgec1Oc8T3XUOc5AAjA0cjJO6D6HH/0JPHYc2"))
