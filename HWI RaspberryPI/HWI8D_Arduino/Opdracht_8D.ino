int ledState1 = LOW, ledState2 = LOW; // Status van de leds
unsigned long previousMillis1 = 0, previousMillis2 = 0; // Vorige berekende snelheden die worden opgeslagen 

int input3 = 3;
int input2 = 2;

void setup() {
  pinMode (input3, OUTPUT);
  pinMode (input2, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  unsigned long currentMillis = millis(); // Huidige tijd van hoe lang de Arduino aanstaat 
  Serial.print(ledState1);
  Serial.print(ledState2);

  if (currentMillis - previousMillis1 >= 1000) { // voor deze code uit op basis van de interval snelheid die wordt meegegeven
    previousMillis1 = currentMillis; // Zet de huidige vorige om naar de huidige
    
    if (ledState1 == LOW) { // LedState steeds Low en High in een loop die wordt uitgevoerd op basis van de snelheid van de interval
      ledState1 = HIGH;
    } else {
      ledState1 = LOW;
    }
    digitalWrite(input2, ledState1);
  }
  if (currentMillis - previousMillis2 >= 3000) { // voor deze code uit op basis van de interval snelheid die wordt meegegeven
    previousMillis2 = currentMillis; // Zet de huidige vorige om naar de huidige
    
    if (ledState2 == LOW) { // LedState steeds Low en High in een loop die wordt uitgevoerd op basis van de snelheid van de interval
      ledState2 = HIGH;
    } else {
      ledState2 = LOW;
    }
    digitalWrite(input3, ledState2); // Verander de status van de led2
  }
}
