#  Created by btrif Trif on 12-02-2023 , 4:23 PM.
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from fastapi import Depends, HTTPException

from database import fake_users_db
from models import UserInDB, User
from utils import fake_hash_password, get_current_active_user



### Initiate FastApi App
bogdan_app = FastAPI()


### ROUTES


@bogdan_app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {"access_token": user.username, "token_type": "bearer"}


@bogdan_app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@bogdan_app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')


### END ROUTES