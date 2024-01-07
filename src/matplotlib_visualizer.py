from .base import VisualizerBase
from matplotlib import pyplot as plt
import numpy as np
from scipy.spatial.transform import Rotation

class MatplotlibVisualizer(VisualizerBase):
    def __init__(self, dataset_path:str):
        super().__init__(dataset_path)

    def visualize(self):
        cameras = self.cameras
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-1.0, 4.0)
        ax.set_zlim(-2.5, 2.5)

        def draw_axis(c:np.ndarray, v:np.ndarray, color:str):
            p = c + v
            ax.plot([c[0], p[0]], [c[1], p[1]], [c[2], p[2]], color=color, lw=1)

        s = 0.1
        draw_axis(np.array([0, 0, 0]), np.array([s, 0, 0]), "red")
        draw_axis(np.array([0, 0, 0]), np.array([0, s, 0]), "green")
        draw_axis(np.array([0, 0, 0]), np.array([0, 0, s]), "blue")
        for camera in cameras:
            mat4x4 = np.array(camera['transform_matrix'], dtype=np.float32)
            rotation = Rotation.from_matrix(mat4x4[:3,:3])
            translation = mat4x4[:3, 3]
            draw_axis(translation, rotation.apply(np.array([s, 0, 0])), "red")
            draw_axis(translation, rotation.apply(np.array([0, s, 0])), "green")
            draw_axis(translation, rotation.apply(np.array([0, 0, s])), "blue")
        plt.show()