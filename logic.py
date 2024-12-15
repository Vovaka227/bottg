from kandinskylib import Kandinsky
from config import api_key, secret_key
import random
client = Kandinsky(api_key, secret_key)
# Generate an image
def gen_img(prompt = "cat", style = "UHD", negative_prompt = "neon", scale = '3:2'):
   rnd_name = str(random.randint(1,10000)).zfill(5)
   path=f"./image/generated_image{rnd_name}.jpg"
   response = client.generate_image(
        prompt=prompt,
        scale=scale,
        style=style,
        negative_prompt=negative_prompt,
        path=f"./image/generated_image{rnd_name}.jpg"
    )
   return f"./image/generated_image{rnd_name}.jpg"
#print(generate_image(prompt="A cat in sunglasses", style="UHD", negative_prompt="Bright colors, neon colors", scale='3:2'))
