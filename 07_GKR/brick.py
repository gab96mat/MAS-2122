import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import math as m
import simple_comm as c
import simple_ur_script as ur




class Brick(object):
    REFERENCE_LENGTH = 12.5
    REFERENCE_WIDTH = 6
    REFERENCE_HEIGHT = 4

    def __init__(self, plane, length=REFERENCE_LENGTH, width=REFERENCE_WIDTH, height=REFERENCE_HEIGHT):
        """Brick containes picking plane, placing plane and geometry

        Parameters
        ----------
        plane : Rhino Geometry plane
        this plane describes the possition and orientation of the Brick

        """
        self.plane = plane
        self.length = length
        self.width = width
        self.height = height



    def pts(self):
        """returns 8 points describing the brick:

        Returns
        ----------
        [pt0 : bottom point at origin,
        pt1 : bottom point at possitive Y,
        pt2 : bottom point at possitive X,
        pt3 : bottom point at possitive X and poossitive Y,
        pt4 : top point at origin,
        pt1 : top point at possitive Y,
        pt2 : top point at possitive X,
        pt3 : top point at possitive X and poossitive Y]

        """

        pt_0 = rg.Point3d(0, 0, 0)
        pt_1 = rg.Point3d(self.length, 0, 0)
        pt_2 = rg.Point3d(self.length, self.width, 0)
        pt_3 = rg.Point3d(0, self.width, 0)

        pt_4 = rg.Point3d(0, 0, self.height)
        pt_5 = rg.Point3d(self.length, 0, self.height)
        pt_6 = rg.Point3d(self.length, self.width, self.height)
        pt_7 = rg.Point3d(0, self.width, self.height)

        b_pts = [pt_0, pt_1, pt_2, pt_3, pt_4, pt_5, pt_6, pt_7]

        return b_pts

    def origin(self):
        """returns the origin plane in the centre of the base of the brick:

        Returns
        ----------
        [Rhino Geometry Plane]

        """
        vec = (self.pts()[2]-self.pts()[0])/2
        origin = self.pts()[0] + vec
        plane = rg.Plane(origin, rg.Vector3d.XAxis, rg.Vector3d.YAxis)
        return plane

    def transformation(self):
        """Transoformation matrix fot transformating the brick to the brick possiotn:

        Returns
        ----------
        [Rhino Geometry Transformation]

        """
        return rg.Transform.PlaneToPlane(self.origin(), self.plane)

    def base_plane(self):
        """Base plane of the transformed brick:

        Returns
        ----------
        [Rhino Geometry Plane]

        """

        p_plane = self.origin()
        p_plane.Transform(self.transformation())
        return p_plane

    def picking_plane(self):
        """Robot's picking plane on the transformed brick:

        Returns
        ----------
        [Rhino Geometry Plane]

        """
        p_plane = self.origin()
        p_pt = p_plane.Origin
        p_plane = rg.Plane(p_pt+rg.Vector3d(0, 0, self.height),
                           p_plane.XAxis, p_plane.YAxis)

        p_plane.Transform(self.transformation())
        return p_plane

    def surface(self):
        """NURB surfaces depicting the brick:

        Returns
        ----------
        [srf0 : base surface,
        srf1 : long edge,
        srf2 : top surface
        srf3 : long edge,
        srf4 : short edge
        srf5 : short edge]

        """
        tran_brick_pts = []
        for pt in self.pts():
            transformation_pt = pt.Clone()
            transformation_pt.Transform(self.transformation())
            tran_brick_pts.append(transformation_pt)

        pt_0, pt_1, pt_2, pt_3, pt_4, pt_5, pt_6, pt_7 = tran_brick_pts

        srf_0 = rg.NurbsSurface.CreateFromPoints(
            [pt_0, pt_1, pt_3, pt_2], 2, 2, 1, 1)
        srf_1 = rg.NurbsSurface.CreateFromPoints(
            [pt_0, pt_1, pt_4, pt_5], 2, 2, 1, 1)
        srf_2 = rg.NurbsSurface.CreateFromPoints(
            [pt_4, pt_5, pt_7, pt_6], 2, 2, 1, 1)
        srf_3 = rg.NurbsSurface.CreateFromPoints(
            [pt_6, pt_7, pt_2, pt_3], 2, 2, 1, 1)
        srf_4 = rg.NurbsSurface.CreateFromPoints(
            [pt_0, pt_3, pt_4, pt_7], 2, 2, 1, 1)
        srf_5 = rg.NurbsSurface.CreateFromPoints(
            [pt_1, pt_2, pt_5, pt_6], 2, 2, 1, 1)

        return (srf_0, srf_1, srf_2, srf_3, srf_4, srf_5)

    def mesh(self):
        """Mesh  depicting the brick:

        Returns
        ----------
        mesh_brick : Mesh
        """

        mesh_brick = rg.Mesh.CreateFromBox(self.pts(), 1, 1, 1)
        mesh_brick.Transform(self.transformation())

        return mesh_brick

