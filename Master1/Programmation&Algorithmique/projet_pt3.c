


#include "functions.h"
// Pixel Art: Caractères en couleur
void Pixel_art(char *C[6][7],Tableau T,char *B[256],int longe, int large){
  for(int i =0; i<longe;i++){
    for(int j = 0; j<large ;j++){
        printf("%s%s",B[(int)(T.T[i][j].h*256)],C[(int)(T.T[i][j].h*6)][(int)(T.T[i][j].l*7)]);
    }
    printf("\n");
  }
}