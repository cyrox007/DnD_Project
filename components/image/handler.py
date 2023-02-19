import os, string, random, base64

from werkzeug.utils import secure_filename
import cv2

from settings import config

def image_processing(img, full_path_file):
    loaded_img = cv2.imread(img, cv2.IMREAD_COLOR)
    cropped_image = crop_image(loaded_img)
    changed_size_img = resize(cropped_image)
    cv2.imwrite(full_path_file, changed_size_img, [cv2.IMWRITE_WEBP_QUALITY]) # Сохраняем

def image_verification(filename) -> str:
    # формируем данные для БД
    new_filename: str = "photo_"+str(hash(filename))+".webp"
    full_path_file = os.path.join(config.FULL_AVATAR_DIR, new_filename) # путь для сохранения
    path_to_the_file = os.path.join(config.AVATAR_DIR, new_filename) # путь для БД
    
    return {
        "for_db": path_to_the_file,
        "for_save": full_path_file
    }

def resize(img, interp=cv2.INTER_LINEAR):
    new_width = 150 
    new_height = 150
    h, w = img.shape[:2]
    if img.shape[0] > 150 or img.shape[1] > 150:
        if new_width is None and new_height is None:
            return img

        if new_width is None:
            ratio = new_height / h
            dimension = (int(w * ratio), new_height)
            
        else: 
            ratio = new_width / w
            dimension = (new_width, int(h * ratio))
            
        return cv2.resize(img, dimension, interpolation=interp)
    
    return img


def crop_image(img: cv2.imread):
    himg = img.shape[0] # height
    wimg = img.shape[1] # width
    if himg == wimg:
        return img

    if himg > wimg:
        size = int((himg - wimg) / 2)
        begin_coord_y = int(size)
        end_coord_y = int(himg-size)
        return img[begin_coord_y:end_coord_y, 0:wimg]
    else:
        size = int((wimg - himg) / 2)
        begin_coord_x = int(size)
        end_coord_x = int(wimg-size)
        return img[0:himg, begin_coord_x:end_coord_x]

    
def temporary_saving(file) -> str:
    temp_filepath = os.path.join(
        config.PATH_TO_DIR+'/static/uploads/av_temp/', 
        secure_filename(file["Value"][-1])
        )
    file.save(temp_filepath)
    return temp_filepath

def avatar_processing(file: str, new_path: str) -> None:
    if file == '':
        return
    image_processing(file, new_path)
    os.remove(file)

def decode_image(raw):
    filename = ''.join(random.choice(string.ascii_lowercase) for i in range(10))+".png"
    filepath = os.path.join(
        config.PATH_TO_DIR+'/static/uploads/av_temp/', 
        filename
        )
    img = open(filepath, "wb")
    img.write(base64.b64decode(raw))
    img.close()
    return filepath