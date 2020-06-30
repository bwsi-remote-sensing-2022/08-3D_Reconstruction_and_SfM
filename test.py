import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os
import sys
import subprocess
import open3d as o3d

pcd = o3d.io.read_point_cloud("kitchen_example/undistorted/depthmaps/merged.ply")

o3d.visualization.draw_geometries([pcd])