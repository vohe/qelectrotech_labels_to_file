## Element-Labels

![Project Image](project-image-url)

> Python script to help keep qelectotech element labels in place.

---

### Table of Contents
Jump to read.

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

Every symbol in qelectotech has a symbol label. The build in symbols uses labels, but the user created symbols doesn't have labels at all, except - the user himself add them.
Manual adding this label tags is a mess. So with a little help of this tool it gets easier.
Qelectrotech stores all information about the (user-)elements in a file called 'qet_labels.xml'.
That is a file represent the whole filepath below users-appdata-qet/elements and for each of that incudet folder there could be a <prefix> tag in the xml file which is directly the label for a symbol in that directory.
if no prefix is given, qelectrotech uses the one of the parent folder.

![Project Image](https://github.com/vohe/qelectrotech_labels_to_file/blob/master/howto/add_folder_sy_tag.png)

But inside qelectrotech there is no option to change or create this labels. The was - till now - is to modify or create the qet_labels.xml file.
Therefor it is possible to add a language description for each folder inside of qelectrotech.
That is the point we use to add our label! And a (fiction) language called sy (only two letters supported!) and you label tag for that folder. That's it.
That information is stored in a file called qet_directory in every folder of the collection. 

In this case you could use this script.
After start it ask for the position of the qet elements folder. (A choice is given so you don't need to change it.)
Then a treeview is given, showing the (sub-)folders from the given path and labels.
Just by select the folder with your elements in it, you can change the Label.
Afte your done, you save your work -  i modify's the qet_labels.xml file.

#### Technologies

- Python (tested under 3.7 linux)
- XML etree (pyhton)
- XML Sax
- README.md created under the hood of (https://github.com/jamesqquick/read-me-template)
[Back To The Top](#Element-Labels)

---

## How To Use
python Elementsym_tofile.py
Look this smal video for more information (https://vimeo.com/user109668906/review/397627826/962f235e15)
#### Installation

just download and start

#### API Reference

```html
    <p>not now</p>
```
[Back To The Top](#Element-Labels)

---

## References
Qelectorech.org 

https://qelectrotech.org/
[Back To The Top](#Element-Labels)

---

## License

CC 3.0 License

https://creativecommons.org/licenses/by/3.0/de/

Copyright (c) [2020] [V.Heggemann]

[Back To The Top](#Element-Labels)

---

## Author Info

- mail - [Voker Heggemann] (vohegg at gmail.com)

[Back To The Top](#Element-Labels)

