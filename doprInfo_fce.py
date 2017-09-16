from PyQt4.QtCore import QVariant
from lxml import etree
import urllib2
import time

from qgis.core import QgsFeatureRequest, QgsGeometry, QgsMapLayerRegistry\
        , QgsCoordinateReferenceSystem, QgsField\
        , QgsFeature, QgsPoint, QgsProject, QgsVectorLayer\
        , QgsSpatialIndex

def getDataFromFile(file):
    doc = etree.parse(file)
    #doc = etree.parse(open('/home/jelen/hackujstat/doprInfo/pitva/sample.xml', 'r'))
    #doc = etree.parse(urllib2.urlopen('http://aplikace.policie.cz/dopravni-informace/GetFile.aspx'))
    #print(doc)
    return(doc.getroot())

def getDataFromUrl():
    #doc = etree.parse(file)
    #doc = etree.parse(open('/home/jelen/hackujstat/doprInfo/pitva/sample.xml', 'r'))
    doc = etree.parse(urllib2.urlopen('http://aplikace.policie.cz/dopravni-informace/GetFile.aspx'))
    #print(doc)
    return(doc.getroot())


def createDoprInfoLayer():
    vl = QgsVectorLayer("MultiPoint?crs=epsg:4326", "dopravni_info", "memory")
    pr = vl.dataProvider()

    #add fields
    pr.addAttributes([QgsField("id", QVariant.String),
        QgsField("popis", QVariant.String),
        QgsField("popis_zkraceny", QVariant.String),
        QgsField("poloha", QVariant.String),
        QgsField("eventcode", QVariant.String),
        QgsField("main_eventcode", QVariant.Int),
        QgsField("od", QVariant.DateTime),
        QgsField("do", QVariant.DateTime)])

    vl.updateFields() # tell the vector layer to fetch changes from the provider

    QgsMapLayerRegistry.instance().addMapLayer(vl)

    return(vl)

def populateDoprInfoLayer(vl, root):
    for feature in root:
        id = feature[0].get("id")
        mloc = feature[0].find("MJD/MSG/MLOC")
        x_begin = mloc.find("SNTL/SBEG").get("x")
        x_end = mloc.find("SNTL/SEND").get("x")
        y_begin = mloc.find("SNTL/SBEG").get("y")
        y_end = mloc.find("SNTL/SEND").get("y")
        textloc = mloc.find("TXPL").text
        text = feature[0].find("MJD/MSG/MTXT").text
        text2 = feature[0].find("MJD/MSG/MEVT/OTXT").text
        eventcode = ', '.join([i.get("eventcode") for i in
            feature[0].findall("MJD/MSG/MEVT/TMCE/EVI")])
        main_eventcode = [i.get("eventcode") for i in
                feature[0].findall("MJD/MSG/MEVT/TMCE/EVI") if
                i.get("eventorder")=="1"][0]
        begin = time.strptime(feature[0].find("MJD/MSG/MTIME/TSTA").get("date") +
                " " + feature[0].find("MJD/MSG/MTIME/TSTA").get("time"),
                "%Y-%m-%d %H:%M:%S")
        end = time.strptime(feature[0].find("MJD/MSG/MTIME/TSTO").get("date") +
                " " + feature[0].find("MJD/MSG/MTIME/TSTO").get("time"),
                "%Y-%m-%d %H:%M:%S")

        # add a feature
        fet = QgsFeature()
        fet.setGeometry(QgsGeometry.fromMultiPoint([QgsPoint(float(x_begin),
            float(y_begin)), QgsPoint(float(x_end), float(y_end))]))
        fet.setAttributes([id, text, text2, textloc, eventcode, main_eventcode,
            time.strftime("%Y-%m-%d %H:%M:%S", begin), time.strftime("%Y-%m-%d %H:%M:%S"
                , end)])
        vl.dataProvider().addFeatures([fet])

    #update layer's extent when new features have been added
    #because change of extent in provider is not propagated to the layer
    vl.updateExtents()
    vl.triggerRepaint()

def updateDoprInfoLayer(vl, root):
    vl.dataProvider().deleteFeatures([feature.id() for feature in
        vl.getFeatures()])
    populateDoprInfoLayer(vl, root)

#lay = createDoprInfoLayer()
#dta = getDataFromFile(open('/home/jelen/hackujstat/doprInfo/pitva/sample.xml', 'r'))
#populateDoprInfoLayer(lay, dta)
