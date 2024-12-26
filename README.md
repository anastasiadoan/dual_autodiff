Hello!!! Welcome to the package!

# Dual_autodiff

## Description
This reporsitory contains the code for the dual_autodiff package and a report detailing the process of making the package. The aim was to demonstrate software developping good practice and also a Cythonized version of the package using C was implemented to compare the performance of pure Python and Cythonized Python.

## Contents

Inside this directory, there are a few sub-directories one can explore. 

The first code directory (```dual_autodiff```) contains all the code used in the package. Within this directory, there is also a Jupyter notebook called (```task5.ipynb```) which solve task 5 of the project.

The second is the dual_autodiff_x directory (```dual_autodiff_x```), which is the cythonized version of the package. To obey the requirement for task 10, the (```__init__.py```) file has been renamed to (```__init__.pyx```).

There is also a (```docs```) which contains a html pages that feature all what
we have implemented with clear explanations and examples. 

Also, the code directory (```Docker-Test```) is made to test the wheels using Docker Image.

There is a Jypyter notebook called (```dual_autodiff.ipynb```) which is used to compare the running time of Pure Python and Cythonized dual_autodiff package.

The last one is the ```report``` directory, which contains the LaTeX file for the report, as well as the pdf version of it, along with the references ```.bib``` file.

## How to run

To run the ```dual_autodiff``` package, you can use the simple line of code ```pip install -e . ``` to be able to install the package everywhere in your repository. 

You can play around with the package and test whether it works using ```pytest -s tests\*```.

The html version of the package is inside ```docs/build/html``` and ready to run by ```open index.html```.

In the ```dual_autodiff_x``` file there is a file called ```wheelhouse```. Two wheels of the cythonized package ```dual_autodiff_x``` were created and put in here, if you download it to your local computer, using CSD3 or Docker Image, you can run this wheel as a package ```dual_autodiff_x```.

There is also a folder ```Docker-Test``` that includes several files. A dockerfile is already written so that you can test to install the wheel for Python 3.10 immediately by ```docker build --platform linux/amd64 -t my-python-app .```.

## Running time
All of the code are run on Macbook Air M1 2020 8Gb Memory. All packages and jupyternotebooks take less than 1 minutes to run.