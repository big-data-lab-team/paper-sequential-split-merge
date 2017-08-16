#!/usr/bin/env gnuplot

set terminal pdf color font ',13'
set border 3 front lt black linewidth 1.000 dashtype solid
set boxwidth 0.75 absolute
set style fill solid 1.00 border lt -1
set style histogram rowstacked
set style data histograms
set xlabel "Memory (GB)"
set ylabel "Merging time (s)"

maxy=13500

############# MERGE #################

## HDD
set output "./figures/benchmark-mreads/mreads-breakdown-hdd.pdf"
plot [][0:maxy] \
     './data/mreads/mreads_hdd_avg_var.dat' using ($2):xtic(1) lt 2 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 2 fs solid 0.5 t "Read" , \
      '' using ($4) lt 2 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-creads/creads-breakdown-hdd.pdf"
plot [][0:maxy] \
     './data/creads/creads_hdd_avg_var.dat' using ($2):xtic(1) lt 1 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 1 fs solid 0.5 t "Read" , \
      '' using ($4) lt 1 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-buff-slices/buff-slices-reads-breakdown-hdd.pdf"
plot [][0:maxy] \
     './data/buff-slices/buff-slices_reads_hdd_avg_var.dat' using ($2):xtic(1) lt 5 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 5 fs solid 0.5 t "Read" , \
      '' using ($4) lt 5 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

## SSD
set output "./figures/benchmark-mreads/mreads-breakdown-ssd.pdf"
plot [][0:maxy] \
     './data/mreads/mreads_ssd_avg_var.dat' using ($2):xtic(1) lt 2 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 2 fs solid 0.5 t "Read" , \
      '' using ($4) lt 2 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-creads/creads-breakdown-ssd.pdf"
plot [][0:maxy] \
     './data/creads/creads_ssd_avg_var.dat' using ($2):xtic(1) lt 1 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 1 fs solid 0.5 t "Read" , \
      '' using ($4) lt 1 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-buff-slices/buff-slices-reads-breakdown-ssd.pdf"
plot [][0:maxy] \
     './data/buff-slices/buff-slices_reads_ssd_avg_var.dat' using ($2):xtic(1) lt 5 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 5 fs solid 0.5 t "Read" , \
      '' using ($4) lt 5 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1


############# SPLIT #################

maxy=4000
## HDD
set output "./figures/benchmark-mwrites/mwrites-breakdown-hdd.pdf"
plot [][0:maxy] \
     './data/mwrites/mwrites_hdd_avg_var.dat' using ($2):xtic(1) lt 2 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 2 fs solid 0.5 t "Read" , \
      '' using ($4) lt 2 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-cwrites/cwrites-breakdown-hdd.pdf"
plot [][0:maxy] \
     './data/cwrites/cwrites_hdd_avg_var.dat' using ($2):xtic(1) lt 1 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 1 fs solid 0.5 t "Read" , \
      '' using ($4) lt 1 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-buff-slices/buff-slices-writes-breakdown-hdd.pdf"
plot [][0:maxy] \
     './data/buff-slices/buff-slices_writes_hdd_avg_var.dat' using ($2):xtic(1) lt 5 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 5 fs solid 0.5 t "Read" , \
      '' using ($4) lt 5 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

## SSD
set output "./figures/benchmark-mwrites/mwrites-breakdown-ssd.pdf"
plot [][0:maxy] \
     './data/mwrites/mwrites_ssd_avg_var.dat' using ($2):xtic(1) lt 2 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 2 fs solid 0.5 t "Read" , \
      '' using ($4) lt 2 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-cwrites/cwrites-breakdown-ssd.pdf"
plot [][0:maxy] \
     './data/cwrites/cwrites_ssd_avg_var.dat' using ($2):xtic(1) lt 1 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 1 fs solid 0.5 t "Read" , \
      '' using ($4) lt 1 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1

set output "./figures/benchmark-buff-slices/buff-slices-writes-breakdown-ssd.pdf"
plot [][0:maxy] \
     './data/buff-slices/buff-slices_writes_ssd_avg_var.dat' using ($2):xtic(1) lt 5 fs solid 0.25 t "Overhead" , \
     '' using ($3) lt 5 fs solid 0.5 t "Read" , \
      '' using ($4) lt 5 fs solid 0.75 t "Write",\
      '' using ($5) lt 7 fs solid 1.0 t "Seek",\
      '' using 0:($2+$3+$4+$5):6 with errorbars notitle lw 2 lt -1
