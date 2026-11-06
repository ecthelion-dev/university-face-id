from fastapi import FastAPI

app = FastAPI(
    title="University Face ID AI",
    version="0.1.0",
    description="Face recognition and attendance processing service",
)


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "face-id-ai",
        "device": "cpu",
    }
