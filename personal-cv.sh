#!/bin/bash

rm *.pdf
rm *.html

mym=$(date +'%B')

#echo 'La variables es:'
#echo $mym

MES=$(LANG=es_ES.UTF-8; date +"%B")
MES=$(LANG=en_EN.UTF-8; date +"%B")

echo $MES

cp './cv/00_Introduction.md' './00_Introduction.md'
cp './cv/01_Professional_Experience.md' './01_Professional_Experience.md'
cp './cv/02_Education.md' './02_Education.md'
cp './cv/03_Complementary_Education.md' './03_Complementary_Education.md'
cp './cv/04_Computer_Skills.md' './04_Computer_Skills.md'
cp './cv/05_Software_Development.md' './05_Software_Development.md'
cp './cv/06_Publications.md' './06_Publications.md'
cp './cv/07_R&D_Projects.md' './07_R&D_Projects.md'
cp './cv/08_Patents.md' './08_Patents.md'
cp './cv/09_Congress.md' './09_Congress.md'
cp './cv/10_Personal.md' './10_Personal.md'

pandoc \
	      '00_Introduction.md' \
	      '01_Professional_Experience.md' \
	      '02_Education.md' \
	      '03_Complementary_Education.md' \
	      '04_Computer_Skills.md' \
	      '05_Software_Development.md' \
	      '06_Publications.md' \
	      '07_R&D_Projects.md' \
	      '08_Patents.md' \
	      '09_Congress.md' \
	      '10_Personal.md' \
	      -f markdown -t html -s -c './css/cv.css' --self-contained -o 'Ibon Martínez-Arranz CV - '$(date +%Y%m%d)'.html'
	      
pandoc \
	      '00_Introduction.md' \
	      '01_Professional_Experience.md' \
	      '02_Education.md' \
	      '03_Complementary_Education.md' \
	      '04_Computer_Skills.md' \
	      '05_Software_Development.md' \
	      '06_Publications.md' \
	      '07_R&D_Projects.md' \
	      '08_Patents.md' \
	      '09_Congress.md' \
	      '10_Personal.md' \
	      -f markdown -t epub -s -c './css/cv.css' --self-contained -o 'Ibon Martinez-Arranz CV.epub'	      

./wkhtmltox/bin/wkhtmltopdf -L 20 -R 20 -T 30 -B 30 \
	      --title 'Ibon Martínez-Arranz, CV' \
	      --footer-font-size 8 --no-footer-line --footer-spacing 10 \
	      --footer-center [fecha] \
	      --footer-right 'page [page] of [topage]' \
	      --header-font-size 8 --no-header-line --header-spacing 10 \
	      --header-right "Ibon Martínez-Arranz" \
	      --replace fecha '- '$MES' '$(date +%d)', '$(date +%Y)' -' \
	      --zoom 1 \
	      'Ibon Martínez-Arranz CV - '$(date +%Y%m%d)'.html' 'Ibon Martínez-Arranz CV - '$(date +%Y%m%d)'.pdf'
      
./wkhtmltox/bin/wkhtmltopdf -L 20 -R 20 -T 30 -B 30 \
	      --title 'Ibon Martínez-Arranz, CV' \
	      --footer-font-size 8 --no-footer-line --footer-spacing 10 \
	      --footer-center [fecha] \
	      --footer-right 'page [page] of [topage]' \
	      --header-font-size 8 --no-header-line --header-spacing 10 \
	      --header-right "Ibon Martínez-Arranz" \
	      --replace fecha '- '$MES' '$(date +%d)', '$(date +%Y)' -' \
	      --zoom 1 \
	      'Ibon Martínez-Arranz CV - '$(date +%Y%m%d)'.html' 'Ibon Martinez-Arranz CV.pdf'      

python last_five_years.py

pandoc \
	      '00_Introduction.md' \
	      '01_Professional_Experience.md' \
	      '02_Education.md' \
	      '03_Complementary_Education.md' \
	      '04_Computer_Skills.md' \
	      '05_Software_Development.md' \
	      '06_Publications_last_five_years.md' \
	      '07_R&D_Projects.md' \
	      '08_Patents.md' \
	      '09_Congress_last_five_years.md' \
	      '10_Personal.md' \
	      -f markdown -t html -s -c './css/cv.css' --self-contained -o 'Ibon Martínez-Arranz CV (5y) - '$(date +%Y%m%d)'.html'	      
-      
./wkhtmltox/bin/wkhtmltopdf -L 20 -R 20 -T 30 -B 30 \
	      --title 'Ibon Martínez-Arranz, CV' \
	      --footer-font-size 8 --no-footer-line --footer-spacing 10 \
	      --footer-center [fecha] \
	      --footer-right 'page [page] of [topage]' \
	      --header-font-size 8 --no-header-line --header-spacing 10 \
	      --header-right "Ibon Martínez-Arranz" \
	      --replace fecha '- '$MES' '$(date +%d)', '$(date +%Y)' -' \
	      --zoom 1 \
	      'Ibon Martínez-Arranz CV (5y) - '$(date +%Y%m%d)'.html' 'Ibon Martinez-Arranz CV (5y).pdf'    	      
	      
     
rm "00_Introduction.md"
rm "01_Professional_Experience.md"
rm "02_Education.md"
rm "03_Complementary_Education.md"
rm "04_Computer_Skills.md"
rm "05_Software_Development.md"
rm "06_Publications.md"
rm "06_Publications_last_five_years.md"
rm "07_R&D_Projects.md"
rm "08_Patents.md"
rm "09_Congress.md"
rm "09_Congress_last_five_years.md"
rm "10_Personal.md"


# BIOSKETCH


cp './cv/11_Biosketch.md' './11_Biosketch.md'

pandoc \
	      '11_Biosketch.md' \
	      -f markdown -t html -s -c './css/cv.css' --self-contained -o 'Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.html'

	      
mym=$(date +'%B')

#echo 'La variables es:'
#echo $mym

MES=$(LANG=es_ES.UTF-8; date +"%B")
MES=$(LANG=en_EN.UTF-8; date +"%B")

echo $MES

./wkhtmltox/bin/wkhtmltopdf -L 20 -R 20 -T 30 -B 30 \
	      --title 'Ibon Martínez-Arranz, Biosketch' \
	      --footer-font-size 8 --no-footer-line --footer-spacing 10 \
	      --footer-center [fecha] \
	      --footer-right 'page [page] of [topage]' \
	      --header-font-size 8 --no-header-line --header-spacing 10 \
	      --header-right "Ibon Martínez-Arranz" \
	      --replace fecha '- '$MES' '$(date +%d)', '$(date +%Y)' -' \
	      --zoom 1 \
	      'Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.html' 'Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.pdf'
      
#mv 'Ibon Martínez CV - '$(date +%Y%m%d)'.html' '/media/imarranz/TOSHIBA EXT/Documentos/CV/CV/cv_markdown/tex/Ibon Martínez CV - '$(date +%Y%m%d)'.html'

#pandoc -H \
#	      './tex/Ibon Martínez-Arranz Biosketch.tex' \
#	      './tex/Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.html' \
#	      -o './tex/Ibon Martínez-Arranz Biosketch - '$(date +%Y%m%d)'.pdf'
     
rm "11_Biosketch.md"

