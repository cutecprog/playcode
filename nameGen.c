#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define rlet() ((rand()%26)+'a')

void pickname(const unsigned int size);

main(int argc, char *argv[])
{
   // Idiot proof
   if(argc == 2) {
      int s = atoi(argv[1]);  // Temporary varible to hold the desire size of the array.
      if(s > 0)
         pickname(s);
   }
}

void pickname(const unsigned int SIZE)
{
   FILE *file;
   srand(time(0));
   char *name = malloc(SIZE+1);
   int i;
   size_t size;
   char *str = malloc(87+SIZE);
   name[SIZE-1] = '\0';

   do {
      for(i=0; i<SIZE; i++)
         name[i] = rlet();
      
      strcpy(str,"lynx -dump -nolist 'http://www.google.com/search?q=");
      strcat(str ,name);
      strcat(str, "' | head -10 | tail -1 > filex.txt");
      system(str);
      
      file = fopen("filex.txt", "r");
      /*if (file == NULL) {
         fprintf(stderr, "Can't open input file in.list!\n");
           exit(1);
      }*/
      
      size = fread(str, 1, 16, file);
      printf("%s %i\n", name, size);
      fclose(file);
   } while(size == 16 || size < 2);

   free(str);
   printf("%s %i\n", name, size);
   free(name);   
   
}
