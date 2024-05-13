
#include "functions.h"

#define JCOMPONENTS 3


//ici on détermine la fonction qui nous permet de convertir un vecteur rgb en un vecteur hsl

hsl rgbtohsl(float r, float g, float b){
  r /= 255, g /= 255, b /= 255;
    float max = fmax(r,fmax(g,b));
    float min = fmin(r,fmin(g,b));
    float h,s,l;
    h = (max + min) / 2;
    s = (max + min) / 2;
    l = (max + min) / 2;
    
    if(max == min){
        h = s = 0; 
    }
    
    else{
        float d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);

        if(max = r){
              h = (g - b) / d + (g < b ? 6 : 0); 
            }
        if(max=g){
              h = (b - r) / d + 2; 
            }
            else{
                h = (r - g) / d + 4; 
        }
        h /= 6;
    }
    hsl pixel;
    pixel.h = h;
    pixel.s = s;
    pixel.l = l;
    return (pixel);
}

//On détermine une fonction qui nous permet d'obtenir le nombre de lignes et de colonnes de chaque pavé (rmq : une fois découpé chaque case contient un vecteur rgb)

//size decoupage(int lignes, int colonnes, int composantes){

size decoupage(int lignes, int colonnes, int composantes, int longe, int large){

  int l;
  int c;
  l=floor(lignes/longe);
  c=floor(colonnes/large);
  size decoupe;
  decoupe.longeur = l;
  decoupe.largeur = c;
  decoupe.composantes = JCOMPONENTS;
  return (decoupe);
}

// on définit une fonction qui permet d'obtenir un buffer hsl à partir d'un buffer rgb

float *convertisseur(unsigned char *rgbbuffer, int jwidth, int jheight){
  float *hslbuffer;
  hslbuffer = malloc(jheight*jwidth*sizeof(hsl));
  for (int i=0; i<jwidth*jheight*3; i+=3){
    *(hslbuffer+i)= rgbtohsl(*(rgbbuffer+i), *(rgbbuffer+i+1), *(rgbbuffer+i+2)).h;
    *(hslbuffer+i+1)= rgbtohsl(*(rgbbuffer+i), *(rgbbuffer+i+1), *(rgbbuffer+i+2)).s;
    *(hslbuffer+i+2)= rgbtohsl(*(rgbbuffer+i), *(rgbbuffer+i+1), *(rgbbuffer+i+2)).l;
  }
  return(hslbuffer); 
}

//ici on définit une fonction qui permet d'obtenir la moyenne d'un pavé en terme de vecteur hsl

hsl gethslmoy(int i, int j, float *hslbuffer, size decoupe, int jwidth, int jheight){
  hsl result;
  result.h=0;
  result.s=0;
  result.l=0;
  for(int ligne=0; ligne<decoupe.longeur; ligne++){
    for(int col=0; col<decoupe.largeur*3; col+=3){
      result.h += *(hslbuffer+(i*decoupe.longeur*jwidth*3)+(ligne*jwidth*3)+(3*decoupe.largeur*j)+col);
      result.s += *(hslbuffer+(i*decoupe.longeur*jwidth*3)+(ligne*jwidth*3)+(3*decoupe.largeur*j)+col+1);
      result.l += *(hslbuffer+(i*decoupe.longeur*jwidth*3)+(ligne*jwidth*3)+(3*decoupe.largeur*j)+col+2);
    }
  }
  result.h = result.h/(decoupe.largeur*decoupe.longeur);
  result.s = result.s/(decoupe.largeur*decoupe.longeur);
  result.l = result.l/(decoupe.largeur*decoupe.longeur);
  return(result);

}

//ici on définit une fonction qui crée le tableau qui contient dans chaque case la moyenne hsl du pavé correspondant aux coordonées de la case

//Tableau ASCII(float *hslbuffer, size decoupe, int jwidth, int jheight){
Tableau ASCII(float *hslbuffer, size decoupe, int jwidth, int jheight, int longe, int large){

  printf("%d \n",decoupe.longeur);
  printf("%d \n",decoupe.largeur);
  Tableau T;
  T.T = (hsl**) malloc((longe)*sizeof(hsl*));
  for(int i=0;i<longe;i++){
    T.T[i] = (hsl*) malloc((large)*sizeof(hsl));
  }

  for(int i =0; i<longe;i++){
    for(int j = 0; j<large ;j++){
      T.T[i][j] = gethslmoy(i,j,hslbuffer,decoupe,jwidth,jheight);
    }   
  }
  return(T);
}

//ici on détermine une fonction qui permet d'afficher simplement le résultat obtenu

void affichage(char *C[6][7], Tableau T,int longe, int large){
  for(int i =0; i<longe;i++){
    for(int j = 0; j<large ;j++){
        printf("%s",C[(int)(T.T[i][j].h*6)][(int)(T.T[i][j].l*7)]);
        //printf(" %f",T.T[i][j].h);
        //printf(" %d",(int)(7*T.T[i][j].l));
    }
    printf("\n");
  }
}

//Enfin ici on crée une fonction qui permet de copier le résultat obtenu sur un fichier texte 

void fichiertext(char *C[6][7],Tableau T,int longe, int large){
  FILE *intext = NULL;
  intext = fopen ("texteimage.txt","w");
  if(intext==NULL){
    printf("Erreur" );

  }
  for(int i =0; i<longe;i++){
    for(int j = 0; j<large ;j++){
        fprintf(intext,"%s",C[(int)(T.T[i][j].h*6)][(int)(T.T[i][j].l*7)]);
        //printf(" %f",T.T[i][j].h);
        //printf(" %d",(int)(7*T.T[i][j].l));
    }
    fprintf(intext,"\n");
  }
  fclose(intext);
}
