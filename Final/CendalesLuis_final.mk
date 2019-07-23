all : Canal.png filtro.png

filtro.png : CendalesLuis_Fourier.py
	python CendalesLuis_Fourier.py

Canal.png : canal_ionico.txt CendalesLuis_canal_ionico.py
	python CendalesLuis_canal_ionico.py
    

