from fastapi import FastAPI

app = FastAPI(title="Havenstone Inquiry System")

@app.get("/health")
def health():
    return {"status": "ok"}