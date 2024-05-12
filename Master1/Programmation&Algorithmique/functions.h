#include <stdlib.h>
#include <stdio.h>
#include <turbojpeg.h>
#include <sys/stat.h>
#include <math.h>

struct hsl{
  float h;
  float s;
  float l;
};
typedef struct hsl hsl;

struct size{
  int largeur;
  int longeur;
  int composantes;
};
typedef struct size size;

struct Tableau{
  hsl** T;
};
typedef struct Tableau Tableau; 

//Partie 1
hsl rgbtohsl(float r, float g, float b);

size decoupage(int lignes, int colonnes, int composantes, int longe, int large);

float *convertisseur(unsigned char *rgbbuffer, int jwidth, int jheight);

hsl gethslmoy(int i, int j, float *hslbuffer, size decoupe, int jwidth, int jheight);

Tableau ASCII(float *hslbuffer, size decoupe, int jwidth, int jheight, int longe, int large);

void affichage(char *C[6][7], Tableau T, int longe, int large);

void fichiertext(char *C[6][7],Tableau T, int longe, int large);

//partie 2

unsigned char* remplircases(int numero_c,int width,int height,unsigned char *rgbbuffer,int jwidth,int jheight,int NB,int longe, int large);

int conv256(char A, char *C[6][7]);

unsigned char* lectxt_conv(unsigned char* srcbuffer, int jwidth, int jheight, int width, int height,char *C[6][7], int longe, int large);

void Image_NB(unsigned char* srcbuffer,unsigned char *jbuffer, int jwidth, int jheight, int tjsamp, int tjstatus, tjhandle handle, long unsigned int jsize,char *C[6][7], int longe, int large );

//partie 3
void Pixel_art(char *C[6][7],Tableau T,char *B[256],int longe, int larges);

