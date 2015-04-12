#include <Bridge.h>

Process p;
#define BUF_SIZE 32
char buf[BUF_SIZE];

void setup() {
  Serial.begin(115200);
  // Start the bridge
  Bridge.begin();
  // Start the modbus server
  p.begin("python");
  p.addParameter("/mnt/sd/modbus_tcp_slave.py"); // modbus float holding registers
  p.addParameter("40001");                       // read only start address
  p.addParameter("6");                           // read only number of holding registers
  p.addParameter("40101");                       // read/write start address (optional)
  p.addParameter("6");                           // read/write number of holding registers (optional)
  p.runAsynchronously();
}
void loop() {
  // AVR -> WRT (modbus read only), write some values to the modbus server
  Bridge.put("40001", String(PI));
  Bridge.put("40003", String(millis()));
  Bridge.put("40005", String(5280));

  // AVR <- WRT (modbus read/write), read some values from the modbus server
  Bridge.get("40101", buf, BUF_SIZE);
  Serial.println(atof(buf));
  delay(500);
}
