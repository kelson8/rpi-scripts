#include <iostream>
#include <fstream>

#include <wiringPi.h>
#include <csignal>

// This seems to work now

// Write to file test
//
// Incomplete.
void writeToFile(std::string filename)
{
    //ofstream myfile;
    // Prevent this from being used for other types of files.
    //myfile.open(filename + ".txt");
//    myfile
}

// Read to file test
// This might work.
void readFile(std::string filename)
{
    std::string myText;
    std::ifstream file(filename + ".txt");

    while(getline(file, myText))
    {
    	std::cout << myText;
    }
    file.close();
}

// https://solarianprogrammer.com/2018/12/23/raspberry-pi-cpp-control-led/
// global flag used to exit from the main loop
bool RUNNING = true;

// Blink an LED
void blink_led(int led, int time) 
{
    digitalWrite(led, HIGH);
    delay(time);
    digitalWrite(led, LOW);
    delay(time);
}

bool green_led_state = false;

// My test code, idk if it'll work.
void toggle_led(int led)
{
   
   if(digitalRead(led) == HIGH) 
   {
   	digitalWrite(led, HIGH);
   }
   if(digitalRead(led) == LOW)
   {
   	digitalWrite(led, LOW);
   }



   // If the led state is true it'll turn on the led, if false it'll turn off.
// if(!green_led_state)
//   {
//	digitalWrite(led, HIGH);
//	green_led_state = true;
//   }
//   else
//   {
//	digitalWrite(led, LOW);
//	green_led_state = false;
//   }
//
}

// Callback handler if CTRL-C signal is detected
void my_handler(int s)
{
    std::cout << "Detected CTRL-C signal no. " << s << '\n';
    RUNNING = false;
}

int main()
{
// Move led test into test statement and disable it for a minute.

//   std::cout << "Hello world";
    readFile("Readme.txt");
#ifndef _TEST
//#define _TEST
#endif

#ifdef _TEST
    // Register a callback function to be called if the user presses CTRL-C
    std::signal(SIGINT, my_handler);

    // Initialize wiringPi and allow the use of BCM pin numbering
    wiringPiSetupGpio();

    std::cout << "Controlling the GPIO pins with wiringPi\n";

    // Define the 3 pins we are going to use
   int red = 17, yellow = 22, green = 16;

   // Setup the pins
     pinMode(red, OUTPUT);
     pinMode(yellow, OUTPUT);
     pinMode(green, OUTPUT);

     toggle_led(green);

    int time = 500;   // interval at which a pin is turned HIGH/LOW
//     while(RUNNING) {
//        blink_led(red, time);
//         blink_led(yellow, time);
//         blink_led(green, time);
//    }

     std::cout << "Program ended ...\n";
#endif //_TEST
}
