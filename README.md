# web-highlighter
highlights terms in an array in an exported excel workbook
Generates a new primary HTML file that the secondary workbook is nested in, removes references to the old workbook name.
Does not iterate through multiple workbooks at this time.
A possible solution to this is checking the XML file for more sheets then iterating through those sheets with another for loop.


This is just a quick and dirty script written to highlight asset numbers on a map build in excel to save time in locating assets.

There's also a GUI for the script built in tkinter. The actual python script for this is much larger as I realized I needed to iterate over many workbooks and also generate a new tab HTML webpage that points to the newly created files. There was also an issue with having to remove some other HTML which would sort of redirect towards the older files if all the original files names aren't corrected with the new master file name.


The goal behind this program was to be able to have a map system for assets (hundreds of static stations) that is editable in Microsoft excel, but searchable with python. A significant amount of time was being wasted by technicians manually looking at printed off maps for assets. This program in its entirety takes a job that could possibly take over an hour down to under a couple minutes. The tkinter interface was developed to allow other technicians to use the script without much hassle. 


I can not share the finished version of this work due to the nature of my employment.
