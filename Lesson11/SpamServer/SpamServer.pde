/**
 * Chat Server 
 * by Tom Igoe. 
 * 
 * Press the mouse to stop the server.
 */
 

import processing.net.*;

int port = 12345;
boolean myServerRunning = true;
int bgColor = 0;
int direction = 1;
int textLine = 60;

Server myServer;

void setup()
{
  size(1000, 400);
  textFont(createFont("SanSerif", 16));
  myServer = new Server(this, port); 
  background(0);
}

void mousePressed()
{
  // If the mouse clicked the myServer stops
  myServer.stop();
  myServerRunning = false;
}

void draw()
{
  if (myServerRunning == true)
  {
    text("server", 15, 45);
    Client thisClient = myServer.available();
    if (thisClient != null) {
      if (thisClient.available() > 0) {
        text("IP: " + thisClient.ip() + "> " + thisClient.readString(), 15, textLine);
        textLine = textLine + 35;
        if (textLine > 400) {
          textLine = 60;
          background(0);
        }
      }
    }
  } 
  else 
  {
    text("server", 15, 45);
    text("stopped", 15, 65);
  }
}
