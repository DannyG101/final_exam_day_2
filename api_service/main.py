from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()



@app.get('/')
def get_img():
    img_buf = q5()
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img_buf.getvalue(), headers=headers, media_type='image/png')



uvicorn.run(app)