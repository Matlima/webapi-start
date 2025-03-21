# app/core/token.py

from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError

# Configurações do JWT
SECRET_KEY = "ezyusvwqldsolrvldzpbuxyfxwjtswcrkawshpvgoevwdyttyqogipmknjamktkqvqpnchynohbssqromfvbyadevzrvhnlzafecsswdxtrrktnmafzvaepkyzxcdven"  # Utilize uma chave robusta e guarde em variável de ambiente
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise JWTError("Token inválido ou expirado")
