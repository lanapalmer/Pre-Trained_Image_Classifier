                                                                       
# PROGRAMMER: Lana Palmer
# DATE CREATED: March 29, 2020                                   
# REVISED DATE: 

##
# Imports python modules
import argparse


# 
def get_input_args():

    # Create Parse using ArgumentParser
    my_parser = argparse.ArgumentParser()    
   
    my_parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to folder of images')
    my_parser.add_argument('--arch', type=str, default = 'vgg' )
    my_parser.add_argument('--dogfile', type=str, default = 'dognames.txt' )
   
    return my_parser.parse_args()