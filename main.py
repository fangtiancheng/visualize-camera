import argparse
from src import BlenderVisualizer, MatplotlibVisualizer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--cam_file", help="camera file", type=str, default='./resources/dataset-actorhq.json')
    parser.add_argument("--vis_type", help="visualization type", type=str, default='matplotlib',
                        choices=['matplotlib', 'blender'])
    args = parser.parse_args()

    visualizer = None
    if args.vis_type == 'matplotlib':
        visualizer = MatplotlibVisualizer(args.cam_file)
    else:
        visualizer = BlenderVisualizer(args.cam_file)
    visualizer.visualize()