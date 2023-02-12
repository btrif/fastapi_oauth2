#  Created by btrif Trif on 12-02-2023 , 4:36 PM.





if __name__ == "__main__":
    import uvicorn
    from routes import bogdan_app

    uvicorn.run("main:bogdan_app", log_level="info", reload=True, port=8002)

