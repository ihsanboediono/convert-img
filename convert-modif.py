import os
import sys
import glob
from PIL import Image
from tqdm import tqdm


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def image_conversion(image_file, dest_format, dest_folder):
    image_name, image_extension = os.path.splitext(image_file)
    image_format = image_extension.lstrip('.')

    output_path = os.path.join(dest_folder, os.path.basename(image_name) + "." + dest_format)

    if image_format.lower() == dest_format.lower():
        with open(image_file, 'rb') as src, open(output_path, 'wb') as dst:
            dst.write(src.read())
    else:
        image = Image.open(image_file)
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        if dest_format.lower() == 'jpg':
            image.save(output_path, "JPEG", quality=95)
        else:
            image.save(output_path, dest_format.upper())


def main():
    path = os.getcwd()
    no = 1
    novel = []
    for dir in os.scandir(path):
        if os.path.isdir(dir):
            # print(str(no)+ ". " + os.path.basename(dir))
            if os.path.basename(dir) != "baru" :
                novel.append(os.path.basename(dir))
            no = no+1
    
    noo = 1
    for a in novel:
        print(str(noo)+ ". " +a)
        noo = noo+1
    
    pilih = input("Novel nomor berapa : ")

    print("1. jpg")
    print("2. png")
    print("3. jpeg")
    pilih_ext = input("ekstensi : ")

    

    ext = ["jpg", "png", "jpeg"]


    source_folder = novel[int(pilih)-1]
    
    converted_folder = 'converted'+" "+source_folder
    destination_format = ext[int(pilih_ext)-1]

    create_dir(converted_folder)

    allowed_file_extensions = ('webp', 'png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif', 'jfif')
    source_files = list(glob.glob(os.path.join(source_folder, '*')))

    print("Converting images...")

    for source_file in tqdm(source_files):
        _, file_extension = os.path.splitext(source_file)
        if file_extension.lstrip('.').lower() not in allowed_file_extensions:
            continue

        if os.path.isfile(source_file):
            image_conversion(source_file, destination_format.lower(), converted_folder)

    print("Finished converting images.")


if __name__ == '__main__':
    main()