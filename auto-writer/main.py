from fastapi import FastAPI,WebSocket,WebSocketDisconnect,BackgroundTasks
from langchain_openai import ChatOpenAI

app = FastAPI()

class Author:
    def __init__(self, name: str) -> None:
        pass
        
    def run(self, query: str) -> str:
        pass
    
        
@app.post("/chat")
def chat(query: str, background_tasks: BackgroundTasks):
    pass
        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)