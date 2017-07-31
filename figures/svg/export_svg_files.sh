#!/usr/bin/env bash

for name in buffer case1-a case2-a case3 incomplete-rows overlap mreads-case1 \
        mreads-case2 mreads-case3 mreads-case4 mreads-case5
do
  #echo "Exporting ${name}.svg"
  inkscape -D -z --file=figures/svg/${name}.svg --export-pdf=figures/svg/${name}.pdf --export-latex
  sed s,${name}\.pdf,figures/svg/${name}\.pdf,g figures/svg/${name}.pdf_tex > figures/svg/${name}.pdf_tex.new
  \mv figures/svg/${name}.pdf_tex.new figures/svg/${name}.pdf_tex
done
