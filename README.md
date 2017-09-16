# doprInfo
![plugin](https://raw.githubusercontent.com/jeleniste/doprInfo/master/screenshots/doprinfo1.png)
Plugin do Qgis, který slouží k načtení a zobrazení aktuálních [informací o
dopravě](http://aplikace.policie.cz/dopravni-informace/)
Začátek a konec dopravního omezení je vyznačen pomocí multipointu. 
![nahrané body na podlkladové mapě google roads](https://raw.githubusercontent.com/jeleniste/doprInfo/master/screenshots/2017-09-16-143718_1438x878_scrot.png)
Kromě geometrie jsou načteny popisné informace (textový popis, popis lokality), [kódy
TMC událostí](http://wiki.openstreetmap.org/wiki/TMC/Event_Code_List).
![načtené atributy](https://github.com/jeleniste/doprInfo/blob/master/screenshots/2017-09-16-143803_1438x878_scrot.png)
![popisky](https://github.com/jeleniste/doprInfo/blob/master/screenshots/2017-09-16-143910_1438x878_scrot.png)

Pluginem je možné načítat uložené soubory, případně načíst data přímo přes sít.
Taktéž je možné aktualizovat existující vrstvu.  
![dialog načtení](https://github.com/jeleniste/doprInfo/blob/master/screenshots/2017-09-16-143727_312x120_scrot.png)



## Závislosti
K fungování je třeba mít v pythonu2 nainstalovaný modul lxml. Na windows je třeba lxml doinstalovat. Postup je stejný jako jako u islh_parser 
[Instalace lxml na windows](https://github.com/jeleniste/islh_parser/wiki/Instalace)

