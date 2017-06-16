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

 

set xtics ("6g-hdd" 1, "6g-ssd" 2, "9g-hdd" 3, "9g-ssd" 4, "12g-hdd" 5, "12g-ssd" 6)
unset format y
unset ydata
unset xrange
unset logscale x
unset format x
set boxwidth 0.5
set xlabel "Merging strategy - Multiple Reads: Defragment Time on HDD and SSD"
set ylabel "Defragment Time (s)"
set output "../figures/benchmark-mreads-hdd-ssd-defrag-time.pdf"
plot '../data/data_hdd.csv' using (1):3, '' using (3):8, '' using (5):13, '../data/data_ssd.csv' using (2):3, '' using (4):8, '' using (6):13
 
