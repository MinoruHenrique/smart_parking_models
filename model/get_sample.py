import os
import shutil
import random

DATA_DIR = "D:\Smart parking\Data\PKLot\PKLotSegm_joined"
DESTINATION_DIR = "D:\Smart parking\Data\PKLot\PKLotSegm_sample"
random.seed(100)

if not os.path.exists(os.path.join(DESTINATION_DIR, "Empty")):
    os.makedirs(os.path.join(DESTINATION_DIR,"Empty"))
    print("Empty folder created succesfully")

if not os.path.exists(os.path.join(DESTINATION_DIR, "Occupied")):
    os.makedirs(os.path.join(DESTINATION_DIR,"Occupied"))
    print("Occupied folder created succesfully")

empty_images = os.listdir(os.path.join(DATA_DIR,"Empty"))
occupied_images = os.listdir(os.path.join(DATA_DIR,"Occupied"))

print(f"Empty: {len(empty_images)}")
print(f"Occupied: {len(occupied_images)}")

sample_empty_sz = 5000
sample_occupied_sz = 5000

empty_sample = random.sample(empty_images, sample_empty_sz)
occupied_sample = random.sample(occupied_images, sample_occupied_sz)


for empty_image in empty_sample:
    img_dir = os.path.join(DATA_DIR, "Empty", empty_image)
    dest_dir = os.path.join(DESTINATION_DIR, "Empty", empty_image)
    shutil.copyfile(img_dir,dest_dir)

for occupied_image in occupied_sample:
    img_dir = os.path.join(DATA_DIR, "Occupied", occupied_image)
    dest_dir = os.path.join(DESTINATION_DIR, "Occupied", occupied_image)
    shutil.copyfile(img_dir,dest_dir)

