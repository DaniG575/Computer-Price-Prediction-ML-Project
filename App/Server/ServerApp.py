import fastapi
import fastapi.middleware
import fastapi.middleware.cors
from fastapi.responses import JSONResponse
import fastapi.encoders
import uvicorn
import json
import util

app = fastapi.FastAPI()
app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.post("/predict_price")
async def Predict(request : fastapi.Request):
    try:
        form = await request.form()
        Inches = float(form["inches"])
        Cpu = float(form["cpu"])
        Ram = float(form["ram"])
        Weight = float(form["weight"])
        HR = float(form["resolution"].split("x")[0])
        VR = float(form["resolution"].split("x")[1])
        SSD = float(form["ssd"])
        HDD = float(form["hdd"])
        graphics = str(form["graphics"])
        OS = str(form["os"])
        gentop = 1 if "tg" in form.keys() else 0

        # Perform prediction logic
        response = util.Predict(Inches, Cpu, Ram, Weight, HR, VR, SSD, HDD, graphics, OS, gentop)[0]
        response = float(round(response, 1))
        
        return JSONResponse(status_code=200, content={"predictedPrice": response})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})



if __name__ == "__main__":
    uvicorn.run(app, port=5000, host="127.0.0.1")
