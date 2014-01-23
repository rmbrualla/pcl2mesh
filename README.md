pcl2mesh
========

Script to generate a mesh from a point cloud.
Requires Python and meshlabserver.

Meshlabserver requires X, if called in a shell and 
it's not working, just do "ssh -X" to the same machine.



usage: pcl2mesh.py [-h] input_pcl output_mesh depth

Convert point cloud to mesh.

positional arguments:
  input_pcl    Input point cloud (PLY)
  output_mesh  Output mesh (PLY)
  depth        Poisson Reconstruction Depth

optional arguments:
  -h, --help   show this help message and exit

