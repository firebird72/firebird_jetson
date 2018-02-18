byte PWM_PIN = 3;
 
int pwm_value;
 
void setup() {
  pinMode(PWM_PIN, INPUT);
  pinMode(7, OUTPUT);
  Serial.begin(115200);
}
 
void loop() {
  pwm_value = pulseIn(PWM_PIN, HIGH);
  Serial.println(pwm_value);
  
  if(pwm_value < 1200) {
    digitalWrite(7, HIGH);
    Serial.println(pwm_value);
    //Serial.println("KILL");
   //Serial.println("00000000000000000010000");
  }
 
}
