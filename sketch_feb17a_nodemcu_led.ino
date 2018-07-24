#include <Adafruit_SSD1306.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

#define OLED_RESET 0
Adafruit_SSD1306 display(OLED_RESET);

#define BLYNK_PRINT Serial    // Comment this out to disable prints and save space
#include <BlynkSimpleEsp8266.h>

// Select your pin with physical button
const int btnPin = 13;
WidgetLED led3(V1);

int ss = 0;

char auth[] = "<##blynk authen token##>";

const char* ssid = "<ssid name>";
const char* password = "<password>";
 
ESP8266WebServer server(80);   //instantiate server at port 80 (http port)
 
String page = "";
int LEDPin = 13;
int statusPin = 12;

void setup(void){

  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(1,3);
  display.print("NODEMCU - start");
  delay(10000);
  
  Blynk.begin(auth, "Mrolarik", "olarik_home");
  //the HTML of the web page
  page = "<h1>Simple NodeMCU Web Server</h1><p><a href=\"LEDOn\"><button>ON</button></a>&nbsp;<a href=\"LEDOff\"><button>OFF</button></a></p>";
  //make the LED pin output and initially turned off
  pinMode(LEDPin, OUTPUT);
  digitalWrite(LEDPin, LOW);

  pinMode(statusPin, OUTPUT);
  digitalWrite(statusPin, HIGH);

  pinMode(V3, INPUT);
   
  delay(1000);
  Serial.begin(115200);
  WiFi.begin(ssid, password); //begin WiFi connection
  Serial.println("");
 
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  for(int i=0; i<=3; i++){
    display.clearDisplay();
    ledDisplay("Connected to ",3,1);
    delay(1500);
    display.clearDisplay();
    ledDisplay(" ",3,1);
    delay(500);
  }
  showStatus();
  delay(1000);
   
  server.on("/", [](){
    server.send(200, "text/html", page);
  });
  server.on("/LEDOn", [](){
    server.send(200, "text/html", page);
    digitalWrite(LEDPin, HIGH);
    Serial.println("ON");
    display.clearDisplay();
    ledDisplay("Light - ON",3,1);
    led3.on();
    delay(5000);
    showStatus();
  });
  server.on("/LEDOff", [](){
    server.send(200, "text/html", page);
    digitalWrite(LEDPin, LOW);
    Serial.println("OFF");
    display.clearDisplay();
    ledDisplay("Light - OFF",3,1);
    led3.off();
    delay(5000);
    showStatus();
  });
  server.begin();
  Serial.println("Web server started!");

}

//To read data from Blynk app widgets
BLYNK_WRITE(V3)
{
  int pinValue = param.asInt(); // assigning incoming value from pin V1 to a variable
  //Serial.print("V3 Button value is: ");
  //Serial.println(pinValue);
  ledControl(pinValue);
  if(pinValue == 1){
    digitalWrite(LEDPin, HIGH);
  }
  else{
    digitalWrite(LEDPin, LOW);
  }
}

BLYNK_WRITE(V5)
{
  int pinValue = param.asInt(); // assigning incoming value from pin V1 to a variable
  Serial.print("V5 Slider value is: ");
  Serial.println(pinValue);
}

void ledDisplay(String text, int curRow, int curCol){
  display.setCursor(curCol, curRow);
  display.print(text); 
  display.display();
}

void showStatus(){
    display.clearDisplay();
    ledDisplay("Connecting",3,1);
    ledDisplay("IP address: ",13,1);
    ledDisplay(WiFi.localIP().toString(),23,1);
}

void ledControl(int onoff)
{
  if(onoff == 1){
    led3.on();
  }
  else{
    led3.off();
  }
}

void loop(void){
  server.handleClient();
  Blynk.run();  
}

