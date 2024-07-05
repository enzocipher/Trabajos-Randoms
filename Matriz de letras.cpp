#include <iostream>
#include <cstdlib>
#include <time.h>
#include <cctype>
#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <conio.h>
#include <iomanip>
#include <locale.h>
using namespace std;

struct letras{
    bool esconsonante;
    char contenido;
};

int main()
{
    char decision ='n';
    //No sé si sirva, lo hice en celular pero en celular esta lib no funciona
    setlocale(LC_CTYPE,"spanish");
    //Estas son las letras
    string vocales = "aeiou";
    string todas = "abcdefghijklmnñoprqstuvxyz";
    srand(time(NULL));
    string eleccion;
    //definir el arreglo bi
    letras letra[10][10];
    cout << "Inserte 3 consonantes seguidas sin espacios ni comas" << endl;
    //Uh esto verifica si lo ingresado es lo que se pide, debería ser una función pero soy muy flojo
    while (true)
    {
     getline(cin, eleccion); 
     for (int i=0; i<3; i++){eleccion[i] = tolower(eleccion[i]);};
     if(eleccion.length() == 3 )
     {
      bool variable = true;
      for (int i=0; i<3; i++){
          for (int j=0; j<5; j++){
              if (eleccion[i] == vocales[j] || isalpha(eleccion[i]) == false){variable = false; break; break;}
          }
      }
      if (variable == true){break;};
     } 
     cout << "Ingrese correctamente\n";
    }
    //definicion de los contadores... no deberían estar ahí 
    int contador=0;
    int contador2=0;
    int contador3=0;
    cout << "seran: " << eleccion[0] << ", " << eleccion[1] << ", " << eleccion[2] << endl;
    //ciclo del script
    while (true)
    {
        cout << setw(40) << setfill('_');
        cout << "\n";
        for (int i=0; i<10; i++)
        {
            // relleno de cada espacio dentro del array y si es consonante
            for (int j=0; j<10; j++)
            {
                int random = 0+rand()%26;
                letra[i][j].contenido=todas[random];
                cout << "[" << letra[i][j].contenido << "] ";  if (j==9){cout << endl;};
                for(int k=0; k<5; k++)
                //Podrias hacer una funcion isvowel y funcionaria, pero solo estoy usando main
                { 
                    if(letra[i][j].contenido == vocales[k])
                    {
                        letra[i][j].esconsonante=false; break;
                    } 
                    else 
                    {
                     letra[i][j].esconsonante=true;
                    };
                };
                //pues estaba dentro del for, así que lo puse aca...
                if(letra[i][j].esconsonante == true){contador++;}
            };
            //suma de los otros contadores
            for (int j=0; j<8; j++) //solo hasta 8 para evitar llamar a los falsos como array[11]
            {
               if (letra[i][j].esconsonante == true && letra[i][j+1].esconsonante ==true && letra[i][j+2].esconsonante == true)
               {
                if (letra[i][j].contenido == eleccion[0] && letra[i][j+1].contenido == eleccion[1] && letra[i][j+2].contenido == eleccion[2])
                {
                        contador2++;
                };
                contador3++;
               };
            };
        };
        cout << setw(40) << setfill('_');
        cout << "\n";
        cout << "El contador de consonantes es de: " << contador << endl;
        cout << "El contador de las consonantes elegidas en linea (La probabilidad es muy baja): \n" << contador2 << endl;
        cout << "El contador de consonantes en linea es de: " << contador3 << endl;
        cout << setw(40) << setfill('_');
        cout << "\n";
        cout << "otra vez?\ny = si\notro = terminar ejecución" << endl;
        //agarrar solo una letra y continuar con el ciclo 
        decision =getch();
        if (toupper(decision)!= 'Y'){break;}
        // redefinición, luego lo haré función... que flojera
        contador=0;
        contador2=0;
        contador3=0;
    }
}