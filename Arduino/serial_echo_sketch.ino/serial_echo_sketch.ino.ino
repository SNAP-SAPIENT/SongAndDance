//int incomingByte = 0; 
int power;
String id;

void setup()
{
  Serial.begin(9600);
}
void loop()
{
  if(Serial.available() > 0)
  {
    // read the incoming bytes
   // incomingByte = Serial.read();
 
    // echo back
   // Serial.print((char)incomingByte);

    id = Serial.readStringUntil(':');
    power = Serial.parseInt();
    Serial.print(id.toInt(),DEC);
    Serial.println(power,DEC);    
  }
}
