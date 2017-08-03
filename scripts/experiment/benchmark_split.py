#!/usr/bin/env python
# Ref: imageutils.py from
# https://github.com/big-data-lab-team/mapreduce/blob/master/python/imageutils.py
import imageutils as img_utils
import numpy as np
from time import time
import argparse
import random
import os

# example
# ./benchmark_mwrites.py -m 3221225472 9663676416 6442450944 13043807040 -r 5 -d ssd
# ./benchmark_mwrites.py -m 3221225472 9663676416 6442450944 13043807040 -r 5 -d hdd


# on the consider
ori_image_hdd = "/data/bigbrain_40microns.nii"
out_dir_hdd = "/data/gao/blocks_split"

ori_image_ssd = "/home/gao/reconstructed.nii"
out_dir_ssd = "/home/gao/blocks125"

csv_file_hdd = "./hdd_mwrites.csv"
csv_file_ssd = "./ssd_mwrites.csv"


Y_splits=5
Z_splits=5
X_splits=5

files = {
    "hdd": (ori_image_hdd, out_dir_hdd, csv_file_hdd),
    "ssd": (ori_image_ssd, out_dir_ssd, csv_file_ssd)
}

def benchmark_mwrites(mem, ori_image, out_dir):
    img = img_utils.ImageUtils(ori_image)
    s_time = time()
    total_read_time, total_write_time, total_seek_time, total_seek_number = img.split_multiple_writes(Y_splits, Z_splits, X_splits, out_dir, mem, filename_prefix="bigbrain",
                          extension="nii", benchmark=True)
    total_time = time() - s_time
    print "mem = {}, takes {}".format(mem, total_time)

    return (total_read_time, total_write_time, total_seek_time, total_seek_number, total_time)

def write_to_csv(data_dict, csv_file):
    with open(csv_file, "a") as f:
        for k in sorted(data_dict.keys()):
            for e in data_dict[k]:
                f.write(str(e) + ",")
        f.write("\n")


def main():
    parser = argparse.ArgumentParser(description='Split - Bechmark for mulitiple writes')
    parser.add_argument('-m', '--mem', nargs='+', type=int, help="mem in bytes. A list of mems is required", required=True)
    parser.add_argument('-r', '--rep', type=int, help="how many repetitions on each mem", required=True)
    parser.add_argument('-d', '--disk', choices=['ssd', 'hdd'], help="running on hdd or ssd", required=True)
    args = parser.parse_args()

    mem_list = args.mem
    rep = args.rep
    disk = args.disk

    for i in range(0, rep):
        data_dict = {}
        print "Repetition: {}".format(i)
        random.shuffle(mem_list)
        for mem in mem_list:
            print "mem = {}".format(mem)
            os.system("echo 3 | sudo tee /proc/sys/vm/drop_caches")
            os.system("rm -rf {}/*".format(files[disk][1]))
            data = benchmark_mwrites(mem=mem, ori_image=files[disk][0], out_dir=files[disk][1])
            data_dict[mem] = data
        write_to_csv(data_dict, files[disk][2])

if __name__ == '__main__':
    main()
