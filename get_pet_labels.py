                                                                            
# PROGRAMMER: Lana Palmer
# DATE CREATED: March 29, 2020                                
# REVISED DATE: 

# Imports python modules
from os import listdir



def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    filenames = listdir(image_dir)
    
    def pet_label(filename):
        low_pet_image = filename.lower()
        word_list_pet_image = low_pet_image.split("_")
        pet_name = ""
        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word + " "
        pet_name = pet_name.strip()
        return pet_name
    
    results_dic = dict()
    
    for filename in filenames:
        if filename[0] != '.':
            
            if filename not in results_dic:
                results_dic[filename] = [pet_label(filename)]
            else:
                print("** Warning: Duplicate files exist in directory:", filename)

    return results_dic