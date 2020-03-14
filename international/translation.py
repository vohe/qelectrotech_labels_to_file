#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from xml.etree import ElementTree

xmlconst = """
            <index>
                <main str="Folder to display">
                   <locale lang="de">Anzuzeigender ordner</locale>
                   <locale lang="en">Folder to display</locale>
                   <locale lang="fr">Dossier à afficher</locale>
                 </main>
                  <main str="save">
                     <locale lang="de">sichern</locale>
                     <locale lang="en">save</locale>
                 </main>
            </index>
            """


class translate:
    def __init__(self, xmlstring, locale='de', path=' '):
        self.xmlstring = xmlstring
        self.locale = locale
        self.filepath = ' '
        if os.path.exists(path):
            self.filepath = path

    def set_locale(self, locale):
        self.locale = locale

    def late(self, astring):
        if self.filepath == ' ':
            root = ElementTree.fromstring(self.xmlstring)
        else:
            doc = ElementTree.parse(self.filepath)
            root = doc.getroot()
        # go thru all index tags
        replace = ' '
        for main in root.findall('main'):
            # match = main.get('str')
            if astring == main.get('str'):
                for l in main.findall('locale'):
                    if l.get('lang') == self.locale:
                        replace = l.text
        if replace == ' ':
            replace = astring
        return replace


def main():
    """ Main program """
    # Code goes over here.
    libraryfile = os.path.join(os.path.dirname(os.path.abspath((__file__))), 'translations.xml')
    trans = translate(xmlconst, locale='fr', path=libraryfile)
    print(trans.late('Folder to display'))
    trans.set_locale('de')
    print(trans.late('save'))
    return 0


if __name__ == "__main__":
    main()
