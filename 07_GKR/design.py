import Rhino.Geometry as rg
import random as r


class Design(object):
    # class variable
    BRICK_LENGTH = 10.
    BRICK_WIDTH = 7.5
    BRICK_HEIGHT = 5.

    def __init__(self, layer_num):
        # instance variable
        self.base_crvs = self.gen_base_crvs(layer_num)

    def gen_base_crvs(self, layer_num):
        # prepare empty list
        base_crvs = []
        # stack base curves
        for i in range(layer_num):
            # set an BaseCrv object
            bc = BaseCrv(i)
            base_crvs.append(bc)
        return base_crvs


class BaseCrv(Design):
    def __init__(self, layer_cnt):
        # set hardcoded values
        self.x_scale = 50
        self.y_scale = 50
        self.ctrl_pts_cnt = 5
        # set input argument
        self.layer_cnt = layer_cnt
        # prepare empty list to store values
        self.ctrl_pts = self.gen_ctrl_pts()
        self.base_crv = self.gen_base_crv(self.ctrl_pts)
        self.brick_pls = self.get_brick_pls()
        self.bricks = self.gen_brick_obj()

    def gen_ctrl_pts(self):
        # prepare empty list
        ctrl_pts = []
        # set random factor along y axis
        y_factor = r.random() - 0.5
        # generate random points along x axis.
        for i in range(self.ctrl_pts_cnt):
            # create a point
            ctrl_pt = rg.Point3d(i*self.x_scale,
                                 0,
                                 self.BRICK_HEIGHT*self.layer_cnt)
        # append a point into a list
            ctrl_pts.append(ctrl_pt)
        return ctrl_pts

    def gen_base_crv(self, ctrl_pts):
        # create a base curve from the control points generated above.
        base_crv = rg.NurbsCurve.CreateInterpolatedCurve(ctrl_pts, degree=3)
        return base_crv

    def get_brick_pls(self):
        # create a list of points to put bricks
        brick_pls = []
        # divide the base_crv based onthe BRICK_LENGTH
        params = self.base_crv.DivideByLength(self.BRICK_LENGTH/2, False)
        # use loop to get points from parameters on one of the base_crvs
        # even bricks in even layer indexs
        if self.layer_cnt % 2 == 0:
            for i in range(0, len(params), 2):
                pl = self.gen_plane(self.base_crv, params[i])
                # append points into a list
                brick_pls.append(pl)
        # odd bricks in odd layer indexs
        elif self.layer_cnt % 2 == 1:
            for i in range(1, len(params), 2):
                pl = self.gen_plane(self.base_crv, params[i])
                # append points into a list
                brick_pls.append(pl)
        return brick_pls

    def gen_plane(self, crv, param):
        # get a point at the parameter
        brick_pt = crv.PointAt(param)
        brick_tan = crv.TangentAt(param)
        brick_norm = rg.Vector3d.CrossProduct(rg.Vector3d.ZAxis, brick_tan)
        # create a plane
        pl = rg.Plane(brick_pt, brick_tan, brick_norm)
        return pl

    def gen_brick_obj(self):
        bricks = []
        for i, pl in enumerate(self.brick_pls):
            b = Brick(pl,
                      layer_cnt=self.layer_cnt,
                      brick_cnt=i)
            bricks.append(b)
        return bricks


class Brick(Design):
    def __init__(self, plane, layer_cnt, brick_cnt):
        """Brick containes picking plane, placing plane and geometry

        Parameters
        ----------
        plane : Rhino Geometry plane
        this plane describes the possition and orientation of the Brick

        """
        self.plane = plane
        self.layer_cnt = layer_cnt
        self.brick_cnt = brick_cnt

        self.corner_pts = self.gen_brick_corner_pts()
        self.surface = self.surface()
        self.mesh = self.mesh()

    def gen_brick_corner_pts(self):
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
        pt_1 = rg.Point3d(self.BRICK_LENGTH, 0, 0)
        pt_2 = rg.Point3d(self.BRICK_LENGTH, self.BRICK_WIDTH, 0)
        pt_3 = rg.Point3d(0, self.BRICK_WIDTH, 0)

        pt_4 = rg.Point3d(0, 0, self.BRICK_HEIGHT)
        pt_5 = rg.Point3d(self.BRICK_LENGTH, 0, self.BRICK_HEIGHT)
        pt_6 = rg.Point3d(self.BRICK_LENGTH, self.BRICK_WIDTH, self.BRICK_HEIGHT)
        pt_7 = rg.Point3d(0, self.BRICK_WIDTH, self.BRICK_HEIGHT)

        b_pts = [pt_0, pt_1, pt_2, pt_3, pt_4, pt_5, pt_6, pt_7]

        return b_pts

    def get_original_base_plane(self):
        """returns the origin plane in the centre of the base of the brick:

        Returns
        ----------
        [Rhino Geometry Plane]

        """
        pts = self.corner_pts
        vec = (pts[2]-pts[0])/2
        origin = pts[0] + vec
        plane = rg.Plane(origin, rg.Vector3d.XAxis, rg.Vector3d.YAxis)
        return plane

    def calc_base_transformation(self):
        """Transoformation matrix fot transformating the brick to the brick possiotn:

        Returns
        ----------
        [Rhino Geometry Transformation]

        """
        original_base_pl = self.get_original_base_plane()
        T = rg.Transform.PlaneToPlane(original_base_pl, self.plane)
        return T

    def calc_pickup_transformation(self):
        """Transoformation matrix fot transformating the brick to the brick possiotn:

        Returns
        ----------
        [Rhino Geometry Transformation]

        """
        original_base_pl = self.get_original_base_plane()
        T = rg.Transform.PlaneToPlane(original_base_pl, self.plane)
        return T

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
        for pt in self.corner_pts:
            transformation_pt = pt.Clone()
            transformation_pt.Transform(self.calc_base_transformation())
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

        mesh_brick = rg.Mesh.CreateFromBox(self.corner_pts, 1, 1, 1)
        mesh_brick.Transform(self.calc_base_transformation())

        return mesh_brick
