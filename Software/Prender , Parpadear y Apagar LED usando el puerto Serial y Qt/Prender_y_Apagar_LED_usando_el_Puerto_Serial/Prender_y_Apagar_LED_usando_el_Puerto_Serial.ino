int led = 4;
int val = 0;
void setup() {
 pinMode  (led , OUTPUT); 
 Serial.begin (9600);
}

void loop() {
   
    
    
}
void serialEvent(){
   if (Serial.available()){
      val = Serial.parseInt(); //Aca convertimos lo que nos llege del serial a entero
    if (val == 1){
      digitalWrite (led, HIGH);
      }
    if (val == 2){
      digitalWrite (led,LOW);
      }  
    if (val == 3){
      while (true) {
      digitalWrite (led, HIGH);
      delay (1000);
      digitalWrite (led,LOW);
      delay (1000);
       }
      }
  
  }
}
