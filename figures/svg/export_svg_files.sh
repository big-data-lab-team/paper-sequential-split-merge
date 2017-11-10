#!/usr/bin/env bash

for name in buffer case1-a case2-a case3 incomplete-columns overlap mreads-case1 \
        mreads-case2 mreads-case3 mreads-case4 mreads-case5 Notations
do
  #echo "Exporting ${name}.svg"
  inkscape -D -z --file=$PWD/figures/svg/${name}.svg --export-pdf=$PWD/figures/svg/${name}.pdf --export-latex
  sed s,${name}\.pdf,$PWD/figures/svg/${name}\.pdf,g $PWD/figures/svg/${name}.pdf_tex > $PWD/figures/svg/${name}.pdf_tex.new
  \mv $PWD/figures/svg/${name}.pdf_tex.new $PWD/figures/svg/${name}.pdf_tex
done
