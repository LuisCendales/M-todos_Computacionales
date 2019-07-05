CendalesLuisResorte.png : datos.dat CendalesLuis_S5C3_plots.py
	python CendalesLuis_S5C3_plots.py
datos.dat: a.out 
	./a.out
a.out: CendalesLuis_S5C3_ODEs.cpp
	g++ CendalesLuis_S5C3_ODEs.cpp