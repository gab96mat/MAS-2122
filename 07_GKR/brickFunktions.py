import Rhino.Geometry as rg
import copy

global LENGTH
global WIDTH
global HEIGHT

LENGTH = 12.5
WIDTH = 6
HEIGHT = 8



def brick(plane):
    """ List of rg.Points definding the corners of the brick

    Returns
    ----------
    [pt0 : bottom point at negative x and negative y,
    pt1 : bottom point at negative x and possitive y,
    pt2 : bottom point at possitive x and possitve y,
    pt3 : bottom point at possitive x and negative y,
    pt4 : pt0 + Thickness,
    pt5 : pt1 + Thickness,
    pt6 : pt2 + Thickness,
    pt7 : pt3 + Thickness]
    """



    origin = plane.Origin

    x_vec = plane.XAxis #rg.Plane.XAxis
    y_vec = plane.YAxis
    z_vec = plane.ZAxis

    pt_0 = origin - (x_vec *LENGTH/2) - (y_vec*WIDTH/2)
    pt_1 = origin + (x_vec *LENGTH/2) - (y_vec*WIDTH/2)
    pt_2 = origin + (x_vec *LENGTH/2) + (y_vec*WIDTH/2)
    pt_3 = origin - (x_vec *LENGTH/2) + (y_vec*WIDTH/2)

    pt_4 = pt_0 + (z_vec*HEIGHT)
    pt_5 = pt_1 + (z_vec*HEIGHT)
    pt_6 = pt_2 + (z_vec*HEIGHT)
    pt_7 = pt_3 + (z_vec*HEIGHT)

    pts = [pt_0, pt_1, pt_2, pt_3, pt_4, pt_5, pt_6, pt_7]



    return pts


def surface(s_pts):
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

    pt_0, pt_1, pt_2, pt_3, pt_4, pt_5, pt_6, pt_7 = s_pts

    srf_0 = rg.NurbsSurface.CreateFromPoints([pt_0, pt_1, pt_3, pt_2], 2, 2, 1, 1)
    srf_1 = rg.NurbsSurface.CreateFromPoints([pt_0, pt_1, pt_4, pt_5], 2, 2, 1, 1)
    srf_2 = rg.NurbsSurface.CreateFromPoints([pt_4, pt_5, pt_7, pt_6], 2, 2, 1, 1)
    srf_3 = rg.NurbsSurface.CreateFromPoints([pt_2, pt_3, pt_6, pt_7], 2, 2, 1, 1)
    srf_4 = rg.NurbsSurface.CreateFromPoints([pt_0, pt_3, pt_4, pt_7], 2, 2, 1, 1)
    srf_5 = rg.NurbsSurface.CreateFromPoints([pt_1, pt_2, pt_5, pt_6], 2, 2, 1, 1)

    return srf_0, srf_1, srf_2, srf_3, srf_4, srf_5


def mesh(m_pts):
    """Mesh  depicting the brick:

    Returns
    ----------
    mesh_brick : Mesh
    """
    mesh_brick = rg.Mesh.CreateFromBox(m_pts, 1,1,1)
    return mesh_brick


def plane(plane):
    """offsets the plane fo the brick with the thickness of the brick.
    Returns
    ----------
    p_plane : rg.Plane
    """

    offset_vec = plane.ZAxis * HEIGHT
    p_plane = copy.copy(plane)
    p_plane.Translate(offset_vec) #rg.Plane.Translate (plane, offset_vector)

    return p_plane


