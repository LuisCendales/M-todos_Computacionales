plot.png : PlacaIni.dat Plots_difusion.py
	python Plots_difusion.py
PlacaIni.dat: a.out 
	./a.out
a.out: Difusion.cpp
	g++ Difusion.cpp