# doprInfo

Plugin do Qgis, který slouží k načtení a zobrazení aktuálních [informací o dopravě](http://aplikace.policie.cz/dopravni-informace/)

Začátek a konec dopravního omezení je vyznačen pomocí multipointu. 

Kromě geometrie jsou načteny popisné informace (textový popis, popis lokality), [kódy
TMC událostí](http://wiki.openstreetmap.org/wiki/TMC/Event_Code_List).

Pluginem je možné načítat uložené soubory, případně načíst data přímo přes sít.
Taktéž je možné aktualizovat existující vrstvu.  

## Instalace

Plugin stáhněte přímo do adresáře s pluginy QGIS.

Linux:

```
cd ~/.qgis2/python/plugins
git clone https://github.com/jeleniste/doprInfo.git
```

Windows:

```
cd C:\Documents and Settings\(user)\.qgis2\python\plugins\
git clone https://github.com/jeleniste/doprInfo.git
```

Pokud nemáte `git` a nic vám to neříkám, prostě stáhněte [ZIP archiv
projektu](https://github.com/jeleniste/doprInfo/archive/master.zip) a rozbalte
do zmíněných adresářů.

Zásuvný modul musíte ještě povolit ve správci pluginů v QGISu v menu `Zásuvné
moduly -> Spravovat a instalovat zásuvné moduly` a v dialogu najít `Dopravni
info` a povolit, viz obrázek:

![povolit plugin](https://raw.githubusercontent.com/jeleniste/doprInfo/master/screenshots/dopravni-info-plugin.png)

## Závislosti
K fungování je třeba mít v pythonu2 nainstalovaný modul `lxml`. Na windows je
třeba lxml doinstalovat. Postup je stejný jako jako u projektu `islh_parser` [Instalace
lxml na windows](https://github.com/jeleniste/islh_parser/wiki/Instalace#instalace-na-windows)


## Screenshoty

![plugin](https://raw.githubusercontent.com/jeleniste/doprInfo/master/screenshots/doprinfo1.png)

Hlavní podoba dat v QGISu

![nahrané body na podlkladové mapě google roads](https://raw.githubusercontent.com/jeleniste/doprInfo/master/screenshots/2017-09-16-143718_1438x878_scrot.png)

Nahrané body na podkladové mapě Google Roads

![načtené atributy](https://github.com/jeleniste/doprInfo/blob/master/screenshots/2017-09-16-143803_1438x878_scrot.png)

Tabulka atributů

![popisky](https://github.com/jeleniste/doprInfo/blob/master/screenshots/2017-09-16-143910_1438x878_scrot.png)

Popisky v mapě

![dialog načtení](https://github.com/jeleniste/doprInfo/blob/master/screenshots/2017-09-16-143727_312x120_scrot.png)

Dialog načtení dat ze souboru/ze sítě

![dialog načtení](https://github.com/jeleniste/doprInfo/blob/master/screenshots/osm_scrot.png)

OpenStreetMaps jako podkladová mapa
