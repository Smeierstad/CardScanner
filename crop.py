from PIL import Image
import os
from tqdm import tqdm

dir = "cards"

for filename in tqdm(os.listdir(dir)):
    f = os.path.join(dir, filename)
    if os.path.isfile(f):
        with Image.open(f) as im:
            im_crop = im.crop((0, 500, 2600, 1200))
            newName = r"processed_" + f
            im_crop.save(newName)

