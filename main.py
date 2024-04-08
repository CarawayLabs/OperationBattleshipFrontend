from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Tell FastAPI where to find the templates
templates = Jinja2Templates(directory="templates")

# If you have static files (CSS, JS, etc.), serve them from a static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/upload", response_class=HTMLResponse)
async def upload_resume_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.get("/serve_recommendations", response_class=HTMLResponse)
async def view_recommendations(request: Request):
    # You would typically fetch recommendations from the database here
    return templates.TemplateResponse("serve_recommendations.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact_us(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
