import processing.net.*;

Client client;

void setup() 
{
  frameRate(5);
  client = new Client(this, "127.0.0.1", 12345);
  client.write("Pysch pysch ololo\n");
}

void draw() 
{
  if (client.available() > 0) {
    String input = client.readString();
    print(input);
  }

}

