# ghpython_02_compas

> Sample code for compas in ghpython.
> For general compas code, see vsc_py_02_compas(to be uploded)

## Requirements

Install the following tools:

- [Rhinoceros](https://www.rhino3d.com/)
- [Anaconda](https://www.anaconda.com/products/individual)

## Getting started

If you already have installed `compas` and `compas_rhino`, skip installation and explore files.

Create an environment using `Anaconda Prompt`:

    conda config --add channels conda-forge
    conda create -n NAME_OF_ENV COMPAS

Activate the environment and check if the installation process was successful:

    conda activate NAME_OF_ENV
    python -m compas

Install `compas_rhino`to your environment (note: select your version of rhino):

    python -m compas_rhino.install -v 6.0
    python -m compas_rhino.install -v 7.0

Open `Grasshopper` and type below in the command line in Rhinoceros3d:

    grasshopper

Verify the setup.
Open GhPython compnent on your Grasshopper canvas and paste the following script and hit OK:

    import compas
    from compas.datastructures import Mesh
    from compas_ghpython.artists import MeshArtist

    mesh = Mesh.from_obj(compas.get('faces.obj'))

    a = MeshArtist(mesh).draw()


🚀 You're ready! 

Open and explore the `NUM_NAME.ghx` files in grasshopper.


For more details, see

- [COMPAS Installation](https://compas.dev/compas/latest/installation.html)
- [COMPAS Rhino](https://compas.dev/compas/latest/gettingstarted/rhino.html)
- [COMPAS Grasshopper](https://compas.dev/compas/latest/gettingstarted/grasshopper.html)
