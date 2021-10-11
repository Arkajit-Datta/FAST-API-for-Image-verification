from fastapi import FastAPI, File, UploadFile
from pydantic.fields import T
import uvicorn
import shutil
from main import main

app = FastAPI()


@app.post("/post_image/")
async def root(file: UploadFile = File(...)):
    with open('files_upload\check.jpg',"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    path = 'files_upload\check.jpg'
    ret = main(path)

    if ret==True:
        return {"result": "Matched"}
    else:
        return {"result": "Not Matched"}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')