#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
   unsigned int hp:7;
   unsigned int bot:1;
	char name[3];
} mon;

void play();
void setup(mon*,mon*);
void move(mon*,mon*,char);
void slash(mon*,mon*);
void heal(mon*);
void lunge(mon*,mon*);
void wait(int);

main()
{
	srand(time(0));
	printf("s = slash, h = heal, l = lunge, e = exit\n\n");
   play();
}

void play()
{
   mon one, two;
   setup(&one,&two);
	char turn = 0;
	unsigned int turnCount = 1;
	
   while(one.hp > 0 && two.hp > 0) {
		printf("\n%s hp: %i and %s hp: %i\n", one.name, one.hp, two.name, two.hp);
		if(rand()%(2<<turnCount)) {
			turnCount = 1;
			turn = !turn;
		} else
			turnCount++;
		move(&one, &two, turn);
	}
	
	printf("\nFinal %s hp: %i and %s hp: %i\n", one.name, one.hp, two.name, two.hp);
	if(one.hp > 0)
		printf("One wins!!!");
	else
		printf("Two wins!!!");
}

void setup(mon *a, mon *b)
{
   int ans;
	printf("How many players?\n");
      
   scanf(" %i", &ans);
   switch(ans) {
      case 1: a->bot = 0; b->bot = 1; break;
      case 2: a->bot = b->bot = 0; break; 
      default: a->bot = b->bot = 1;
   }
	
   a->hp = b->hp = 127;
	a->name[0] = b->name[0] = 'P';
	a->name[1] = '1';
	b->name[1] = '2';
	a->name[2] = b->name[2] = '\0';
}

void move(mon *a, mon *b, char turn)
{
	if(turn) {
		mon *temp = a; // Switch a and b pointers
		a=b;
		b=temp;
	}
	printf("%s: ", &a->name);
   if(a->bot) {
		int s, h, l;
		
		wait(rand()%4+1);
		
		s = rand()%(127/b->hp);
		h = rand()%(127/a->hp);
		l = rand()%2;
		
		if(s > l && s > h) {
			printf("s\n");
			wait(1);
			slash(a, b);
		} else if(h > s && h > l) {
			printf("h\n");
			wait(1);
			heal(a);
		} else {
			printf("l\n");
			wait(1);
			lunge(a, b);
		}
		
	} else {
		char ans;
		do 
			scanf(" %c", &ans);
		while(ans != 's' && ans != 'h' && ans != 'l' && ans != 'e');
		switch(ans) {
			case 's': slash(a, b); break;
			case 'h': heal(a); break;
			case 'l': lunge(a, b); break;
			default: a->hp = 0;
		}
	}
}

void slash(mon *a, mon *b)
{
	int change = rand()%4 * 3 + 5;
	b->hp = (b->hp-change < 0) ? 0 : b->hp - change;
	printf("%s slashes %s (-%i).\n", a->name, b->name, change);
}

void heal(mon *a)
{
	int change = (rand()%3+1) * 7;
	a->hp = (a->hp+change > 127) ? 127 : a->hp + change;
	printf("%s heals self (+%i).\n", a->name, change);
}

void lunge(mon *a, mon *b)
{
	int change;
	if(rand()%3) {
		change = rand()%6 * 7 + 1;
		b->hp = (b->hp-change < 0) ? 0 : b->hp - change;
		printf("%s lunges at %s (-%i).\n", a->name, b->name, change);
	} else {
		change = rand()%3*15;
		a->hp = (a->hp-change < 0) ? 0 : a->hp - change;
		printf("%s missed (-%i).\n", a->name, change);
	}
}

void wait(int s)
{
	// Wait for s seconds.
	s += time(0);
	while(time(0) < s)
		;
}
