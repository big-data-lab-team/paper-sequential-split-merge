#!/usr/bin/env python

input_file_mreads_ssd = "./data/mreads/mreads_ssd.dat"
input_file_naive_ssd = "./data/blocks-slices/totaltime.dat"
output_file_mreads_ssd = "./data/mreads/mreads_ssd_avg_var.dat"

input_file_mreads_hdd = "./data/mreads/mreads_hdd.dat"
input_file_naive_hdd = "./data/blocks-slices/totaltime.dat"
output_file_mreads_hdd = "./data/mreads/mreads_hdd_avg_var.dat"

def avg(l):
    return sum(l) / float(len(l))

def var(l):
    s1 = 0
    s2 = 0
    for i in l:
        s1 += i ** 2
        s2 += i
    return (float(s1) / len(l) - (float(s2) / len(l)) ** 2) ** 0.5

def get_avg_var_mreads_naive(input_file_mreads, input_file_naive, output_file, disk):
    read_times_3g = []
    write_times_3g = []
    seek_times_3g = []
    calculation_times_3g = []
    total_time_3g = []

    read_times_6g = []
    write_times_6g = []
    seek_times_6g = []
    calculation_times_6g = []
    total_time_6g = []

    read_times_9g = []
    write_times_9g = []
    seek_times_9g = []
    calculation_times_9g = []
    total_time_9g = []

    read_times_12g = []
    write_times_12g = []
    seek_times_12g = []
    calculation_times_12g = []
    total_time_12g = []

    read_times_slices = []
    write_times_slices = []
    seek_times_slices = []
    calculation_times_slices = []
    total_time_slices = []

    read_times_blocks = []
    write_times_blocks = []
    seek_times_blocks = []
    calculation_times_blocks = []
    total_time_blocks = []

    with open(input_file_mreads, 'r') as f:
        for line in f:
            if '#' not in line:
                items = line.split(' ')
                # 3g
                read_time = float(items[0])
                write_time = float(items[1])
                seek_time = float(items[2])
                total_time = float(items[4])
                calculation_time = total_time - seek_time - write_time - read_time
                read_times_3g.append(read_time)
                write_times_3g.append(write_time)
                seek_times_3g.append(seek_time)
                calculation_times_3g.append(calculation_time)
                total_time_3g.append(total_time)
                # 6g
                read_time = float(items[5])
                write_time = float(items[6])
                seek_time = float(items[7])
                total_time = float(items[9])
                calculation_time = total_time - seek_time - write_time - read_time
                read_times_6g.append(read_time)
                write_times_6g.append(write_time)
                seek_times_6g.append(seek_time)
                calculation_times_6g.append(calculation_time)
                total_time_6g.append(total_time)
                # 9g
                read_time = float(items[10])
                write_time = float(items[11])
                seek_time = float(items[12])
                total_time = float(items[14])
                calculation_time = total_time - seek_time - write_time - read_time
                read_times_9g.append(read_time)
                write_times_9g.append(write_time)
                seek_times_9g.append(seek_time)
                calculation_times_9g.append(calculation_time)
                total_time_9g.append(total_time)
                # 12g
                read_time = float(items[15])
                write_time = float(items[16])
                seek_time = float(items[17])
                total_time = float(items[19])
                calculation_time = total_time - seek_time - write_time - read_time
                read_times_12g.append(read_time)
                write_times_12g.append(write_time)
                seek_times_12g.append(seek_time)
                calculation_times_12g.append(calculation_time)
                total_time_12g.append(total_time)
    # open naive slice block file:
    with open(input_file_naive, 'r') as f:
        if disk == "hdd":
            for line in f:
                if '#' not in line:
                    items = line.split(' ')
                    # naive slices hdd
                    read_time = float(items[9])
                    write_time = float(items[10])
                    seek_time = 0
                    total_time = float(items[5])
                    calculation_time = total_time - seek_time - write_time - read_time
                    read_times_slices.append(read_time)
                    write_times_slices.append(write_time)
                    seek_times_slices.append(seek_time)
                    calculation_times_slices.append(calculation_time)
                    total_time_slices.append(total_time)
                    # naive blocks hdd
                    read_time = float(items[14])
                    write_time = float(items[16])
                    seek_time = float(items[15])
                    total_time = float(items[6])
                    calculation_time = total_time - seek_time - write_time - read_time
                    read_times_blocks.append(read_time)
                    write_times_blocks.append(write_time)
                    seek_times_blocks.append(seek_time)
                    calculation_times_blocks.append(calculation_time)
                    total_time_blocks.append(total_time)

        else:
            for line in f:
                if '#' not in line:
                    items = line.split(' ')
                    # naive slices ssd
                    read_time = float(items[7])
                    write_time = float(items[8])
                    seek_time = 0
                    total_time = float(items[0])
                    calculation_time = total_time - seek_time - write_time - read_time
                    read_times_slices.append(read_time)
                    write_times_slices.append(write_time)
                    seek_times_slices.append(seek_time)
                    calculation_times_slices.append(calculation_time)
                    total_time_slices.append(total_time)
                    # naive blocks ssd
                    read_time = float(items[11])
                    write_time = float(items[13])
                    seek_time = float(items[12])
                    total_time = float(items[1])
                    calculation_time = total_time - seek_time - write_time - read_time
                    read_times_blocks.append(read_time)
                    write_times_blocks.append(write_time)
                    seek_times_blocks.append(seek_time)
                    calculation_times_blocks.append(calculation_time)
                    total_time_blocks.append(total_time)

    with open(output_file, 'w') as f:
        f.write("#time calculation_time read_time write_time seek_time total_time_error")
        f.write('\n')
        f.write("naive-block {} {} {} {} {}".format(avg(calculation_times_blocks), avg(read_times_blocks),
                                                    avg(write_times_blocks),
                                                    avg(seek_times_blocks), var(total_time_blocks)))
        f.write('\n')
        f.write("3g {} {} {} {} {} ".format(avg(calculation_times_3g), avg(read_times_3g), avg(write_times_3g),
                                            avg(seek_times_3g), var(total_time_3g)))
        f.write('\n')
        f.write("6g {} {} {} {} {} ".format(avg(calculation_times_6g), avg(read_times_6g), avg(write_times_6g),
                                            avg(seek_times_6g), var(total_time_6g)))
        f.write('\n')
        f.write("9g {} {} {} {} {} ".format(avg(calculation_times_9g), avg(read_times_9g), avg(write_times_9g),
                                            avg(seek_times_9g), var(total_time_9g)))
        f.write('\n')
        f.write("12g {} {} {} {} {} ".format(avg(calculation_times_12g), avg(read_times_12g), avg(write_times_12g),
                                             avg(seek_times_12g), var(total_time_12g)))
        f.write('\n')
        f.write("naive-slice {} {} {} {} {}".format(avg(calculation_times_slices), avg(read_times_slices),
                                                    avg(write_times_slices),
                                                    avg(seek_times_slices), var(total_time_slices)))

def main():
    get_avg_var_mreads_naive(input_file_mreads_ssd, input_file_naive_ssd, output_file_mreads_ssd, disk="ssd")
    get_avg_var_mreads_naive(input_file_mreads_hdd, input_file_naive_hdd, output_file_mreads_hdd, disk="hdd")

if __name__ == '__main__':
    main()
