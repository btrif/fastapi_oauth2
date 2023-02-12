

You need to create a Virtual Env and install requirements.txt as follows

```
fastapi_oauth2> pip install -r requirements.txt
```


You should have the following packages :

```
(fastapi_oauth2_venv) fastapi_oauth2> pip freeze
```

```
anyio==3.6.2
click==8.1.3
colorama==0.4.6
fastapi==0.90.0
h11==0.14.0
idna==3.4
pydantic==1.10.4
python-multipart==0.0.5
six==1.16.0
sniffio==1.3.0
starlette==0.23.0
style==1.1.0
typing_extensions==4.4.0
update==0.0.1
uvicorn==0.20.0
```


There are 2 applications within this project. They are the same
but the structure differs.
- one_file_app_oauth.py runs on port :8001 and is a standalone app with no dependencies
- the other *.py files are part of the second same app running on port :8002
