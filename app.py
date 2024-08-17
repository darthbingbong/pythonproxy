from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from conva_ai import AsyncConvaAI
import asyncio

# Initialize FastAPI app
app = FastAPI()

# Allow CORS (Cross-Origin Resource Sharing) from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (adjust if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize Conva AI client
client = AsyncConvaAI(
    assistant_id="9de9101449314e1e9e3b18c73a9951c5",
    assistant_version="9.0.1",
    api_key="50e557e85d6a46548ebc82d0b1f293b7"
)

# Asynchronous function to get response from Conva AI
async def get_conva_response(query: str):
    response = await client.invoke(query=query)
    return response['output']

# Route to handle POST requests from the frontend
@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query")
    
    # Get response from Conva AI
    response = await get_conva_response(query)
    
    return {"response": response}

# Entry point to run FastAPI with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080)
