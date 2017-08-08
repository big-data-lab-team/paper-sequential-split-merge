#!/usr/bin/env python

input_file_mreads_ssd = "./data/mreads/mreads_ssd.dat"
output_file_mreads_ssd = "./data/mreads/mreads_ssd_avg_var.dat"
input_file_mreads_hdd = "./data/mreads/mreads_hdd.dat"
output_file_mreads_hdd = "./data/mreads/mreads_hdd_avg_var.dat"

input_file_creads_ssd = "./data/creads/creads_ssd.dat"
output_file_creads_ssd = "./data/creads/creads_ssd_avg_var.dat"
input_file_creads_hdd = "./data/creads/creads_hdd.dat"
output_file_creads_hdd = "./data/creads/creads_hdd_avg_var.dat"

input_file_buff_slices_ssd = "./data/buff-slices/buff-slices_ssd.dat"
output_file_buff_slices_ssd = "./data/buff-slices/buff-slices_ssd_avg_var.dat"
input_file_buff_slices_hdd = "./data/buff-slices/buff-slices_hdd.dat"
output_file_buff_slices_hdd = "./data/buff-slices/buff-slices_hdd_avg_var.dat"


def avg(l):
    if len(l) == 0:
        return 0
    return sum(l) / float(len(l))
    
def var(l):
    if len(l) == 0:
        return 0
    s1 = 0
    s2 = 0
    for i in l:
        s1 += i ** 2
        s2 += i
    return (float(s1) / len(l) - (float(s2) / len(l)) ** 2) ** 0.5

def get_avg_var_naive(input_file, output_file, input_file_naive_blocks, input_file_naive_slices, hasnaive, disk):
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

    read_times_16g = []
    write_times_16g = []
    seek_times_16g = []
    calculation_times_16g = []
    total_time_16g = []
    
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

    offset=0
    if hasnaive:
        offset=5
        
    with open(input_file, 'r') as f:
        for line in f:
            if '#' not in line:
                items = line.split(' ')
                # 3g
                read_time = float(items[offset+0])
                write_time = float(items[offset+1])
                seek_time = float(items[offset+2])
                total_time = float(items[offset+4])
                calculation_time = total_time - seek_time - write_time - read_time
                read_times_3g.append(read_time)
                write_times_3g.append(write_time)
                seek_times_3g.append(seek_time)
                calculation_times_3g.append(calculation_time)
                total_time_3g.append(total_time)
                # 6g
                read_time = float(items[offset+5])
                write_time = float(items[offset+6])
                seek_time = float(items[offset+7])
                total_time = float(items[offset+9])
                calculation_time = total_time - seek_time - write_time - read_time
                read_times_6g.append(read_time)
                write_times_6g.append(write_time)
                seek_times_6g.append(seek_time)
                calculation_times_6g.append(calculation_time)
                total_time_6g.append(total_time)
                # 9g
                read_time = float(items[offset+10])
                write_time = float(items[offset+11])
                seek_time = float(items[offset+12])
                total_time = float(items[offset+14])
                calculation_time = total_time - seek_time - write_time - read_time
                read_times_9g.append(read_time)
                write_times_9g.append(write_time)
                seek_times_9g.append(seek_time)
                calculation_times_9g.append(calculation_time)
                total_time_9g.append(total_time)
                # 12g
                read_time = float(items[offset+15])
                write_time = float(items[offset+16])
                seek_time = float(items[offset+17])
                total_time = float(items[offset+19])
                calculation_time = total_time - seek_time - write_time - read_time
                read_times_12g.append(read_time)
                write_times_12g.append(write_time)
                seek_times_12g.append(seek_time)
                calculation_times_12g.append(calculation_time)
                total_time_12g.append(total_time)
                # 16g
                read_time = float(items[offset+20])
                write_time = float(items[offset+21])
                seek_time = float(items[offset+22])
                total_time = float(items[offset+24])
                calculation_time = total_time - seek_time - write_time - read_time
                read_times_16g.append(read_time)
                write_times_16g.append(write_time)
                seek_times_16g.append(seek_time)
                calculation_times_16g.append(calculation_time)
                total_time_16g.append(total_time)

    # open naive block file:
    with open(input_file_naive_blocks, 'r') as f:
            for line in f:
                if '#' not in line:
                    items = line.split(' ')
                    # naive blocks hdd
                    read_time = float(items[0])
                    write_time = float(items[1])
                    seek_time = float(items[2])
                    total_time = float(items[4])
                    calculation_time = total_time - seek_time - write_time - read_time
                    read_times_blocks.append(read_time)
                    write_times_blocks.append(write_time)
                    seek_times_blocks.append(seek_time)
                    calculation_times_blocks.append(calculation_time)
                    total_time_blocks.append(total_time)

        # open naive slice  file:
    with open(input_file_naive_slices, 'r') as f:
            for line in f:
                if '#' not in line:
                    items = line.split(' ')
                    # naive slices hdd
                    read_time = float(items[0])
                    write_time = float(items[1])
                    seek_time = float(items[2])
                    total_time = float(items[4])
                    calculation_time = total_time - seek_time - write_time - read_time
                    read_times_slices.append(read_time)
                    write_times_slices.append(write_time)
                    seek_times_slices.append(seek_time)
                    calculation_times_slices.append(calculation_time)
                    total_time_slices.append(total_time)
                    
    with open(output_file, 'w') as f:
        f.write("#time calculation_time read_time write_time seek_time total_time_error")
        f.write('\n')
        f.write("naive-block {} {} {} {} {}".format(avg(calculation_times_blocks), avg(read_times_blocks),
                                                    avg(write_times_blocks),
                                                    avg(seek_times_blocks), var(total_time_blocks)))
        f.write('\n')
        f.write("3 {} {} {} {} {} ".format(avg(calculation_times_3g), avg(read_times_3g), avg(write_times_3g),
                                            avg(seek_times_3g), var(total_time_3g)))
        f.write('\n')
        f.write("6 {} {} {} {} {} ".format(avg(calculation_times_6g), avg(read_times_6g), avg(write_times_6g),
                                            avg(seek_times_6g), var(total_time_6g)))
        f.write('\n')
        f.write("9 {} {} {} {} {} ".format(avg(calculation_times_9g), avg(read_times_9g), avg(write_times_9g),
                                            avg(seek_times_9g), var(total_time_9g)))
        f.write('\n')
        f.write("12 {} {} {} {} {} ".format(avg(calculation_times_12g), avg(read_times_12g), avg(write_times_12g),
                                             avg(seek_times_12g), var(total_time_12g)))
        f.write('\n')
        f.write("16 {} {} {} {} {} ".format(avg(calculation_times_16g), avg(read_times_16g), avg(write_times_16g),
                                             avg(seek_times_16g), var(total_time_16g)))
        f.write('\n')
        f.write("naive-slice {} {} {} {} {}".format(avg(calculation_times_slices), avg(read_times_slices),
                                                    avg(write_times_slices),
                                                    avg(seek_times_slices), var(total_time_slices)))

def main():
    # mreads
    get_avg_var_naive(input_file_mreads_ssd, output_file_mreads_ssd, input_file_creads_ssd, input_file_buff_slices_ssd, hasnaive=False, disk="ssd")
    get_avg_var_naive(input_file_mreads_hdd, output_file_mreads_hdd, input_file_creads_hdd, input_file_buff_slices_hdd, hasnaive=False, disk="hdd")
    # creads
    get_avg_var_naive(input_file_creads_ssd, output_file_creads_ssd, input_file_creads_ssd, input_file_buff_slices_ssd, hasnaive=True, disk="ssd")
    get_avg_var_naive(input_file_creads_hdd, output_file_creads_hdd, input_file_creads_hdd, input_file_buff_slices_hdd, hasnaive=True, disk="hdd")
    # buffered slicse
    get_avg_var_naive(input_file_buff_slices_ssd, output_file_buff_slices_ssd, input_file_creads_ssd, input_file_buff_slices_ssd, hasnaive=True, disk="ssd")
    get_avg_var_naive(input_file_buff_slices_hdd, output_file_buff_slices_hdd, input_file_creads_hdd, input_file_buff_slices_hdd, hasnaive=True, disk="hdd")

if __name__ == '__main__':
    main()
