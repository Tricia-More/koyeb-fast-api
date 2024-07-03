from fastapi import FastAPI, Request

import logging




app = FastAPI()



@app.get("/api/hello")
async def hello(visitor_name: str, request: Request):
    
        client_ip = request.client.host
        

        

        city = ("New York")  # Fallback to New York if city not found
        

        

        greeting = f"Hello, {visitor_name}!, the temperature is 11 degrees Celsius in {city}"

        return {
            "client_ip": client_ip,
            "location": city,
            "greeting": greeting
        }
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
