import pygame
from os import walk


def map_folders(path):
    """Return all folders with assets that need to be imported"""
    for _,folder_list, __ in walk(path):
        return folder_list

def import_images(path):
    """Automatically import the images from all folders in a given path"""
    image_surfaces = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            image_surfaces.append(image_surface)

    return image_surfaces

def flip_animation(animation_list):
    flipped_animation = []

    for frame in animation_list:
        flipped_frame = pygame.transform.flip(frame, True, False)
        flipped_animation.append(flipped_frame)

    return flipped_animation