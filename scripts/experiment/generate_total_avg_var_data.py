#!/usr/bin/env python
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

# merge
#ssd
input_file_mreads_ssd = "./data/mreads/mreads_ssd.dat"
input_file_creads_ssd = "./data/creads/creads_ssd.dat"
input_file_buff_slices_ssd = "./data/buff-slices/buff-slices_ssd.dat"

#hdd
input_file_mreads_hdd = "./data/mreads/mreads_hdd.dat"
input_file_creads_hdd = "./data/creads/creads_hdd.dat"
input_file_buff_slices_hdd = "./data/buff-slices/buff-slices_hdd.dat"

# split
#ssd
input_file_mwrites_ssd = "./data/mwrites/mwrites_ssd.dat"
input_file_cwrites_ssd = "./data/cwrites/cwrites_ssd.dat"
input_file_buff_slices_split_ssd = "./data/buff-slices/buff-slices_split_ssd.dat"

#hdd
input_file_mwrites_hdd = "./data/mwrites/mwrites_hdd.dat"
input_file_cwrites_hdd = "./data/cwrites/cwrites_hdd.dat"
input_file_buff_slices_split_hdd = "./data/buff-slices/buff-slices_split_hdd.dat"





def generate(input_file_mreads, input_file_creads, input_file_buff_slices, output_file):
    total_time_06g, total_time_3g, total_time_6g, total_time_9g, total_time_12g, total_time_16g = [], [], [], [], [], []

    with open(input_file_creads, 'r') as f:
        for line in f:
            if '#' not in line:
                items = line.split(' ')
                # 0.6g - naive blocks
                total_time_06g.append(float(items[4]))
                # 3g - cr
                total_time_3g.append(float(items[9]))
                # 6g - cr
                total_time_6g.append(float(items[14]))
                # 9g - cr
                total_time_9g.append(float(items[19]))
                # 12g - cr
                total_time_12g.append(float(items[24]))
                # 16g - cr
                total_time_16g.append(float(items[29]))

        nb_total = [avg(total_time_06g), 0,0,0,0,0]
        nb_total_err = [var(total_time_06g), 0,0,0,0,0]
        cr_total = [0, avg(total_time_3g), avg(total_time_6g), avg(total_time_9g), avg(total_time_12g), avg(total_time_16g)]
        cr_total_err = [0, var(total_time_3g), var(total_time_6g), var(total_time_9g), var(total_time_12g), var(total_time_16g)]

    total_time_06g, total_time_3g, total_time_6g, total_time_9g, total_time_12g, total_time_16g = [], [], [], [], [], []
    with open(input_file_mreads, 'r') as f:
        for line in f:
            if '#' not in line:
                items = line.split(' ')
                # 3g - mr
                total_time_3g.append(float(items[4]))
                # 6g - mr
                total_time_6g.append(float(items[9]))
                # 9g - mr
                total_time_9g.append(float(items[14]))
                # 12g - mr
                total_time_12g.append(float(items[19]))
                # 16g - mr
                total_time_16g.append(float(items[24]))

        mr_total = [0, avg(total_time_3g), avg(total_time_6g), avg(total_time_9g), avg(total_time_12g), avg(total_time_16g)]
        mr_total_err = [0, var(total_time_3g), var(total_time_6g), var(total_time_9g), var(total_time_12g), var(total_time_16g)]

    total_time_06g, total_time_3g, total_time_6g, total_time_9g, total_time_12g, total_time_16g = [], [], [], [], [], []
    with open(input_file_buff_slices, 'r') as f:
        for line in f:
            if '#' not in line:
                items = line.split(' ')
                # 0.6g - naive slices
                total_time_06g.append(float(items[4]))
                # 3g - bs
                total_time_3g.append(float(items[9]))
                # 6g - bs
                total_time_6g.append(float(items[14]))
                # 9g - bs
                total_time_9g.append(float(items[19]))
                # 12g - bs
                total_time_12g.append(float(items[24]))

        ns_total = [avg(total_time_06g), 0, 0, 0, 0, 0]
        ns_total_err = [var(total_time_06g), 0, 0, 0, 0, 0]
        bs_total = [0, avg(total_time_3g), avg(total_time_6g), avg(total_time_9g), avg(total_time_12g), 0]
        bs_total_err = [0, var(total_time_3g), var(total_time_6g), var(total_time_9g), var(total_time_12g), 0]

    mem = ["0.6", "3", "6", "9", "12", "16"]
    with open(output_file, 'w+') as f:
        f.write("mem \"Naive blocks\" NBR \"Naive slices\" NSR \"Cluster reads\" CRR \"Multiple reads\" MRR \"Buffered slices \" BSR")
        f.write('\n')
        for i in range(0,6):
            f.write(
                "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}"
                .format(mem[i], nb_total[i], nb_total_err[i], ns_total[i], ns_total_err[i], cr_total[i], cr_total_err[i]
                            ,mr_total[i], mr_total_err[i], bs_total[i], bs_total_err[i]))
            f.write('\n')

def main():
    output_file = "./data/total-merge-time-ssd.dat"
    generate(input_file_mreads_ssd, input_file_creads_ssd, input_file_buff_slices_ssd, output_file=output_file)
    output_file = "./data/total-merge-time-hdd.dat"
    generate(input_file_mreads_hdd, input_file_creads_hdd, input_file_buff_slices_hdd, output_file=output_file)
    output_file = "./data/total-split-time-ssd.dat"
    # generate(input_file_mwrites_ssd, input_file_cwrites_ssd, input_file_buff_slices_split_ssd, output_file=output_file)
    output_file = "./data/total-split-time-hdd.dat"
    # generate(input_file_mwrites_hdd, input_file_cwrites_hdd, input_file_buff_slices_split_hdd, output_file=output_file)
if __name__ == '__main__':
    main()
