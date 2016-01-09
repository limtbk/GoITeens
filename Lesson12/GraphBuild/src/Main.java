
import processing.core.*;

public class Main extends PApplet {

    public void setup() {
        size(800, 600);
        background(0);
    }

    double f(double x) {
        double y = java.lang.Math.sin(x);
        return y;
    }

    double df(double x) {
        double dx = 2.0/width;
        double y = (f(x + dx) - f(x)) / dx;
        return y;
    }

    public void draw() {
        stroke(128);

        line(0, height/2, width, height/2);
        line(width/2, 0, width/2, height);

        stroke(255);
        for (int xi = 0; xi < width; xi++) {
            double x = (((double)xi) / width) * 2 - 1;

            double y = f(x*2*PI); // Calc value of function
            double yp = df(x*2*PI); // Calc value of derivative function

            int yi = (int)(((y + 1) / 2) * height);
            int ypi = (int)(((yp + 1) / 2) * height);

            point(xi, height - yi - 1);
            point(xi, height - ypi - 1);
        }
    }

    public static void main(String[] args) {
        PApplet.main(new String[] {"Main"});
    }

}
