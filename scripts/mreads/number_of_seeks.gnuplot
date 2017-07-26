set terminal pdfcairo color
set border 3 front lt black linewidth 1.000 dashtype solid
set boxwidth 0.5 absolute
set style fill solid 0.50 border lt -1
unset key
set pointsize 0.5

set style data boxplot
set xtics border in scale 0,0 nomirror norotate  autojustify
set xtics  norangelimit
set datafile separator ","



set xtics ("3g-hdd" 1, "3g-ssd" 2, "9g-hdd" 3, "9g-ssd" 4)
unset format y
unset ydata
unset xrange
unset logscale x
unset format x
set boxwidth 0.5
set xlabel "Merging strategy - Multiple Reads: Number of seeks on HDD and SSD"
set ylabel "Number of seeks"
set output "../../../figures/benchmark-mreads/number_of_seeks.pdf"
plot '../../../data/benchmark/mreads/hdd.csv' using (1):4, '' using (3):9, '../../../data/benchmark/mreads/ssd.csv' using (2):4, '' using (4):9



