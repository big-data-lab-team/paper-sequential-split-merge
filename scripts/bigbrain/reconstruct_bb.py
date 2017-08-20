import nibabel as nib
import os
import h5py
import numpy as np
import math
import sys
import argparse
from time import time


def reconstruct(legend_fn, reconstructed_fn, block_folder, block_prefix, block_suffix, bytes_per_voxel):

    legend = nib.load(legend_fn).get_data()
    reconstructed_img = nib.load(reconstructed_fn)


    ystart_0 = 0
    zstart_0 = 0
    xstart_0 = 0

    blocks_copied =  {}

    bb_header = reconstructed_img.header

    try:
      header_size = bb_header.single_vox_offset
    except:
      print 'ERROR: File not a NIfTI image'
      sys.exit(1)

    bb_ydim = bb_header.get_data_shape()[0]
    bb_zdim = bb_header.get_data_shape()[1]
    bb_xdim = bb_header.get_data_shape()[2]

    with open(reconstructed_fn, "r+b") as reconstructed:
        for x in range(0, legend.shape[2]):
            for y in range(0, legend.shape[0]):
                for z in range(0, legend.shape[1]):
                   
                    block_num = str(int(legend[y][z][x])).zfill(3) 
                    
                    block_filename = '{0}-0{1}-{2}'.format(os.path.join(block_folder,block_prefix), block_num, block_suffix)
                    
                    if block_num in blocks_copied:
                        continue
                    else:
                        blocks_copied[block_num] = 1

                    block_img = nib.load(block_filename)
                    header = block_img.header
                    shape = header.get_data_shape()
                    ydim = shape[0]
                    zdim = shape[1]
                    xdim = shape[2]

                    block_data = block_img.get_data()

                    start = header['descrip'].tostring().strip('\x00').split()
                    step = header['pixdim']

                    ystep = round(float(step[1]), 2)
                    zstep = round(float(step[2]), 2)
                    xstep = round(float(step[3]), 2)
                   

                    ystart = float(start[0].strip())
                    zstart = float(start[1].strip())
                    xstart = float(start[2].strip())

                    #get first block's start values to compare position with other blocks
                    if y == 0 and z == 0 and x == 0 :
                        ystart_0 = ystart
                        zstart_0 = zstart
                        xstart_0 = xstart

                    y_block = int(abs((ystart-ystart_0)/ystep))
                    z_block = int(abs((zstart-zstart_0)/zstep))
                    x_block = int(abs((xstart-xstart_0)/xstep))

                    for i in range(0,xdim):
                        for j in range(0, zdim):
                            reconstructed.seek(header_size + bytes_per_voxel*(y_block + (z_block + j)*bb_ydim +(x_block + i)*bb_ydim*bb_zdim), 0)
                            reconstructed.write(block_data[:, j,i].tobytes())
                            
                     

if __name__ == "__main__":


    # sample command: python reconstruct_bb.py legend1000_1.mnc /data/reconstructed_bb.nii /data/nifti-blocks/ block40 inv.nii.gz np.ushort
    # NOTE: the reconstructed image's filepath points to an 0-filled image created by imageutils' generate_zero_nifti function

    parser = argparse.ArgumentParser(description='Reconstruct a nifti image given blocks and a legend')
    parser.add_argument('legend', type=str, help='The legend image to be used for reconstruction')
    parser.add_argument('emptyimg', type=str, help="The template nifti-1 image that will be used as the reconstructed image.")
    parser.add_argument('blockfldr', type=str, help="The folder containing the blocks")
    parser.add_argument('blockprfx', type=str, help="The block name prefix. ex: block-0001-inv.nii, prefix = block")
    parser.add_argument('blocksffx', type=str, help="The block name suffix. ex: block-0001-inv.nii, suffix = inv.nii")
    parser.add_argument('dtype', type=str, help="Numpy datatype \
                                                            (np.int16, np.ushort, np.uint16, np.float32,\
                                                            np.float64).")

    args = parser.parse_args()

    legend = args.legend
    reconstructed_fn = args.emptyimg
    
    block_folder = args.blockfldr
    block_prefix = args.blockprfx
    block_suffix = args.blocksffx

    bytes_per_voxel = 0

    if args.dtype == "np.int16":
        bytes_per_voxel = np.dtype(int16).itemsize
    elif args.dtype == "np.ushort":
        bytes_per_voxel = np.dtype(np.ushort).itemsize
    elif args.dtype == "np.uint16":
        bytes_per_voxel = np.dtype(np.uint16).itemsize
    elif args.dtype == "np.float32":
        bytes_per_voxel = np.dtype(np.float32).itemsize
    else:
        bytes_per_voxel = np.dtype(np.float64).itemsize

    reconstruct(legend, reconstructed_fn, block_folder, block_prefix, block_suffix, bytes_per_voxel)
