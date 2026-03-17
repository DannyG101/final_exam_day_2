from fastapi import FastAPI, Response
import uvicorn
from sql_connection import MySQLConnection

query_handler = MySQLConnection()


app = FastAPI()



@app.get("/route_visualization")
def get_img(entity_id):
    img_buf = query_handler.q5(entity_id)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img_buf.getvalue(), headers=headers, media_type='image/png')



uvicorn.run(app)