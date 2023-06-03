import os
import shutil

DATA_DIR = "D:\Smart parking\Data\PKLot\PKLotSegmented"
DESTINATION_DIR = "D:\Smart parking\Data\PKLot\PKLotSegm_joined"

if not os.path.exists(os.path.join(DESTINATION_DIR, "Empty")):
    os.makedirs(os.path.join(DESTINATION_DIR,"Empty"))
    print("Empty folder created succesfully")

if not os.path.exists(os.path.join(DESTINATION_DIR, "Occupied")):
    os.makedirs(os.path.join(DESTINATION_DIR,"Occupied"))
    print("Occupied folder created succesfully")

subsets = os.listdir(DATA_DIR)
for subset in subsets:
    SUBSET_DIR = os.path.join(DATA_DIR, subset)
    kinds = os.listdir(SUBSET_DIR)
    for kind in kinds:
        KIND_DIR = os.path.join(SUBSET_DIR, kind)
        days = os.listdir(KIND_DIR)
        for day in days:
            DAY_FOLDER = os.path.join(KIND_DIR, day)
            states_of_space = os.listdir(DAY_FOLDER)
            for state_of_space in states_of_space:
                COPY_FOLDER = os.path.join(DESTINATION_DIR, state_of_space)
                ORIGIN_FOLDER = os.path.join(DAY_FOLDER, state_of_space)
                images = os.listdir(ORIGIN_FOLDER)
                for image in images:
                    image_folder = os.path.join(ORIGIN_FOLDER, image)
                    image_copy_folder = os.path.join(COPY_FOLDER, image)
                    shutil.copyfile(image_folder, image_copy_folder)
                # print(state_of_space)