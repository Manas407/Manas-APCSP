#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define SIZE1 5000
#define SIZE2 10000
#define SIZE3 50000
int *readFile(string fileName, int size, int size2);  //pointer to return and int array
int linearSearch(int array[], int size);  //linear search
int binarySearch(int array[]);
int *bubbleSort(int array[]);
int *selectionSort(int array[], int size);
void printArray(int sortArray[], int size);

int main(void)
{

    string fileName=get_string("Enter File name ");
    FILE* file=(fopen(fileName, "r"));
    if(!file)
    {
    printf("\n Unable to open : %s ", fileName);
    return -1;
    }
    fclose(file); // WHY CLSOING FILE?
    int *array;
    array=readFile(fileName, 10000, 5);   // call of the function
    int *sorted  = selectionSort(array, SIZE2);
   // printArray(sorted, SIZE2);
    //int guess=get_int("give me a number in between 0 and 10000");
    int indx = 0;
    // int indx = linearSearch(array, guess, SIZE2);
  //  printf("the index is %i \n", indx);
    indx=binarySearch(sorted);
    // printf("the binary index is %i \n", indx);



{

printf("                |--------------------------| \n");
printf("                1. read array \n");
printf("                2. linear search the file \n");
printf("                3. binary search the file\n");
printf("                4. bubble search the file\n");
printf("                5. selection sort the file\n");
printf("                6. print file contents \n");
printf("                7.Exit \n");
printf("                |--------------------------| \n");
char choice;
 do
    {
         choice = get_char("enter function choice: \n");
    }
while (choice <= 1 || choice >= 6);
array[50,000];
int index=0;
string filename=" ";
int size = 50000;
switch (choice)
{


    case '1':
    //ask user for the file name
    filename = get_string ("Enter filename");
    array = readFile(fileName, 50000,6);
    printf(" file has been read! \n");
    break;

    case '2':
     index=linearSearch(array, size);                // linear sort
   printf(" index is on :%i",index);
    break;


    case '3':
index = binarySearch(array);
   printf(" index is on :%i",index);
    break;

    case '4':
 *selectionSort(array, size);
 printf("sorted!");
    break;

    case '5':
    printArray(sortArray, size);
    break;

    case '6':
    printf(" Cya! \n");
    break;


}
}
}
int *readFile(string fileName, int size, int size2 )
    {


    FILE* file=(fopen(fileName, "r"));

    char line[size2]; //how many characers per line
    char options[size][size2];//array to put all the numbers from the file

    int  static numbers[SIZE2];  // file to be returned

    for (int i=0; i < size; i++)
    {
        fscanf(file, "%s", options[i]);
        // printf("%s \n", options[i]);
        numbers[i]= atoi(options[i]);
    }
    fclose(file);
   return numbers;
}
int linearSearch(int array[], int size )                // linear sort
{
    int guess=get_int("give me a number in your file");
    for( int i = 0; i < size; i++)
    {
        if (array[i] == guess)
        {
            printf (" your number is on line %i ",i);
            return i;
        }
    }

    return 1;
}


int *selectionSort(int array[], int size)                // selection sort
{

    int indx = 0;
    for (int i = 0; i < size; i++) // sort whole array
    {
        printf("%i \n",array[i]); //debug

        int min = size+1;
        for(int j = i; j < size; j++) // locate minimum and assign it to variable
        {
            int num = array[j];
            if(num < min)
            {
                indx = j;
                min = array[j];
                printf("%i \n",array[j]); //debug

            }

        }

        int temp = array[i];
        array[i] = array [indx];
        array[indx] = temp;
         printf("%i \n",array[i]); // debug

    }
    return array;

}



int binarySearch(int array[])               // binary search
{

int num = get_int("what number : ");
int mid;
int min = 0;
int max=SIZE2;
do
{
    mid = (min+max)/2;
 //   printf("%i    %i \n", mid, array[mid]);
 //   char wait=get_char("wait1");
    if (num == array[mid])
    {
        return mid;
    }
    if(num < array[mid])
    {
       // printf("%i \n", mid);
 //       wait=get_char("wait2");
         max = mid;
    }
    else
    {
    min = mid;
    }
    }
    while( mid > 0 );
     printf("the binary index is %i \n", mid);

return 0;
}


void printArray(int sortArray[], int size)
{
    for (int i = 0; i < SIZE2; i++)
    {
        printf("%i \n",sortArray[i]);
    }

}



void writeArray(int sorted[], int size)
{
    string name = get_string("how do you want to call your file? ");
    char filename [6];
    sprintf(filename, "%s.txt", name);
    FILE *file = fopen(filename, "w");
    for( int i = 0; i < size; i++)
    {
        fprintf(file,"%d\n",sorted[i]);
    }
}

