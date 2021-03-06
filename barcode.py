#!/usr/bin/python3
# coding: utf-8

import os
import luhn # sudo apt install python3-pip && sudo pip3 install luhn

# Deutsche Post DHL hat einfach an Packstationen den Kartenleser
# ausgebaut und duch einen Barcodeleser ersetzt, ohne den
# Besitzern einer Goldcard automatisch rechtzeitig eine neue
# Karte zuzuschicken. Man kann aber weiterhin an solchen Stationen
# Pakete abholen, nur muss man jetzt die PostNummer manuell eintippen.
# Mit diesem Skript generieren wir uns den entsprechenden Barcode, da das
# Zusenden einer neuen Karte bei DHL beauftragt werden muss, die alte Karte
# in der Zwischenzeit sofort gesperrt wird und die neue bis zu 2 Wochen
# dauern kann. Das ist maximal kundenunfreundlich.
# Sicherheitstechnisch liegt kein Verstoß vor, da man durch Eintippen
# der PostNummer sowieso Pakete abholen kann und die Umrechnung von
# PostNummer zu Barcode im Netz bereits vielfach beschrieben ist.
# Der 16-stellige ITF-Barcode ist relativ einfach aufgebaut:
# "3”+”[so viele ‘0’, dass die Zahl insgesamt 16 Stellen hat]”
# +”[Postnummer*631]”+”[Luhn-Prüfziffer über ‘Postnummer*631’]"
# http://www.frei-tag.com/index.php?/archives/445-DHL-Packstation-ohne-Goldcard.html

def generate(number):
	postnummer = int(number)

	number = postnummer*631
	luhnnr = luhn.generate(str(number))
	number = "3" + (str(number)+str(luhnnr)).zfill(15)

	return(str(number))

# Beispiel anhand einer zufallsgenerierten Zahl:
# 20281557 ergibt 3000127976624677
assert generate("20281557") == "3000127976624677"

# Interleaved 2 of 5 ITF barcode
os.system("xdg-open https://barcode.tec-it.com/de/Code25IL?data=" + generate(20281557))
