import os

os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["SUNO_USE_SMALL_MODELS"] = "1"

import numpy as np
import json

from bark import generate_audio, preload_models, SAMPLE_RATE

from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
import time
from pydantic import BaseModel

# Import the logging module
import logging

# Configure the logging settings
logging.basicConfig(level=logging.DEBUG)

# Print debug message
logging.debug("Starting the run module")


class Item(BaseModel):
    prompt: str

app = FastAPI()

@app.post("/barkprocess/")
async def process_prompt(item: Item):

    # Process the prompt here, you can call external services or perform any other operations
    
    preload_models()

    t0 = time.time()

    audio_array = generate_audio(item.prompt)
    generation_duration_s = time.time() - t0
    audio_duration_s = audio_array.shape[0] / SAMPLE_RATE

    # Print debug message
    logging.debug("Finished running the run module")

    
    return Response(content=audio_array.tobytes(), media_type="application/octet-stream")
