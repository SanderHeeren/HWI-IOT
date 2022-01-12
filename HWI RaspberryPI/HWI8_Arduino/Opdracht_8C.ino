int led1 = 0, led2 = 0; // 2 leds om bij de houden welke er aan staan, en zodat er altijd 2 aan blijven

const int ledPins[] = {6, 7}; // Meerdere Led pins in een array
int input3 = 3;
int input2 = 2;
int KNOP = 4;
int State3 = LOW;
int State2 = LOW;

void setup() {
  pinMode (ledPins[0], OUTPUT); // Leds koppelen aan pins op basis van array positie
  pinMode (ledPins[1], OUTPUT);
  pinMode (input3, INPUT);
  pinMode (input2, INPUT);
  pinMode(KNOP, INPUT);

  led1 = ledPins[0]; // 2 leds koppelen zodat er al 2 aan staan bij het opstarten
  led2 = ledPins[1];
}

void loop() {
  int buttenState = digitalRead(KNOP);
  State3 = digitalRead(input3);
  State2 = digitalRead(input2);

  if (buttenState == HIGH){
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    delay(1000);
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    delay(1000);
  }else{
    if (State3 == HIGH) 
    {
      digitalWrite(led1, HIGH);
    }else{
      digitalWrite(led1, LOW);
    }
    if (State2 == HIGH) 
    {
      digitalWrite(led2, HIGH);
    }else{
      digitalWrite(led2, LOW);
    }
  }
}
