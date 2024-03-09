#include <iostream>
#include <ctime>

#define SIZE 128


int main(){
    srand(time(NULL));
    std::cout<<"Generator C++/"<<std::endl;
    for (size_t i=0;i<SIZE;++i){
        size_t bit= rand() % 2;
        std::cout<< bit;
    }
}