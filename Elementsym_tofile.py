#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# a Script to change the user collection element Symbols
# for qelectrotech
# this should be a little more elegant then the first try.
# -------------
# to use this:
# in qelectrotech user elements(collection) add a folder option
#  (thats in the section of the languages for the folders)
# for me - i am german - i add a line: de - and the german folder descrition there.
# in this list add a line - like a language - with "sy" als language and the element
# description as description.

# sample: for folder /.qet/elements/fuses
# de    Sicherungen
# en    fuses
# sy    F

# this scripts look out for the sy tag and put in into the
#

__author__ = "Volker Heggemann, Melle, DE"
__copyright__ = "Copyright (C) 2020 Volker Heggemann"
__license__ = "CC BY 3.0 DE"
__version__ = "1.0"

# import the stuff we use later
import os
import sys
from sys import platform
from xml.etree import ElementTree
from xml.sax.saxutils import quoteattr as xml_quoteattr

# there a 2 versions of our GUI lib so we take the right one for our python version
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg


# letz do the main program
# a class is not nessesary yet, because this is only a tool at the moment

def main():
    """ Main program """
    # get the path with the user collection for qelectrotech
    elementspath = ''
    # in future we want to use this on all platforms (which is qelectrotech is build for)
    # platform uses different pathes and path separators
    if platform == "linux" or platform == "linux2":
        # linux platform detected
        home = os.path.expanduser('~')
        elementspath = os.path.join(home, '.qet/elements/')
        qet_directory_name = 'qet_directory'
        qet_labels_name = os.path.join(elementspath, 'qet_labels.xml')
    if platform == "darwin":
        # OS X
        # Todo how to find out the elementspath for Mac OS
        pass
    if platform == "win32":
        # Windows...
        elementspath = os.path.join(os.getenv('APPDATA'), 'qet', 'elements')
        # Todo: no extension for qet_directory in windows? is this right?
        qet_directory_name = 'qet_directory'
        qet_labels_name = os.path.join(elementspath, 'qet_labels.xml')

    # walk thru the whole elements path and look out for a qet_directory file.
    # if it there, look inside for a sy: Tag ang get value for this
    # store the value and the path inside a new xml-string which could store as
    # as a xml-file
    def make_xmlfile(path):
        # recursive function
        def dir_as_less_xml(path):
            # set the begin of the file
            result = '<category name=%s>\n' % xml_quoteattr(os.path.basename(path))
            prefix = ''
            for item in os.listdir(path):
                itempath = os.path.join(path, item)
                # if there is a (sub) dir in directory whe fist collect all subdirs in it
                if os.path.isdir(itempath):
                    result += '\n'.join('   ' + line for line in
                                        dir_as_less_xml(os.path.join(path, item)).split('\n'))
                    result += '   \n'
                # may the entry in this dir is a file?
                elif os.path.isfile(itempath):
                    # may the entry is a file called 'qet_directory'?
                    if item == qet_directory_name:
                        # get the may in this (xml-like) file stored value
                        prefix = get_symbol_for_directory(os.path.dirname(itempath))
                #     pass
                #     #result += '  <file name=%s />\n' % xml_quoteattr(item)
            # put the prefix into our xml file
            # prefix could be empty
            # in that case we go a template to edit later manually
            result += '   <prefix>' + prefix + '</prefix>\n'
            result += '</category>\n'
            return result

        # put the xml structure and tail and a header in a string
        xmltxtfile = '<?xml version="1.0" encoding="utf-8"?>\n<labels>\n' + dir_as_less_xml(path) + '\n</labels>'
        return xmltxtfile

    # save the treeviewed directroy structure in a xml.file
    def save_as_xml(path):
        # first get the xml as a string
        xml_coded_string = make_xmlfile(os.path.dirname(path))
        # debug the output ? let's print it out here : print(xml_coded_string)
        # set a filename for a existing (old) file we just add .old to it
        old = path + '.old'
        # but we only want one - the first - the original ! OLD file
        # so if a .old file is there, we don't touch it
        if not os.path.isfile(old):
            # may there is no old file and no qet_labels file
            # cause we deleted it manually?
            if os.path.exists(path):
                # but if, we rename the old file to get a place for the new file
                os.rename(path, old)
        # open a file to write
        f = open(path, "w+")
        # and now save the string into it
        f.write(xml_coded_string)
        # if we want save & exit then uncomment the following
        # exit(0)

    # we got a help button so we need to act for this
    # todo may later add a language (text)field to our main view
    # todo and show language dependent help then? i don't know
    # for the moment we use 'de-english' help
    def show_help_messagebox():
        sg.PopupOK('Kleine Hilfe - little Help for element Letter nach DIN EN 81346-2:2010 ',
                   'Bustabe\t Aufgabe\t Beispiel \n'
                   'A\t unterschiedliche Zwecke \n'
                   'B\t Umwandlung einer Eingangsgröße\t Sensoren, Messwiderstand, Grenztaster\n'
                   'C\t Speicherung von Energie\t Kondensator, Festplatte , Speicher\n'
                   'D\t Reserviert\n'
                   'E\t Bereitstellung von Wärme\t Lampen, Heizung, Heizwiderstand\n'
                   'F\t Schutz eines Signalflusses\t Sicherung, Bimetallauslöser\n'
                   'G\t Energieerzeugung\t Generator, Batterie, USV\n'
                   'H\t Reserviert\n'
                   'I\t Wegen Verwechslungsgefahr mit 1 nicht in Benutzung.\n'
                   'J\t Reserviert\n'
                   'K\t Signale verarbeiten\t Relais, Schütze, Transistor\n'
                   'L\t -\n'
                   'M\t mechanische Energie\t Motoren\n'
                   'N\t -\n'
                   'O\t Wegen Verwechslungsgefahr mit 0 nicht in Benutzung.\n'
                   'P\t Information\t Optische- und akustische Meldegeräte Signallampe, LED, Messgerät\n'
                   'Q\t Schalten eines Stromes\t Leistungstransistor, Thyristor, Softstarter, '
                   'Leistungs-/Halbleiterschütz, Lasttrenner\n'
                   'R\t Begrenzung\t Widerstand, Diode, Drossel\n'
                   'S\t Signalumwandlung\t Befehlsgeräte, Drucktaster, Schalter\n'
                   'T\t Energieumwandlung\t Ladegerät, Netzgerät, Transformator, Gleichrichter, Verstärker, Antenne,'
                   ' Messumformer, Frequenzumrichter, Spannungswandler, Stromwandler\n'
                   'U\t Halten von Objekten\n'
                   'V\t Verarbeitung von Materialien\t Elektrofilter\n'
                   'W\t Energie leiten\t  Kabel, Adern\n'
                   'X\t Verbinden von Objekten\t Klemmen, Steckdosen\n'
                   'Y\t -\n'
                   'Z\t Reserviert \n')

    # in each directory should be a qet_directory file in xml like structure
    # we parse this and look for an 'sy' entry with a value
    # and in this case we replace the value with the new_symbol text
    # if there isn't a entry for 'sy' we create a new one
    # and then we store the file back to it's location
    def set_symbol_for_directory(path, new_symbol):
        # check the path
        lookfor = os.path.join(path, qet_directory_name)
        # no changes made yet
        done = False
        # may there is no file we search for
        # then do nothing
        # it be possible to create a file ?
        if os.path.isfile(lookfor):
            # open the xml like file for our work to do
            dom = ElementTree.parse(lookfor)
            root = dom.getroot()
            # go thru all name tags and loog for the 'sy' entry
            for name in root.iter('name'):
                a = name.attrib['lang']
                # t = name.tag
                # txt = name.text
                # if found a 'sy' entry
                if a.upper() == 'SY':
                    # change the value for the symbol
                    name.text = new_symbol
                    # write our changes back to file
                    dom.write(lookfor)
                    done = True
            # found a file, but doesn't change that mean there is no 'sy' inside the file
            if not done:
                # so we create a new node in this xml file under the names tag
                sub = root.find('names')
                new_batch = ElementTree.SubElement(sub, 'name', {'lang': 'sy'})
                new_batch.text = new_symbol
                dom.write(lookfor)
                done = True
                # todo make pretty
        return done

    # we parse this and look for an 'sy' entry with a value
    # and in this case return the value or none
    def get_symbol_for_directory(path):
        symbol = 'none'
        lookfor = os.path.join(path, qet_directory_name)
        if os.path.isfile(lookfor):
            dom = ElementTree.parse(lookfor)
            root = dom.getroot()
            for name in root.iter('name'):
                a = name.attrib['lang']
                # t = name.tag
                txt = name.text
                if a.upper() == 'SY':
                    symbol = txt
        return symbol

    # fill our treeview with the names of all subfolders, beginning with a given path
    def add_files_in_folder(parent, dirname):
        # make a list of all the subfolders and files in it
        files = os.listdir(dirname)
        # walk thru the list an check wether it's a file or a directory
        for f in files:
            # expand to the fullqualified filename
            fullname = os.path.join(dirname, f)
            # is it a dir?
            if os.path.isdir(fullname):
                # insert the dirname into the tree and check if there is a qet_directory file in
                # this dir. When get the 'sy' tagged value out of the file an add it as a column
                # to our treeview
                treedata.Insert(parent, fullname, f, values=[get_symbol_for_directory(fullname)])
                # go recursivly to the next (sub) folder
                add_files_in_folder(fullname, fullname)
            # if it's not a dir, it's a file
            else:
                # treedata.Insert(parent, fullname, f, values=[])
                pass

    # open a input message box for changing the value of a symbol
    def change_item(path, old):
        # got nothing at first
        text_input = ''
        # define a messagebox layout
        changelayout = [[sg.Text(path)],
                        [sg.InputText(old)],
                        [sg.Submit(), sg.Cancel()]]
        # show the messagebox window
        wnd = sg.Window('Change the Value for ', changelayout)
        # wait for the buttons be clicked
        while True:
            # read the event values
            ev2, vals2 = wnd.read()
            # exit or windowclosed is clicked, nothing to get
            if ev2 is None or ev2 == 'Exit':
                wnd.close()
                break
            wnd.close()
            # any other button (e.g. OK Button) is clicked we get an input
            text_input = vals2[0]
        return text_input

    # this is nessesary because we have to rebuild the treeview window any
    # time as we do changes on it
    def set_layout_for_mainwin():
        layout = [[sg.Text('Please give a two char text of your language')],
                  [sg.InputText('de', key='_language_')],
                  [sg.Text('Select the folder you want to change the symbol for')],
                  [sg.Tree(data=treedata, headings=['symbol'], auto_size_columns=True, num_rows=20, col0_width=30,
                           key='_TREE_', show_expanded=False, enable_events=True), ],
                  [sg.Button('Change'), sg.Button('Save'), sg.Button('Help'), sg.Button('Cancel')]]
        return layout

    # our main sequence starts here:

    # depending on our platform we could now show the path where the (user) elements stored
    # but may we got some more than one user or something has been changed we give the
    # oppotunity to select another path
    starting_path = sg.PopupGetFolder('Folder to display', default_path=elementspath)

    if not starting_path:
        exit()

    # the treeview object in PySimpleGui - must be init
    treedata = sg.TreeData()

    # fill the treeview with pathes and label symbols
    add_files_in_folder('', starting_path)

    # first we want to display a (main) window
    window2_active = False
    # define our main window layout
    # in the moment it is

    # Text-Label
    # Treeview with two columns
    # Button line with four buttons

    layout1 = set_layout_for_mainwin()
    window = sg.Window('Modify element letter').Layout(layout1)

    # go to th eevent lop of window 1
    while True:  # Event Loop
        # if button clicked, get the button and Value
        # values hold the fullqualified pathname of the selected row in treeview

        event, values = window.Read()
        # set the language option
        if values['_language_']:
            language = values['_language_']
            print('Lang: ', language)
        # the button change is clicked and the action for this isn't yet started
        if event is 'Change' and not window2_active:
            # set the action as active
            window2_active = True
            # normaly just hide the window, but PySimpleGui could not refresh a treeview so....
            # window.hide()
            # we close the window 1
            window.close()
            # if a row is selected in treeview
            if values['_TREE_']:
                # get a new value for the seleced path
                newvalue_for_path = change_item(values['_TREE_'][0], get_symbol_for_directory(values['_TREE_'][0]))
                # something change, so we have to refresh the view
                if set_symbol_for_directory(values['_TREE_'][0], newvalue_for_path):
                    # todo update Treeview - workaround : fill a new ;(
                    treedata = sg.TreeData()
                    add_files_in_folder('', starting_path)
            # close our  changing window
            window2_active = False
            # create the layout for window 1 new
            layout1 = set_layout_for_mainwin()
            window = sg.Window('Modify element letter').Layout(layout1)
            # normaly just hide the window, but PySimpleGui could not refresh a treeview so....
            # window.un_hide()
        # the button Save is clicked
        if event is 'Save':
            save_as_xml(os.path.join(home, qet_labels_name))
        # the button help is clicked
        if event is 'Help':
            show_help_messagebox()
        # the button Cancel is clicked
        if event in (None, 'Cancel'):
            break

if __name__ == "__main__":
    main()
