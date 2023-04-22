# packstation-barcode

__Update 2023:
Die Nutzung der Packtstation erfordert nun zwingend die Verwendung einer proprietären Closed Source App, die (offiziell) nur über den Google Play Store erhältlich ist, was die Zustimmung zu den Datenschutzbedingungen von Google (USA, Einflussbereich der NSA) erfordert, und zudem Tracker (u.a. Adobe Marketing Cloud in den USA) einsetzt:__

__https://reports.exodus-privacy.eu.org/de/reports/de.dhl.paket/latest/__

__Daher ist die Packtstation unbenutzbar geworden für Personen, die Closed Source Apps und Cloud Services im Einflussbereich der NSA ablehnen.__

Das Mindeste wäre, dass die Post die Packstation App Open Source macht und auf https://f-droid.org/ veöffentlicht.

Erstellung von Barcodes für DHL Goldcard

Deutsche Post DHL hat einfach an Packstationen den Kartenleser
ausgebaut und duch einen Barcodeleser ersetzt, ohne den
Besitzern einer mit Magnetstreifen ausgestatteten Goldcard 
automatisch rechtzeitig eine neue Karte mit Barcode zuzuschicken.__ 

Man kann aber weiterhin an solchen Stationen
Pakete abholen, nur muss man jetzt die PostNummer manuell eintippen.

Das Zusenden einer neuen Karte muss bei DHL beauftragt werden, was
aber mit großen Umständen verbunden ist, da die alte Karte
in der Zwischenzeit sofort gesperrt wird und die Zusendung der neuen
bis zu 2 Wochen dauern kann. Das ist maximal kundenunfreundlich.

Mit diesem Skript generieren wir uns den entsprechenden Barcode.

Sicherheitstechnisch liegt kein Verstoß vor, da man durch Eintippen
der PostNummer sowieso Pakete abholen kann und die Umrechnung von
PostNummer zu Barcode im Netz bereits vielfach beschrieben ist.

Der 16-stellige ITF-Barcode ist relativ einfach aufgebaut:

```
"3”+”[so viele ‘0’, dass die Zahl insgesamt 16 Stellen hat]”
+”[Postnummer*631]”+”[Luhn-Prüfziffer über ‘Postnummer*631’]"
http://www.frei-tag.com/index.php?/archives/445-DHL-Packstation-ohne-Goldcard.html
```

Wie an anderer Stelle schon berichtet, ist mit diesem Barcode
das __Versenden__ möglich. Das beweist, dass der Barcode richtig ist
und an sich funktioniert.

__NICHT__ möglich ist aber das __Abholen__.
Versucht man das, kommt die Meldung

> Die Anmeldung mit dieser PostNummer ist nicht möglich!
> 
> Bitte wenden Sie sich per E-Mail an paket@dhl.de

Vielleicht funktioniert das Abholen nur mit solchen Barcodes,
die zu Goldcards gehören, die ab Werk mit dem Barcode kamen.

Das ist maximal kundenunfreundlich und dient wie oben dargestellt __NICHT__
dazu, die Sicherheit zu erhöhen. Denn: Wenn man die zu dem Barcode
gehörende PostNummer von Hand eintippt, kann man ohne Probleme mit
dieser PostNummer abholen. Gerade getestet.
