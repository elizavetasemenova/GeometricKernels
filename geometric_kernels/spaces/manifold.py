"""
Manifold: TODO
"""
import numpy as np

from geometric_kernels.spaces import Space


class Manifold(Space):
    """TODO"""

    @property
    def dim(self) -> int:
        pass

    def get_eigenfunctions(self, num: int):
        pass

    def get_eigenvalues(self, num: int) -> np.ndarray:
        """
        First `num` eigenvalues of the Laplace-Beltrami operator

        :return: [num, 1] array containing the eigenvalues
        """
        pass


# from geomstats.geometry.manifold import Manifold
