import sys
import os
#import numpy as np
from PIL import Image
import rembg

session = rembg.new_session("u2netp")

def process(session, image, size=None, bgcolor='white'):
    "session is a rembg Session, and image is a PIL Image"
    if size is not None:
        image = image.resize(size)
    else:
        size = image.size
    result = Image.new("RGB", size, bgcolor)
    out = rembg.remove(image, session=session)
    result.paste(out, mask=out)
    return result

def remove_background(file_to_rm_bk):

   
    file_to_save_arr=os.path.basename(file_to_rm_bk).split('.')

    if(len(file_to_save_arr)<2): 
        raise Exception("invalid file")  

    file_to_save=file_to_save_arr[0]
    file_to_save_ext=file_to_save_arr[1]
    Output_path=f"{file_to_save}_rm_bk.{file_to_save_ext}"

    input_image = Image.open(file_to_rm_bk)
    output_image = process(session, input_image , None, bgcolor='#FFFFFF')
# color replace
#    data = np.array(im)
#    # just use the rgb values for comparison
#    rgb = data[:,:,:3]
#    color = [246, 213, 139]   # Original value
#    black = [0,0,0, 255]
#    white = [255,255,255,255]
#    mask = np.all(rgb == color, axis = -1)
#    # change all pixels that match color to white
#    data[mask] = white
#
#    # change all pixels that don't match color to black
#    ##data[np.logical_not(mask)] = black
#    new_im = Image.fromarray(data)
#    new_im=new_im.convert('RGB')
#   Convert the input image to a numpy array
    #input_image = input_image.convert('RGBA')
    #input_array=np.array(input_image)
    #output_array=remove(input_array)
    # Create a PIL Image from the output array
    #output_image = Image.fromarray(output_array)
    #output_image = output_image.convert("RGB")
    
    output_image.save(Output_path)
    

if __name__ == "__main__":
    # Check if a file argument is provided
    if len(sys.argv) != 2:
        print("Usage: python background_remove.py /path/to/your/file")
        sys.exit(1)

    # Get the target file from the command-line argument
    target_file = sys.argv[1]

    # Call the function to remove background
    remove_background(target_file)
