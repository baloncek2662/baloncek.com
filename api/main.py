from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {
        'app': 'baloncek.com',
        'author' : 'baloncek',
    }


# example call: http://127.0.0.1:8000/users/?user_id=12
@app.get('/users/')
def read_item(user_id: Optional[int] = 0, password:  Optional[str] = None):
    return {
        'user_id': user_id, 
        'password': password,
    }