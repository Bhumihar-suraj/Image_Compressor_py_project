# Image_Compressor_py_project
GUI for Image Compression 
Python Project on Image Compressor/Decompressor

Problem Statement:-
Create a graphical user interface (GUI) application for image compression and decompression using PyQt5. The application should allow users to perform two main tasks:
•	Compression/Depression of single image
•	Compression/Depression of multiple in a folder

Solution:-
1. Importing Libraries:
•	The code begins by importing various Python libraries and modules necessary for building the application.
•	Notable libraries include PyQt5 for the GUI, PIL (Pillow) for image processing, and other standard libraries like sys and os.
2. Class Definition:
•	The code defines a class named `App`, which inherits from `QMainWindow`. This class represents the main application window.
3. Constructor `__init__`:
•	The constructor method initializes the main window's properties, such as its title, size, and position.
•	It also sets up the status bar and loads a custom stylesheet from a file called "design.qss."


4. `initUI` Method:
•	The `initUI` method is responsible for creating the user interface components within the main window.
5. Main Window Components:
•	The GUI is designed as a series of "bubbles" that represent different actions within the application.
•	There are two main bubbles: one for compressing a single image and one for compressing multiple images in a directory.
•	Each bubble consists of labels, buttons, input fields, and frames, which are defined and positioned within the window.
6. Event Handling:
•	Various event handlers are defined for different user interactions, such as mouse clicks on the bubbles.
•	Clicking on a bubble expands it to reveal additional options, allowing the user to choose an image or directory and set the compression quality.
7. Image Compression:
•	The application supports the compression of single images as well as multiple images in a directory.
•	Users can specify the desired compression quality as "High," "Medium," or "Low," which affects the width of the compressed images.
•	The actual image compression is performed using the PIL library's `Image` class.
8. Status Bar Updates:
•	The status bar at the bottom of the window displays messages to inform the user about the progress of image compression.
9. Execution:
•	The code block at the end of the script initializes the PyQt5 application and creates an instance of the `App` class. Then, it starts the application's event loop.

	Software/Hardware Requirements:-

Software Requirements:
1. Python:- The code is written in Python, so you need to have Python installed on your computer. 
2. PyQt5:- PyQt5 is used for building the graphical user interface (GUI).    
3.Pillow (PIL):- Pillow is used for image processing in the application. You can install Pillow using pip:
4.Operating System:- The code is designed to run on various operating systems, including Windows, macOS, and Linux.
5.QSS File (design.qss):-The application uses an external QSS (Qt Style Sheet) file for styling the GUI. Ensure that you have a valid "design.qss" file in the same directory as the Python script.
Hardware Requirements:
1.Computer:-You need a computer or laptop to run the Python application.
2.Input Devices:-A keyboard and a mouse or touchpad for interacting with the GUI.
3.Display:-A display screen to view the GUI.
4.Storage:-Disk space is required for storing the images, especially when compressing multiple images in a directory.


	Steps Followed:-

	Compressing single image at onces
	Compressing multiple images at onces
	PyQt5 – Creating Main Window
	PyQt5 – Main Window – Using external Style Sheet(design.qss)
	PyQt5 – QFrame – adding Frames
	PyQt5 – Multiple screens- Clicking on QFrame
	PyQt5 – QLabel Text to frames
	PyQt5 – QLabel- RichText – Adding back arrow icon for navigation
	PyQt5 – QLineEdit – Designing simple image window
	PyQt5 – QPushButton – Adding buttons on frames
	PyQt5 – QComboBox – Adding quality combobox on frames
	PyQt5 – Designing directory frame
	PyQt5 – QFilesDialog – Choosing image from files
	PyQt5 – Select Folder dialog box
	PyQt5 – Choosing image quality
	PyQt5 – Choosing image quality for directory window
	PyQt5 – Performing compression for single image
	PyQt5 – Input Window- getting new image’s name
	PyQt5 – Status Bar
	Compressing directory of images using UI
	Converting Images compressor to EXE
	Conclusion:-
Overall, this code creates a user-friendly interface for image compression, allowing users to select individual images or folders of images,
set compression quality, and compress them with the specified settings. It provides visual feedback through the status bar, informing users
of the progress of image compression.
