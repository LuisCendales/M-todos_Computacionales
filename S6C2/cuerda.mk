plot.png : datos.dat Plots_cuerda.py
	python Plots_cuerda.py
datos.dat: a.out 
	./a.out
a.out: CendalesLuis_cuerda.cpp
	g++ CendalesLuis_cuerda.cpp