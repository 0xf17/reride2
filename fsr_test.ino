

int fsr_l = 0;
int fsr_r = 0;

int fsr_l_pin = A0;
int fsr_r_pin = A1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(fsr_l_pin,INPUT);
  pinMode(fsr_r_pin,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  fsr_l = analogRead(fsr_l_pin);
  fsr_r = analogRead(fsr_r_pin);

  Serial.println(fsr_l);
  Serial.println(fsr_r);
  delay(500);
}
