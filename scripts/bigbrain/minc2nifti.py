import nibabel as nib
import h5py
import os
import numpy as np
import sys
import argparse


def get_dimensions(var):
    try:
        dimorder = var.attrs['dimorder']
    except KeyError:  # No specified dimensions
        return []
    return dimorder.split(',')

def convert2nifti(in_folder, out_folder, dtype, gzip=False):
    for mnc_block in os.listdir(in_folder):

        if mnc_block[-4:] != ".mnc":
            continue

        filepath = os.path.join(in_folder, mnc_block)
        block_header = h5py.File(filepath, 'r')

        minc_part = block_header['minc-2.0']
        # The whole image is the first of the entries in 'image'
        image = minc_part['image']['0']
        image_data = image['image']
        dim_names = get_dimensions(image_data)
        dimensions = minc_part['dimensions']

        dims = [dimensions[s].attrs.items() for s in dim_names]

        ydim = dims[0][0][1]
        zdim = dims[1][0][1]
        xdim = dims[2][0][1]

        ystep = dims[0][11][1]
        zstep = dims[1][10][1]
        xstep = dims[2][10][1]

        ystart = dims[0][12][1]
        zstart = dims[1][11][1]
        xstart = dims[2][11][1]


        data = nib.load(filepath).get_data().astype(dtype) 
        nifti = nib.Nifti1Image(data, np.eye(4))
        
        nifti.header['descrip'] =  '{0} {1} {2}'.format(ystart, zstart, xstart)
        
        nifti.header['pixdim'][1] = ystep
        nifti.header['pixdim'][2] = zstep
        nifti.header['pixdim'][3] = xstep

        print nifti.header['pixdim']

        nii_file = mnc_block[:-4] + '.nii'
        
        if gzip:
            nii_file += '.gz'
        
        nib.save(nifti, os.path.join(out_folder, nii_file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert minc images to nifti images')

    parser.add_argument('inpt', type=str, help="Input folder")
    parser.add_argument('outpt', type=str, help="Output folder")
    parser.add_argument('dtype', type=str, help="Numpy datatype \
                                                            (np.int16, np.uint16, np.float32,\
                                                            np.float64).")
    parser.add_argument('-gz', '--gzip', help="gzip file", action='store_false')

    args = parser.parse_args()

    in_folder = args.inpt
    out_folder = args.outpt


    dtype=""

    if args.dtype == "np.int16":
        dtype = np.int16
    elif args.dtype == "np.ushort":
        dtype = np.ushort
    elif args.dtype == "np.uint16":
        dtype = np.uint16
    elif args.dtype == "np.float32":
        dtype = np.float32
    else:
        dtype = np.float64 
    
    gzip = args.gzip
    
    convert2nifti(in_folder, out_folder, dtype, gzip)
