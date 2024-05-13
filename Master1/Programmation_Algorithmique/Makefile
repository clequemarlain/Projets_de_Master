CC=gcc

all:executable

executable: projet_final.o projet_pt1.o projet_pt2.o projet_pt3.o
	$(CC) -o executable projet_final.o projet_pt1.o projet_pt2.o projet_pt3.o -lturbojpeg -lm
projet_pt1.o:projet_pt1.c functions.h
	$(CC) -c projet_pt1.c -lturbojpeg -lm 
projet_pt2.o:projet_pt2.c functions.h
	$(CC) -c projet_pt2.c -lturbojpeg -lm 
projet_pt3.o:projet_pt3.c functions.h
	$(CC) -c projet_pt3.c -lturbojpeg -lm 
clean:
	rm projet_final.o projet_pt1.o projet_pt2.o projet_pt3.o executable core
