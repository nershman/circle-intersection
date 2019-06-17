// my plans:
// take as input a text file which is outputted by my approximation alg, create vector of values for distance.
// use a loop to draw each circle at certaind distance from each other.
// both circles equidistant from center.

//this file is for intersection area = 1000. this is irrelevant for the most part.
float x;
float y;
float bx;
float by;
float xOffset = 0.0; 
float yOffset = 0.0; 
boolean pictaken = true;
int value = 1;
int q = 33; //the largest radius size. this information is in calculate.py
int n = 41; //the size of the array below
//THIS DATA IS CALCULATED FOR AN AREA OF 100.
float[] distnums = new float[] {40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0};

float[] radnums = new float[] {33.38268764160993, 32.95212916662234, 32.52289413870678, 32.09502337712562, 31.66821431874287, 31.243538601943342, 30.8200231275692, 30.39804656451623, 29.977673763137226, 29.558484233255115, 29.14193018028886, 28.72660004657869, 28.313244171930233, 27.901701265823156, 27.49210736198554, 27.084538975137836, 26.679063708391308, 26.27575858748284, 25.87470694609766, 25.47517850517819, 25.079685141463187, 24.6858909435454, 24.29470801994986, 23.90623578290854, 23.520569390624786, 23.136955630327265, 22.758121993567528, 22.381579498941495, 22.008323029254726, 21.637712395769377, 21.272216694385673, 20.90965553304685, 20.550967343479243, 20.1963038899849, 19.84583879615625, 19.499766539964046, 19.158262119429473, 18.821532162833225, 18.489782358396667, 18.163238499020146, 17.84212847449097};
//float r[] = 100;

int highlite= 0;
float m = 0;
//float zoom = 0.1;
float zoom = 50;
void setup (){
  size(1000,800);
  frameRate(10);
  background(100);
  colorMode(HSB);
  bx = width/2.0;
  by = height/2.0;
}
  
void draw(){  
//float zoom = (mouseX - 600)*0.1;

//zoom = zoom*1.01;
    rectMode(CENTER);
    fill(0,0,0,0);
    clear();
    
    for( int i = 0; i<n;i++){
      float hue = i*2.55 + m;
      while(hue > 255){hue = hue-255;}
   
      strokeWeight(0.5);
      stroke(hue,200,255);
//            if(i == highlite){stroke(hue,0,hue);      strokeWeight(2);}
//ellipse(mouseX, mouseY, 2.5*i, 2.5*i);
//ellipse(200, 300, 2.5*i, 2.5*i);
//ellipse(mouseX - 5*sin(m), mouseY + m, 3*i, 3*i);
//ellipse(mouseX, mouseY, 6*i, 6*i);


ellipse(bx - zoom*0.5*distnums[n-i-1], by, zoom*2*radnums[n-i-1], zoom*2*radnums[n-i-1]);
ellipse(bx + zoom*0.5*distnums[n-i-1], by, zoom*2*radnums[n-i-1], zoom*2*radnums[n-i-1]);
//ellipse(600 -40*sin(m/10), 400 + 40*cos(m/10), 6*i, 6*i);
    }
    
    if(m <= 255){m++;}
    else{m = 0;}
 if (pictaken == false){save("render.png"); pictaken = true;}
 pictaken=true;
}

void keyPressed()
{
  if(key == CODED)
  {
    if (keyCode == LEFT)
    {
      if (highlite > 0)    highlite--;
    }
    if(keyCode == RIGHT)
    {
      if (highlite<n)     highlite++;
    }
    
    if(keyCode == UP)
    {zoom = zoom*1.1;}
    
    if(keyCode == DOWN)
    {zoom = zoom/1.1;}
   
  }
}

void mousePressed() {
  xOffset = mouseX-bx; 
  yOffset = mouseY-by; 

}
void mouseDragged() {

    bx = mouseX-xOffset; 
    by = mouseY-yOffset; 
}


