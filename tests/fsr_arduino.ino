/**
.. module:: test/fsr_arduino
   : platform:
   : synopsis: test fsrs on arduino

.. moduleauthor:: @anchitsh96

**/
int fsr_l = 0;
int fsr_r = 0;

int fsr_r_pin = A1;
int fsr_l_pin = A2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(fsr_r_pin, INPUT);
  pinMode(fsr_l_pin, INPUT);
}

void loop() {
  fsr_r = analogRead(fsr_r_pin);
  fsr_l = analogRead(fsr_l_pin);

  Serial.print(fsr_l);
  Serial.print(",");
  Serial.println(fsr_r);
  delay(500);
}
