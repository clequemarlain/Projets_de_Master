
#define OUTFILENAME "low.jpg"
#include <stdlib.h>


#include "functions.h"

//Conversion ASCII vers noir et blanc
unsigned char* remplircases(int numero_c,int width,int height,unsigned char *rgbbuffer,int jwidth,int jheight,int NB,int longe,int large){ 

  //printf("%d ", numero_c);
  //printf("%d ",larT);s
  if(NB== 500){
    return (rgbbuffer);
  }
  int i = numero_c%(large);
  int j = (numero_c-i)/(large);
  //printf("i:%d,j:%d ",i,j);
  for(int u =0; u<height;u++){
    for(int v = 0; v<width ;v++){


      rgbbuffer[(j*height*jwidth*3)+(3*width*i)+3*v+(u*jwidth*3)]=NB;
      rgbbuffer[(j*height*jwidth*3)+(3*width*i)+3*v+(u*jwidth*3)+1]=NB;
      rgbbuffer[(j*height*jwidth*3)+(3*width*i)+3*v+(u*jwidth*3)+2]=NB; 
      //printf("%d ", (i*height*jwidth*3)+(3*width*j)+3*v+(u*jwidth*3));
    }
  }

  return(rgbbuffer);
}



// fonction de convertion du caractere en valeur de 0 a 255

int conv256(char A, char *C[6][7]){

  int couleur = 500;
  for(int i =0; i<6;i++){
    for(int j = 0; j<7 ;j++){

    if(A == *C[i][j]){
    couleur = (j*36 + i*6);
      }
     }
    }
    //printf("%d",couleur);
    return(couleur);
}



unsigned char* lectxt_conv(unsigned char* srcbuffer, int jwidth, int jheight, int width, int height,char *C[6][7],int longe, int large){
    //ouverture du txt
  
  
    FILE * fp;
    fp = fopen("texteimage.txt","r");
    
    if (fp == NULL) {
      printf("erreur \n");
      }
    int numero_c = 0;
    int NB;
    

    // premiere occurence
    char c = fgetc(fp);
    NB = conv256(c,C);
    srcbuffer = remplircases(numero_c,width,height,srcbuffer,jwidth,jheight,NB,longe, large);
    
    while((c = fgetc(fp)) != EOF){
      // je rempli mon tableau des caracteres pour ensuite convertire le srcbuffer
      //printf("%d",numero_c);
      //printf("%c\n", c);
      NB = conv256(c,C);
      if(NB== 500){
        numero_c = numero_c-1;
     }

      numero_c = numero_c + 1;
      srcbuffer = remplircases(numero_c,width,height,srcbuffer,jwidth,jheight,NB, longe, large);
    }
    return(srcbuffer);

  }


  void Image_NB(unsigned char* srcbuffer,unsigned char *jbuffer, int jwidth, int jheight, int tjsamp, int tjstatus, tjhandle handle, long unsigned int jsize,char *C[6][7],int longe, int large ){

  int width = (jwidth/large); //largeur du pavé
  int height = (jheight/longe); //hauteur du pavé
  
  // APPEL DE LA FONCTION 

  srcbuffer = lectxt_conv(srcbuffer,jwidth,jheight,width,height,C, longe, large);

  //printf("%d ESTTTTT", srcbuffer[4291182]);

  
  // Compress srcbuffer in jbuffer
  handle = tjInitCompress() ;   // check for non NULL
  tjstatus = tjCompress2 (handle, srcbuffer, jwidth, 0, jheight, TJPF_RGB, &jbuffer, &jsize, TJSAMP_444, 100, 0) ;
  tjDestroy (handle) ; 
  printf ("tjstatus is %d.\n", tjstatus) ;


  
  // Writeout
  FILE *outfile = fopen (OUTFILENAME, "wb") ;
  fwrite (jbuffer, jsize, 1, outfile) ;
  fclose (outfile) ;

}
