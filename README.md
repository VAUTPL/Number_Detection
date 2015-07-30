{\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;\f2\fnil\fcharset0 LucidaGrande;
\f3\fmodern\fcharset0 Courier-BoldOblique;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue233;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid101\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid102\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid2}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa321

\f0\b\fs48 \cf0 \expnd0\expndtw0\kerning0
Detect Numbers Meter\
\pard\pardeftab720\sl320\sa240

\f1\b0\fs24 \cf0 \expnd0\expndtw0\kerning0
This project involved an investigation in detecting meter numbers using Python and OpenCV API. The code is free to be used and modified by anyone wishing to do so\
\pard\pardeftab720\sa298

\f0\b\fs36 \cf0 \expnd0\expndtw0\kerning0
System Requirements\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl320
\ls1\ilvl0
\f1\b0\fs24 \cf0 \kerning1\expnd0\expndtw0 {\listtext	\'95	}\expnd0\expndtw0\kerning0
An i3 or better processor. The faster the better, especially at high video resolutions.\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\'95	}\expnd0\expndtw0\kerning0
2 GB or more RAM.\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\'95	}\expnd0\expndtw0\kerning0
At least 100 MB Free Disk space Windows 7 or later, OS X 10.8 or later (has only been tested on 10.9), Linux 3.0+\
\pard\pardeftab720\sa298

\f0\b\fs36 \cf0 \expnd0\expndtw0\kerning0
Installation\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl320
\ls2\ilvl0
\f1\b0\fs24 \cf0 \kerning1\expnd0\expndtw0 {\listtext	1.	}\expnd0\expndtw0\kerning0
First, one should install the following libraries:\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\sl320
\ls2\ilvl1\cf2 \kerning1\expnd0\expndtw0 {\listtext	
\f2 \uc0\u9702 
\f1 	}{\field{\*\fldinst{HYPERLINK "http://opencv.org/"}}{\fldrslt \expnd0\expndtw0\kerning0
\ul OpenCV}}\cf0 \expnd0\expndtw0\kerning0
\'a0version 2.4.10+\
\ls2\ilvl1\cf2 \kerning1\expnd0\expndtw0 {\listtext	
\f2 \uc0\u9702 
\f1 	}{\field{\*\fldinst{HYPERLINK "https://www.python.org/"}}{\fldrslt \expnd0\expndtw0\kerning0
\ul Python}}\cf0 \expnd0\expndtw0\kerning0
\'a02.7.9 (or any later Python 2.x) ({\field{\*\fldinst{HYPERLINK "https://github.com/VAUTPL/Deteccion/blob/master/README.md#installation-on-os-x"}}{\fldrslt \cf2 \expnd0\expndtw0\kerning0
\ul \ulc2 See\'a0
\f3\i\b \expnd0\expndtw0\kerning0
Installation on OS X
\f1\i0\b0 \expnd0\expndtw0\kerning0
\'a0if using a Mac}})\
\ls2\ilvl1\cf2 \kerning1\expnd0\expndtw0 {\listtext	
\f2 \uc0\u9702 
\f1 	}{\field{\*\fldinst{HYPERLINK "http://www.numpy.org/"}}{\fldrslt \expnd0\expndtw0\kerning0
\ul Numpy}}\cf0 \expnd0\expndtw0\kerning0
\'a01.9.2+\
\ls2\ilvl1\cf2 \kerning1\expnd0\expndtw0 {\listtext	
\f2 \uc0\u9702 
\f1 	}{\field{\*\fldinst{HYPERLINK "http://www.scipy.org/"}}{\fldrslt \expnd0\expndtw0\kerning0
\ul Scipy}}\cf0 \expnd0\expndtw0\kerning0
\'a00.15.1+\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl320
\ls2\ilvl0\cf0 \kerning1\expnd0\expndtw0 {\listtext	2.	}\expnd0\expndtw0\kerning0
Now download and extract this repository with one of several options:\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\sl320
\ls2\ilvl1\cf0 \kerning1\expnd0\expndtw0 {\listtext	
\f2 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
Clone the repository with\'a0$ git clone https://github.com/VAUTPL/Deteccion.git\
\ls2\ilvl1\kerning1\expnd0\expndtw0 {\listtext	
\f2 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
Download the repository as a\'a0.zip\'a0or\'a0.tar.gz\'a0and then extract it.\
\pard\pardeftab720\sa298

\f0\b\fs36 \cf0 \expnd0\expndtw0\kerning0
Installation on OS X\
\pard\pardeftab720\sl320\sa240

\f1\b0\fs24 \cf0 \expnd0\expndtw0\kerning0
Apple uses a prior version of Python that does not support the latest Python libraries. One work around is to install Python with Homebrew:\
$ brew install python\
Replacing Apple's system Python with an unsupported version may break things. Therefore we linked Homebrew's Python into the system path without replacing the system Python:\
$ ln -s /usr/local/Cellar/python/2.x.y/bin/python /bin/hbpython\
Where 2.x.y is the version number of your Python.\
\pard\pardeftab720\sa298

\f0\b\fs36 \cf0 \expnd0\expndtw0\kerning0
Running\
\pard\pardeftab720\sl320\sa240

\f1\b0\fs24 \cf0 \expnd0\expndtw0\kerning0
From a command line in the folder of the repository:\
First you have to run train.py  \
$ python train.py -dataset data/digits.csv -model models/svm.cpickle\
then you can detect with detect_numbers_images.py It serves to detect the number of meters of an image\
$ python detect_numbers_images.py --model models/svm.cpickle --image images/f5a.jpg    \
It serves to detect the number of meters of web cam\
$ python detect_numbers_webcam.py --model models/svm.cpickle\
A box where you will take the first picture (press' q 'to take photo) and analyze, then another box where you take the second photo (press' q'para take photo) appears\
}