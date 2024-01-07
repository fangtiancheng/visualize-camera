from .base import VisualizerBase
import os

class BlenderVisualizer(VisualizerBase):
    def __init__(self, dataset_path: str) -> None:
        super().__init__(dataset_path)
    
    def visualize(self):
        blender_source = (
            "import bpy\n"
            "import json\n"
            "from mathutils import Matrix\n"
            "from typing import List, Tuple\n"
            "def create_camera(cam_name:str):\n"
            "    camera_data  = bpy.data.cameras.new(name=cam_name)\n"
            "    camera_object = bpy.data.objects.new(cam_name, camera_data)\n"
            "    bpy.context.scene.collection.objects.link(camera_object)\n"
            "    return camera_object\n\n"
            "if __name__ == '__main__':\n"
            f"    cam_file = '{os.path.abspath(self.dataset_path)}'\n"
            "    with open(cam_file, 'r') as f:\n"
            "        cameras = json.load(f)['frames']\n"
            "    for cam_data in cameras:\n"
            "        camera = create_camera(cam_data['camera_name'])\n"
            "        camera.matrix_world = Matrix(cam_data['transform_matrix'])\n"
        )
        output_path = './resources/blender-out.py'
        with open(output_path, 'w') as f:
            f.write(blender_source)
        print('blender script is saved to "%s"'%output_path)