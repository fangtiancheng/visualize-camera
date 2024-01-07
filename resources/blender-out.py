import bpy
import json
from mathutils import Matrix
from typing import List, Tuple
def create_camera(cam_name:str):
    camera_data  = bpy.data.cameras.new(name=cam_name)
    camera_object = bpy.data.objects.new(cam_name, camera_data)
    bpy.context.scene.collection.objects.link(camera_object)
    return camera_object

if __name__ == '__main__':
    cam_file = '/media/ftc/G/code/visualize-camera/resources/dataset-actorhq.json'
    with open(cam_file, 'r') as f:
        cameras = json.load(f)['frames']
    for cam_data in cameras:
        camera = create_camera(cam_data['camera_name'])
        camera.matrix_world = Matrix(cam_data['transform_matrix'])
