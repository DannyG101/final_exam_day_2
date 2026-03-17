from fastapi import FastAPI, Response
import uvicorn
from sql_connection import MySQLConnection

query_handler = MySQLConnection()


app = FastAPI()

@app.get("/get_all_high_priority")
def get_all_high_priority():
    return query_handler.get_all_high_priority()

@app.get("/signal_type_count")
def signal_type_count():
    return query_handler.signal_type_count()

@app.get("/top_3_unknown_targets")
def top_3_unknown_targets():
    return query_handler.top_3_unknown_targets()

@app.get("/awake_sleeping_cells")
def awake_sleeping_cells():
    return query_handler.awake_sleeping_cells()


@app.get("/route_visualization")
def route_visualization(entity_id):
    img_buf = query_handler.route_visualization(entity_id)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img_buf.getvalue(), headers=headers, media_type='image/png')
