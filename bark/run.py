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
# preload_models()

# t0 = time.time()
# text = "In the light of the moon, a little egg lay on a leaf"
# audio_array = generate_audio(text)
# generation_duration_s = time.time() - t0
# audio_duration_s = audio_array.shape[0] / SAMPLE_RATE
# print(audio_array.astype(np.float32).tostring())
# print(f"took {generation_duration_s:.0f}s to generate {audio_duration_s:.0f}s of audio")

class Item(BaseModel):
    prompt: str

app = FastAPI()

@app.post("/barkprocess/")
async def process_prompt(item: Item):

    # Process the prompt here, you can call external services or perform any other operations
    
    preload_models()

    t0 = time.time()
    # text = "In the light of the moon, a little egg lay on a leaf"
    audio_array = generate_audio(item.prompt)
    generation_duration_s = time.time() - t0
    audio_duration_s = audio_array.shape[0] / SAMPLE_RATE

    # print(f"took {generation_duration_s:.0f}s to generate {audio_duration_s:.0f}s of audio")

    # Example response
    # response = json.dumps(audio_array.tolist())

    
    return Response(content=audio_array.tobytes(), media_type="application/octet-stream")
