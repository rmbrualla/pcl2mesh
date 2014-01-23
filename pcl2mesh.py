#!/usr/bin/python

import os, sys, os.path, argparse


parser = argparse.ArgumentParser(description='Convert point cloud to mesh.')
parser.add_argument('input_pcl', help='Input point cloud (PLY)')
parser.add_argument('output_mesh', help='Output mesh (PLY)')
parser.add_argument('depth', type=int,help='Poisson Reconstruction Depth')
args = parser.parse_args()

(root_path, t) = os.path.split(sys.argv[0]);

original_file = args.input_pcl
dest_file = args.output_mesh
(path,fname) = os.path.split(dest_file)
(name, ext) = os.path.splitext(fname)

tmp_mlx_file = os.path.join(path, '%s_tmp.mlx' % name)
cmd0 = 'sed s/%%DEPTH%%/%d/ < %s > %s' % (args.depth, os.path.join(root_path, 'proc1.mlx'), tmp_mlx_file)

tmp_file1 = os.path.join(path, '%s_tmp1.ply' % name)
cmd1 = 'meshlabserver -i %s -o %s -s %s  -om vc vn' % (original_file, tmp_file1, tmp_mlx_file)

tmp_file2 = os.path.join(path, '%s_tmp2.ply' % name)
cmd2 = 'meshlabserver -i %s %s -o %s -s %s  -om vc vn' % (tmp_file1, original_file, tmp_file2, os.path.join(root_path, 'proc2.mlx') )

cmd3 = 'meshlabserver -i %s -o %s -s %s  -om vc vn' % (tmp_file2, dest_file, os.path.join(root_path, 'proc3.mlx'))

cmd_clean = 'rm %s %s %s' % (tmp_mlx_file, tmp_file1, tmp_file2);

os.system(cmd0)
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
os.system(cmd_clean)

