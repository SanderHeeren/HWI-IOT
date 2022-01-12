// C++ code
//
#include<IRremote.h> // Include Infrarood remote module
const int irPin = 7; // Infrarood ontvanger op pin 2
IRrecv irrecv(irPin); // Pin koppelen aan de IR  
decode_results results; // Results van het ontvangst van de remote

const int ledPins[] = {5, 4, 3, 2}; // Meerdere Led pins in een array
const long int buttons[] = {16724175, 16718055, 16743045, // Codes voor de knoppen van die afstand bediening uit de Arduino kit (1 tot 9)
                            16716015, 16726215, 16726215,
                            16728765, 16730805, 16732845};

int count = 2; // Counter om het aantal clicks bij te houden
int led1 = 0, led2 = 0; // 2 leds om bij de houden welke er aan staan, en zodat er altijd 2 aan blijven
int ledState1 = LOW, ledState2 = LOW; // Status van de leds
long interval1 = 1000, interval2 = 800; // 2 Intervals zodat de 2 leds altijd op verschillende snelheden kunnen blinken
unsigned long previousMillis1 = 0, previousMillis2 = 0; // Vorige berekende snelheden die worden opgeslagen

void setup()
{
  Serial.begin(9600); // Aanzetten van de Serial monitor
  irrecv.enableIRIn(); // IR signalen kunnen ontvangen aanzetten
  
  pinMode (ledPins[0], OUTPUT); // Leds koppelen aan pins op basis van array positie
  pinMode (ledPins[1], OUTPUT);
  pinMode (ledPins[2], OUTPUT);
  pinMode (ledPins[3], OUTPUT);
  
  led1 = ledPins[2]; // 2 leds koppelen zodat er al 2 aan staan bij het opstarten
  led2 = ledPins[3];
}

void loop()
{
  if(irrecv.decode(&results)){ // Als er een signaal wordt ontvangen
    irrecv.resume();
    long int result = results.value; // Haal het resultaat op wat wordt gestuurd
    Serial.println(results.value);  // Print resultaat in de monitor
    
    if(count % 2 == 0){ // Op de eerste click kan een led worden aangezet
      if(result == buttons[0] && digitalRead(ledPins[0]) == LOW){ // Als knop 1 wordt ingedrukt en led 1 staat uit voor dan de methode uit
        Response(ledPins[0]); // Stuur het nummer van de led mee
      }else if(result == buttons[1] && digitalRead(ledPins[1]) == LOW){
        Response(ledPins[1]);
      }else if(result == buttons[2] && digitalRead(ledPins[2]) == LOW){
        Response(ledPins[2]);
      }else if(result == buttons[3] && digitalRead(ledPins[3]) == LOW){
        Response(ledPins[3]);
      } // Else op de tweede click om snelheid toe te voegen
    } else if (result == buttons[0]) { // Als knop 1 dan stuur een snelheid van 100 milliseconden
      Blinkspeed(100);
    } else if (result == buttons[1]) { // Als knop 2 dan stuur een snelheid van 200 milliseconden
      Blinkspeed(200);
    } else if (result == buttons[2]) {
      Blinkspeed(300);
    } else if (result == buttons[3]) {
      Blinkspeed(400);
    } else if (result == buttons[4]) {
      Blinkspeed(500);
    } else if (result == buttons[5]) {
      Blinkspeed(600);
    } else if (result == buttons[6]) {
      Blinkspeed(700);
    } else if (result == buttons[7]) {
      Blinkspeed(800);
    } else if (result == buttons[8]) {
      Blinkspeed(900);
    } 
  }
  
  unsigned long currentMillis = millis(); // Huidige tijd van hoe lang de Arduino aanstaat

  if (currentMillis - previousMillis1 >= interval1) { // voor deze code uit op basis van de interval snelheid die wordt meegegeven
    previousMillis1 = currentMillis; // Zet de huidige vorige om naar de huidige

    if (ledState1 == LOW) { // LedState steeds Low en High in een loop die wordt uitgevoerd op basis van de snelheid van de interval
      ledState1 = HIGH;
    } else {
      ledState1 = LOW;
    }

    digitalWrite(led1, ledState1); // Verander de status van de led1
  }
  
  if (currentMillis - previousMillis2 >= interval2) { // voor deze code uit op basis van de interval snelheid die wordt meegegeven
    previousMillis2 = currentMillis; // Zet de huidige vorige om naar de huidige

    if (ledState2 == LOW) { // LedState steeds Low en High in een loop die wordt uitgevoerd op basis van de snelheid van de interval
      ledState2 = HIGH;
    } else {
      ledState2 = LOW;
    }

    digitalWrite(led2, ledState2); // Verander de status van de led2
  }
}

void Blinkspeed(int blinkspeed){
    interval1 = blinkspeed; // Interval1 wordt aangepast naar de meegegeven snelheid
    count++; // Telt de count voor de klik volgorde
}

void Response(int LED){
    digitalWrite(led2, LOW); // De laatst aangepaste led wordt uitgezet
    led2 = led1; // Led1 wordt led2 om de volgorde aan te houden 
    led1 = LED; // Led1 gaat aan voor de laatst gekozen input
    digitalWrite(led1, HIGH); // Beide leds gaat aan
    digitalWrite(led2, HIGH);
    interval2 = interval1; // Interval1 wordt Interval2 om de volgorde aan te houden, en om de blinksnelheid bij de juiste led te houden
    interval1 = 1000; // Tijdelijke nieuwe interval tot er een wordt gekozen met de tweede klik op de afstandsbediening
    count++; // Telt de count voor de klik volgorde
}
