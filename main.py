from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Tell FastAPI where to find the templates
templates = Jinja2Templates(directory="templates")

# Mount the static directory
app.mount("/static", StaticFiles(directory="templates/assets"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/portfolio/{page_name}", response_class=HTMLResponse)
async def read_portfolio(request: Request, page_name: str):
    return templates.TemplateResponse(f"portfolio/{page_name}.html", {"request": request})

@app.get("/sonar.html", response_class=HTMLResponse)
async def read_sonar(request: Request):
    return templates.TemplateResponse("sonar.html", {"request": request})

@app.get("/contact.html", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})