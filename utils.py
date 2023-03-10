#  Created by btrif Trif on 12-02-2023 , 4:24 PM.
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from database import fake_users_db
from models import UserInDB, User

### METHODS

# Method for has password
def fake_hash_password(password: str):
    return password # + "_fakehashed"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


## Check if user in database
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

### END METHODS
