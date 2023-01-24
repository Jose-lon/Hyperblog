import pand
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,4]

@app.get("/content", response_class=HTMLResponse)
def get_list():
    return """
        <h1>Holi soy una pagina</h1>
    """