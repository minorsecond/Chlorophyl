import laspy
import numpy as np
from shapely.geometry import Point
from geopandas import GeoSeries


class PointCloud:
    """
    Point cloud object
    """

    def __init__(self, path):
        self.in_file = laspy.file.File(path)
        dataset = np.vstack([self.in_file.x, self.in_file.y, self.in_file.z]).transpose()

        self.point_number = dataset.shape[0]

    def get_vegetation(self):
        """
        Get the vegetation points from the point cloud.
        :return: Vegetation
        """

        vegetation = np.where(np.logical_and(np.logical_or(np.logical_or(self.in_file.raw_classification == 3,
                                                                         self.in_file.raw_classification == 4),
                                                           self.in_file.raw_classification == 5),
                                             self.in_file.num_returns == 1))

        single_vegetation_points = self.in_file.points[vegetation]
        single_vegetation_points_xyz = np.array((single_vegetation_points['point']['X'],
                                                single_vegetation_points['point']['Y'],
                                                single_vegetation_points['point']['Z'])).transpose()

        gs = GeoSeries(map(Point, single_vegetation_points_xyz))
        return gs
