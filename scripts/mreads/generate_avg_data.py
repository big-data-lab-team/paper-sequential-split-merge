#!/usr/bin/env python

input_file_mreads_ssd = "./data/mreads/mreads_ssd.dat"
output_file_mreads_ssd = "./data/mreads/mreads_ssd_avg.dat"

input_file_mreads_hdd = "./data/mreads/mreads_hdd.dat"
output_file_mreads_hdd = "./data/mreads/mreads_hdd_avg.dat"

input_file_naive_ssd = "./data/blocks-slices/totaltime.dat"
output_file_naive_ssd = "./data/blocks-slices/blocks_slices_avg_ssd.dat"

input_file_naive_hdd = "./data/blocks-slices/totaltime.dat"
output_file_naive_hdd = "./data/blocks-slices/blocks_slices_avg_hdd.dat"

def avg(l):
    return sum(l) / float(len(l))

def get_avg_mreads(input_file, output_file):
    read_times_3g = []
    write_times_3g = []
    seek_times_3g = []
    calculation_times_3g = []

    read_times_6g = []
    write_times_6g = []
    seek_times_6g = []
    calculation_times_6g = []

    read_times_9g = []
    write_times_9g = []
    seek_times_9g = []
    calculation_times_9g = []

    read_times_12g = []
    write_times_12g = []
    seek_times_12g = []
    calculation_times_12g = []

    with open(input_file, 'r') as f:
        for line in f:
            if '#' not in line:
                items = line.split(' ')

                read_time = float(items[0])
                write_time = float(items[1])
                seek_time = float(items[2])
                total_time = float(items[4])
                calculation_time = total_time - seek_time - write_time - read_time

                read_times_3g.append(read_time)
                write_times_3g.append(write_time)
                seek_times_3g.append(seek_time)
                calculation_times_3g.append(calculation_time)

                read_time = float(items[5])
                write_time = float(items[6])
                seek_time = float(items[7])
                total_time = float(items[9])
                calculation_time = total_time - seek_time - write_time - read_time

                read_times_6g.append(read_time)
                write_times_6g.append(write_time)
                seek_times_6g.append(seek_time)
                calculation_times_6g.append(calculation_time)

                read_time = float(items[10])
                write_time = float(items[11])
                seek_time = float(items[12])
                total_time = float(items[14])
                calculation_time = total_time - seek_time - write_time - read_time

                read_times_9g.append(read_time)
                write_times_9g.append(write_time)
                seek_times_9g.append(seek_time)
                calculation_times_9g.append(calculation_time)

                read_time = float(items[15])
                write_time = float(items[16])
                seek_time = float(items[17])
                total_time = float(items[19])
                calculation_time = total_time - seek_time - write_time - read_time

                read_times_12g.append(read_time)
                write_times_12g.append(write_time)
                seek_times_12g.append(seek_time)
                calculation_times_12g.append(calculation_time)

    with open(output_file, 'w') as f:
        f.write("time 3g 6g 9g 12g")
        f.write('\n')
        f.write("calculation-time {} {} {} {}".format(avg(calculation_times_3g), avg(calculation_times_6g),
                                                      avg(calculation_times_9g), avg(calculation_times_12g)))
        f.write('\n')
        f.write("read-time {} {} {} {}".format(avg(read_times_3g), avg(read_times_6g),
                                               avg(read_times_9g), avg(read_times_12g)))
        f.write('\n')
        f.write("write-time {} {} {} {}".format(avg(write_times_3g), avg(write_times_6g),
                                                avg(write_times_9g), avg(write_times_12g)))
        f.write('\n')
        f.write("seek-time {} {} {} {}".format(avg(seek_times_3g), avg(seek_times_6g),
                                               avg(seek_times_9g), avg(seek_times_12g)))

def get_avg_naive(input_file, output_file):
    read_times_slices = []
    write_times_slices = []
    seek_times_slices = []
    calculation_times_slices= []

    read_times_blocks = []
    write_times_blocks = []
    seek_times_blocks = []
    calculation_times_blocks = []

    with open(input_file, 'r') as f:
        if "hdd" in output_file:
            for line in f:
                if '#' not in line:
                    items = line.split(' ')
                    read_time = float(items[9])
                    write_time = float(items[10])
                    seek_time = 0
                    total_time = float(items[5])
                    calculation_time = total_time - seek_time - write_time - read_time

                    read_times_slices.append(read_time)
                    write_times_slices.append(write_time)
                    seek_times_slices.append(seek_time)
                    calculation_times_slices.append(calculation_time)

                    read_time = float(items[14])
                    write_time = float(items[16])
                    seek_time = float(items[15])
                    total_time = float(items[6])
                    calculation_time = total_time - seek_time - write_time - read_time

                    read_times_blocks.append(read_time)
                    write_times_blocks.append(write_time)
                    seek_times_blocks.append(seek_time)
                    calculation_times_blocks.append(calculation_time)
        else:
            for line in f:
                if '#' not in line:
                    items = line.split(' ')
                    read_time = float(items[7])
                    write_time = float(items[8])
                    seek_time = 0
                    total_time = float(items[0])
                    calculation_time = total_time - seek_time - write_time - read_time

                    read_times_slices.append(read_time)
                    write_times_slices.append(write_time)
                    seek_times_slices.append(seek_time)
                    calculation_times_slices.append(calculation_time)

                    read_time = float(items[11])
                    write_time = float(items[13])
                    seek_time = float(items[12])
                    total_time = float(items[1])
                    calculation_time = total_time - seek_time - write_time - read_time

                    read_times_blocks.append(read_time)
                    write_times_blocks.append(write_time)
                    seek_times_blocks.append(seek_time)
                    calculation_times_blocks.append(calculation_time)
    with open(output_file, 'w') as f:
        f.write("time naive-slices naive-blocks")
        f.write('\n')
        f.write("calculation-time {} {}".format(avg(calculation_times_slices), avg(calculation_times_blocks)))
        f.write('\n')
        f.write("read-time {} {}".format(avg(read_times_slices), avg(read_times_blocks)))
        f.write('\n')
        f.write("write-time {} {}".format(avg(write_times_slices), avg(write_times_blocks)))
        f.write('\n')
        f.write("seek-time {} {}".format(avg(seek_times_slices), avg(seek_times_blocks)))


def main():
    get_avg_mreads(input_file_mreads_ssd, output_file_mreads_ssd)
    get_avg_mreads(input_file_mreads_hdd, output_file_mreads_hdd)
    get_avg_naive(input_file_naive_ssd, output_file_naive_ssd)
    get_avg_naive(input_file_naive_hdd, output_file_naive_hdd)
if __name__ == '__main__':
    main()
