euler.png : euler.dat plot.py
	python plot.py
euler.dat: a.out 
	./a.out
a.out: CendalesLuisS5C2.cpp
	g++ CendalesLuisS5C2.cpp