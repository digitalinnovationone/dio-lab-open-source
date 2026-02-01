#include <stdio.h>
int main() {
    int n1, n2, n3, n4, n5, n6, pivo;
    int bonifica1 = 0, penaliza1 = 0, bonifica2 = 0, penaliza2 = 0;
    int pontjogador1, pontjogador2;
    scanf ("%d %d %d %d %d %d %d", &n1, &n2, &n3, &n4, &n5, &n6, &pivo);
    
    if (pivo % 2 == 0) {
        if (n1 % 2 == 0) 
            bonifica1 += n1;
         else 
            penaliza1 += n1;
         if (n2 % 2 == 0) 
            bonifica1 += n2;
         else 
            penaliza1 += n2;
         if (n3 % 2 == 0) 
           bonifica1 += n3;
         else 
            penaliza1 += n3;
        
    }
     else {
         if (n1 %2 !=0) 
             bonifica1 += n1;
          else 
             penaliza1 += n1;
          if (n2 %2 !=0) 
             bonifica1 += n2;
          else 
             penaliza1 += n2;
          if (n3 %2 !=0) 
             bonifica1 += n3;
          else 
             penaliza1 += n3;
         
         
     }
      if (pivo % 2 == 0) {
        if (n4 % 2 == 0) 
            bonifica2 += n4;
         else 
            penaliza2 += n4;
         if (n5 % 2 == 0) 
            bonifica2 += n5;
         else 
            penaliza2 += n5;
         if (n6 % 2 == 0) 
           bonifica2 += n6;
         else 
            penaliza2 += n6;
        
    }
     else {
         if (n4 %2 !=0) 
             bonifica2 += n4;
          else 
             penaliza2 += n4;
          if (n5 %2 !=0) 
             bonifica2 += n5;
          else 
             penaliza2 += n5;
          if (n6 %2 !=0) 
             bonifica2 += n6;
          else 
             penaliza2 += n6;
         
     }
        pontjogador1 = bonifica1 - penaliza1;
        pontjogador2 = bonifica2 - penaliza2;
  
     if (pontjogador1 > pontjogador2)
        printf("Jogador1 %d", pontjogador1);
     else if (pontjogador1 < pontjogador2) 
    printf("Jogador2 %d", pontjogador2);
     else 
        printf("Empate"); 
    
    return 0;
}
