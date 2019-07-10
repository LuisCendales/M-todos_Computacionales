plot.png : datos1.dat Plots_cuerdayTambor.py
	python Plots_cuerdayTambor.py
datos1.dat: a.out 
	./a.out
a.out: CendalesLuis_cuerdayTambor.cpp
	g++ CendalesLuis_cuerdayTambor.cpp