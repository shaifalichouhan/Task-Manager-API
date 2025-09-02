from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.auth.jwt_handler import decode_access_token
from app.models.user import User

# tokenUrl points to the OAuth2 token route (we create it in routers/users.py)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/token")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    creds_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    if payload is None:
        raise creds_exc

    user_id = payload.get("sub")
    if user_id is None:
        raise creds_exc

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise creds_exc

    return user
