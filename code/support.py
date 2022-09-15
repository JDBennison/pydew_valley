import imp
from os import walk
import pygame


def import_folder(path):
    image_list = []
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_list.append(full_path)
    for image in sorted(image_list):
        image_surf = pygame.image.load(image).convert_alpha()
        surface_list.append(image_surf)
    return surface_list


def import_folder_dict(path):
    surface_dict = {}

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_dict[image.split('.')[0]] = image_surf

    return surface_dict
