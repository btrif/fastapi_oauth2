#  Created by btrif Trif on 12-02-2023 , 4:20 PM.
from typing import Union
from pydantic import BaseModel

### MODELS
# Model for User
class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str
