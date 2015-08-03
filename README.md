#UTPL
###Professor:
- Rodrigo Barba [lrbarba@utpl.edu.ec](mailto:lrbarba@utpl.edu.ec)

###Students:
- Marcelo Bravo [mdbravo4@utpl.edu.ec](mdbravo4@utpl.edu.ec)
- Galo Celly [gscelly@utpl.edu.ec](gscelly@utpl.edu.ec)
- Nicholas Earley [nearley@utpl.edu.ec](nearley@utpl.edu.ec)

Detect Numbers Meter
====================
This project involved an investigation in detecting meter numbers using Python and OpenCV API. The code is free to be used and modified by anyone wishing to do so.
It was designed with the purpose of recognizing numbers light meters (eg meter in folder 'images')



System Requirements
-------------------
	•	An i3 or better processor. The faster the better, especially at high video resolutions.
	•	2 GB or more RAM.
	•	At least 100 MB Free Disk space Windows 7 or later, OS X 10.8 or later (has only been tested on 10.9), Linux 3.0+

Installation
-------------
	1.	First, one should install the following libraries:
	◦	OpenCV version 2.4.10+
	◦	Python 2.7.9 (or any later Python 2.x) (See Installation on OS X if using a Mac)
	◦	Numpy 1.9.2+
	◦	Scipy 0.15.1+
	2.	Now download and extract this repository with one of several options:
	◦	Clone the repository with $ git clone https://github.com/VAUTPL/Deteccion.git
	◦	Download the repository as a .zip or .tar.gz and then extract it.

Installation on OS X
--------------------
Apple uses a prior version of Python that does not support the latest Python libraries. One work around is to install Python with Homebrew:

`$ brew install python`

Replacing Apple's system Python with an unsupported version may break things. Therefore we linked Homebrew's Python into the system path without replacing the system Python:

`$ ln -s /usr/local/Cellar/python/2.x.y/bin/python /bin/hbpython`

Where 2.x.y is the version number of your Python.

Running
-------
From a command line in the folder of the repository:
First you have to run train.py  
`$ python train.py -dataset data/digits.csv -model models/svm.cpickle`

Then you can detect with detect_numbers_images.py It serves to detect the number of meters of an image

`$ python detect_numbers_images.py --model models/svm.cpickle --image images/f5a.jpg `

It serves to detect the number of meters of web cam

`$ python detect_numbers_webcam.py --model models/svm.cpickle`

A box where you will take the first picture (press' q 'to take photo) and analyze, then another box where you take the second photo (press' q'para take photo) appears

To use sounds, if you use OSX, add this line to the program
`os.system ("say Match")`

If you use another system, add this line to the program
`os.system("../sound/si.wav")`
