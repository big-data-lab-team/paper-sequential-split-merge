# How to get a pdf

A pdf is uploaded for every release of the paper:
* [Release 1.0](https://github.com/big-data-lab-team/paper-sequential-split-merge/files/1467700/paper.pdf) (camera-ready version for IEEE BigData 2017).
* [Release 0.1](https://github.com/big-data-lab-team/paper-sequential-split-merge/releases/download/0.1/paper.pdf) (submitted to IEEE BigData 2017).

See instructions below to create a pdf for the current version.

# How to contribute

Fork the repository, edit ```paper.tex``` and ```biblio.bib```, and make a pull-request. 

Add your name and affiliation to the list of co-authors. Contact
tristan.glatard@concordia.ca if you feel that the list or order of
authors should be amended.

# How to give feedback

* General comments: create an issue in this repository.
* Detail comments in the paper: use command ```\note``` in ```paper.tex``` as follows: ```\note{This is a comment}```.

# How to generate the pdf

0. Install ```pdflatex```, ```inkscape```, ```gnuplot``` and ```bibtex```
1. Generate the figures: ```./generate_figures.sh``` (requires ```inkscape``` and ```gnuplot```)
2. Compile the document: ```pdflatex paper ; pdflatex ``` (yes, twice).
3. Generate the bibliography: ```bibtex paper ; pdflatex paper``` (yes, once again).

# Figure sources

See https://drive.google.com/drive/folders/0BzT7pbvPDUdQRXppVlhfdS0ycGc?usp=sharing

# Latex installation

* On Linux Fedora 24: ```dnf install texlive-bin texlive-bibtex-bin texlive-minted texlive-pdfcomment texlive-collection-fontsrecommended texlive-algorithmicx texlive-framed```. 

