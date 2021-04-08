# from typing import Optional
# from datetime import datetime, timedelta

# from .mongodb import AsyncIOMotorClient, get_database
# from .config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM
# from ..services.users import get_user
# from ..models.schemas.auth import TokenData
# from ..models.schemas.users import User

# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt



# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth")


# def create_access_token(
#     data: dict,
#     expires_delta: Optional[timedelta] = None
# ):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# async def get_current_user(
#     db: AsyncIOMotorClient = Depends(get_database),
#     token: str = Depends(oauth2_scheme)
# ):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"}
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#         token_data = TokenData(email=email)
#     except JWTError:
#         raise credentials_exception
#     dbuser = await get_user(db, token_data.email)
#     if dbuser is None:
#         raise credentials_exception
#     return User(**dbuser.dict(), token=token)