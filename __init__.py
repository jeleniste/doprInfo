# -*- coding: utf-8 -*-
"""
/***************************************************************************
 doprInfo
                                 A QGIS plugin
 Načte aktuální dopravní informace
                             -------------------
        begin                : 2017-09-15
        copyright            : (C) 2017 by Jelen
        email                : jelen@opengeolabs.cz
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load doprInfo class from file doprInfo.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .doprInfo import doprInfo
    return doprInfo(iface)
