import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import controlP5.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class Sim extends PApplet {



boolean mostrarO= false;

JSONObject json= new JSONObject();
JSONArray values;
int i=0;
//numero de obstaculos, numero de barcos 
int obsT=3;
int gen=0;

float timon=0;

ControlP5 cp5;

obstaculo[] obs= new obstaculo[obsT];
Barco barco;
hitbox hitbox= new hitbox();

//creo un punto que es la meta
PVector meta;

public void setup() {
  

  values = new JSONArray();
  cp5 = new ControlP5(this);
  //fullScreen();
  //lleno la array de obstaculos con obstaculos aleatorios
  nextgen();
  meta= new PVector(width/2, 10);
  JSONObject test= new JSONObject();
  int x=0;
  while (true) {
    try {
      test = loadJSONObject("new.json("+x+")");
    } 
    catch (NullPointerException e) {
      //e.printStackTrace();
      break;
    }
    x++;
  }
  gen= x;
}

public void draw() {

  background(101, 166, 185);

  fill(255, 0, 0);
  circle(meta.x, meta.y, 10);
  
  if (mostrarO==true){
    for (int i=0; i<obsT; i++) {
      obs[i].display();
    }
  }

  barco.timon=timon;
  stroke(10);
  line(barco.pos.x, barco.pos.y, meta.x, meta.y);
  barco.display();
  barco.move();
  barco.update(obs);
  hitbox.Hitbox(barco);
  barco.choque=hitbox.colision(obs);  

  if ((frameCount%60==0 && frameCount>=180)) {
    guardar();
  }
  if (barco.choque==true) {  
    nextgen();
  }

  if (barco.llegada==true) {
    json.setJSONArray("valores", values);
    saveJSONObject(json, "data/new.json("+gen+")");
    gen++;
    nextgen();
    i=0;
  }
}

public void keyPressed() {
  if (key=='c') {  
    timon=0;
    cp5.addSlider("timon", -30, 30, 0, 20, height-100, 200, 30);
  }
  if (key=='m'){
    if (mostrarO){
      mostrarO=false;
    }
    else{
      mostrarO=true;
    }
  }
}

public void guardar() {
  
  for (int j = 0; j < barco.inputs.length; j++) {
    JSONObject temp2 = new JSONObject();
    temp2.setFloat("id", barco.inputs[j]);
    values.setJSONObject(j+ (i*barco.inputs.length), temp2);
  }
  i+=1;
}

public void nextgen() {
  timon=0;
  cp5.addSlider("timon", -30, 30, 0, 20, height-100, 200, 30);
  barco= new Barco(36, 56);
  for (int i=0; i<obsT; i++) {
    obs[i]=new obstaculo((width/2)-80+random(160), 
      random(100, (height-250)/2), 
      40, PApplet.parseInt(random(10, 50)));
  }
}
class Barco {

  int ancho;
  int alto;
  float timon;

  float vel=0.2f;

  PVector pos= new PVector(width/2, height-300);
  float curso= 0;
  float cursoD;

  boolean choque = false;
  boolean llegada= false;

  float fitness=0;
    
  float delta= random(-90,90);
  
  float[] inputs= new float[11];

  //le doy 8 US en una array
  US[] us= new US[8];

  //constructor del objeto
  Barco(int ancho, int alto) {
    this.ancho=ancho;
    this.alto=alto;
    //inicio los US en las 8 posiciones
    for (int i=0; i<8; i++) {
      us[i]=new US(i);
    }
  }

  public void display() {
    //muestro el barco
    //hay mucha trigonometrica y cosas para mostrarlo bien
    //confien en que esta bien
    if (this.choque == false) {
      push();

      translate(this.pos.x, this.pos.y);
      rotate(radians(-this.curso));
      
      stroke(10);
      line(0, 0, 0, -this.alto);
      
      noStroke();
                 
      fill(180, 135, 11);
      rect(0-(this.ancho/2), 0-(this.alto/2), this.ancho, this.alto);

      fill(101, 166, 185);
      rect(0-(this.ancho/4), 0-(this.alto/2), this.ancho/2, this.alto/4);
      
      pop();
      
    }
  }

  //muevo el barco-------------------------------------------------------------------------------------------------------------------------------------------------------
  public void move() {
    //si ya llego a la meta que se quede ahi
    if (llegada==true || this.pos.y<=0) {
      vel=0;
      return;
    }

    //si no choco hasta el momento
    if (this.choque == false) {
      //aca hago que el curso se mantenga entre valores de 0 a 360
      this.curso=constrain(this.curso);

      //lo muevo segun su vel y curso
      //mas trigonometria
      this.pos.x=this.pos.x-sin(radians(this.curso))*this.vel;
      this.pos.y=this.pos.y-cos(radians(this.curso))*this.vel;

      //si choco le bajo la vel a 0
    } else {
      this.vel= 0;
    }
  }

  //actualizo al barquito -----------------------------------------------------------------------------------------------------------------------------
  public void update(obstaculo[] obs) {
    //primero me fijo se ya llego

    float d= dist(this.pos.x, this.pos.y, meta.x, meta.y);
    //en ese caso pongo el flag en rue
    if (d<20) {
      this.llegada=true;
    }
    //aca calculo el curso deseado con mas trignometria
    cursoD= (atan((this.pos.x-meta.x)/(this.pos.y-meta.y)))*180/PI;

    //normalizo el valor del curso deseado a valore positivos
    if (this.cursoD<0) {
      this.cursoD=360+this.cursoD;
    } 
    
    this.curso+= map(this.timon, -30,30, 0.15f,-0.15f);

    //si no choco 
    if (this.choque==false) {
      //mido con los US y guardo los valores en la array de inputs
      for (int i=0; i<8; i++) {
        us[i].posicion(this);
        this.inputs[i]=map(us[i].cheak(obs), 0, 80, 0, 400);
      }
    }
    this.inputs[8]=constrain(this.curso+ this.delta);
    this.inputs[9]=constrain(cursoD+ this.delta);
    this.inputs[10]=this.timon;
  }
}

public float constrain(float num){
  if (num>=360) {
    num=num-360;
  }
  else if (num<0) {
    num=360+num;
  }
  return num;
} 
public float hip(float a, float b) {

  float a2=pow(a, 2);
  float b2=pow(b, 2);
  float c= sqrt(a2+b2);
  return c;
}

public boolean intersec(PVector barco1, PVector barco2, PVector obs1, PVector obs2) {

  float x1=barco1.x;
  float y1=barco1.y;
  float x2=barco2.x;
  float y2=barco2.y;

  float x3=obs1.x;
  float y3=obs1.y;
  float x4=obs2.x;
  float y4=obs2.y;

  float den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4);
  if (den==0) {    
    return false;
  }
  float t=((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den;
  float u=-((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den;

  //PVector pt= new PVector(x1+t*(x2-x1), y1+t*(y2-y1));

  if ((t<=1) && (t>=0) && (u<=1) && (u>=0)) {
    return true;
  } else {
    return false;
  }
}

class hitbox {

  PVector[] pts= new PVector[5];
  PVector  p1= new PVector();
  PVector  p4= new PVector();
  PVector  p2= new PVector(); 
  PVector  p3= new PVector();
  hitbox() {
  }

  public void Hitbox(Barco Barco) {

    //calculo las 4 esquinas 

    float beta=atan(PApplet.parseFloat(Barco.alto)/PApplet.parseFloat(Barco.ancho));
    float alfa=(-Barco.curso)*PI/180 + beta;
    float c=hip(Barco.ancho/2, Barco.alto/2);

    float deltax=(cos(alfa)) * c;
    float deltay=(sin(alfa)) * c;

    this.p1.x=Barco.pos.x-deltax;         
    this.p1.y=Barco.pos.y-deltay;
    this.p3.x=Barco.pos.x+deltax;        
    this.p3.y=Barco.pos.y+deltay;

    alfa=(-Barco.curso)*PI/180 -beta;

    deltax=(cos(alfa)) * c;
    deltay=(sin(alfa)) * c;

    this.p2.x=Barco.pos.x-deltax;         
    this.p2.y=Barco.pos.y-deltay;
    this.p4.x=Barco.pos.x+deltax;        
    this.p4.y=Barco.pos.y+deltay;

    //guardo en puntos
    this.pts[0]=p1;
    this.pts[1]=p2;
    this.pts[2]=p3;
    this.pts[3]=p4;
    this.pts[4]=p1;
  }

  public boolean colision(obstaculo[] Obs) {

    int Chek=0;

    for (int h=0; h<(Obs.length); h++) {
      for (int j=0; j<4; j++) {
        for (int i=0; i<4; i++) {
          boolean chek=intersec(this.pts[j], this.pts[j+1], Obs[h].pts[i], Obs[h].pts[i+1]);
          if (chek==true) {
            Chek+=1;
          }
        }
      }
    }
    if (Chek>=1) {
      return true;
    } else {
      return false;
    }
  }
}
class obstaculo {

  float x;
  float y;
  int ancho;
  int alto;
  PVector[] pts= new PVector[5];

  obstaculo(float x, float y, int ancho, int alto) {
    this.x=x;
    this.y=y;
    this.ancho=ancho;
    this.alto=alto;
    
    this.pts[0]= new PVector(x, y);
    this.pts[1]= new PVector(x, y+ this.alto);
    this.pts[2]= new PVector(x +this.ancho, y +this.alto);
    this.pts[3]= new PVector(x +this.ancho, y);
    this.pts[4]= new PVector(x, y);
  }

  public void display() {

    stroke(200, 100);
    fill(160, 150, 0);
    rect(this.x, this.y, this.ancho, this.alto);
  }
}
//PVector Null= new PVector(0,0);

public PVector USmed(PVector US1, PVector US2, PVector obs1, PVector obs2) {

  float x1=US1.x;
  float y1=US1.y;
  float x2=US2.x;
  float y2=US2.y;

  float x3=obs1.x;
  float y3=obs1.y;
  float x4=obs2.x;
  float y4=obs2.y;

  float den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4);
  if (den==0) {    
    return null;
  }
  float t=((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den;
  float u=-((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den;

  PVector pt= new PVector(x1+t*(x2-x1), y1+t*(y2-y1));

  if ((t<=1) && (t>=0) && (u<=1) && (u>=0)) {
    return pt;
  } else {
    return null;
  }
}

class US {

  float largo=80;
  float dir;
  PVector dist= new PVector();
  PVector pt= new PVector();
  PVector pos= new PVector();
  PVector pos2= new PVector();
  int us;


  Barco barco;

  US(int us) {
    this.us= us;
  }

  public void posicion(Barco barco) {

    this.barco= barco;

    if (this.us==0) {

      float alfa=atan(PApplet.parseFloat(barco.alto)/-PApplet.parseFloat(barco.ancho));
      float beta=((-barco.curso)*PI/180)-alfa;
      float c=hip(barco.alto/4, barco.ancho/2);

      float deltax=(sin(beta)) *c ;
      float deltay=(cos(beta)) *c ;

      this.pos.x=barco.pos.x-deltax;
      this.pos.y=barco.pos.y+deltay;

      deltax=(cos((-barco.curso)*PI/180))*largo ;
      deltay=(sin((-barco.curso)*PI/180))*largo ;

      this.pos2.x=pos.x-deltax;
      this.pos2.y=pos.y-deltay;
    }

    if (this.us==1) {

      float alfa=atan(PApplet.parseFloat(barco.alto)/-PApplet.parseFloat(barco.ancho));
      float beta=((barco.curso)*PI/180)-alfa;
      float c=hip(barco.alto/4, barco.ancho/2);

      float deltax=(sin(beta)) *c ;
      float deltay=(cos(beta)) *c ;

      this.pos.x=barco.pos.x-deltax;
      this.pos.y=barco.pos.y-deltay;

      deltax=(cos((-barco.curso)*PI/180))*largo ;
      deltay=(sin((-barco.curso)*PI/180))*largo ;

      this.pos2.x=pos.x-deltax;
      this.pos2.y=pos.y-deltay;
    }

    if (this.us==2) {

      float alfa=atan(PApplet.parseFloat(barco.ancho)/PApplet.parseFloat(barco.alto));
      float beta=((-barco.curso)*PI/180)-alfa;
      float c=hip(barco.alto/2, barco.ancho/2);

      float deltax=(sin(beta)) *c ;
      float deltay=(cos(beta)) *c ;

      this.pos.x=barco.pos.x+deltax;
      this.pos.y=barco.pos.y-deltay;

      deltax=(sin((barco.curso+45)*PI/180))*largo ;
      deltay=(cos((barco.curso+45)*PI/180))*(largo) ;

      this.pos2.x=pos.x-deltax;
      this.pos2.y=pos.y-deltay;
    }

    if (this.us==3) {

      float alfa=atan(PApplet.parseFloat(barco.ancho/2)/PApplet.parseFloat(barco.alto));
      float beta=((-barco.curso)*PI/180)-alfa;
      float c=hip(barco.alto/2, barco.ancho/4);

      float deltax=(sin(beta)) *c ;
      float deltay=(cos(beta)) *c ;

      this.pos.x=barco.pos.x+deltax;
      this.pos.y=barco.pos.y-deltay;

      deltax=(sin((barco.curso)*PI/180))*(largo) ;
      deltay=(cos((barco.curso)*PI/180))*(largo) ;

      this.pos2.x=pos.x-deltax;
      this.pos2.y=pos.y-deltay;
    }
    if (this.us==4) {
      float alfa=atan(PApplet.parseFloat(barco.ancho/2)/PApplet.parseFloat(barco.alto));
      float beta=((barco.curso)*PI/180)-alfa;
      float c=hip(barco.alto/2, barco.ancho/4);

      float deltax=(sin(beta)) *c ;
      float deltay=(cos(beta)) *c ;

      this.pos.x=barco.pos.x-deltax;
      this.pos.y=barco.pos.y-deltay;

      deltax=(sin((barco.curso)*PI/180))*(largo) ;
      deltay=(cos((barco.curso)*PI/180))*(largo) ;

      this.pos2.x=pos.x-deltax;
      this.pos2.y=pos.y-deltay;
    }
    if (this.us==5) {
      float alfa=atan(PApplet.parseFloat(barco.ancho)/PApplet.parseFloat(barco.alto));
      float beta=((barco.curso)*PI/180)-alfa;
      float c=hip(barco.alto/2, barco.ancho/2);

      float deltax=(sin(beta)) *c ;
      float deltay=(cos(beta)) *c ;

      this.pos.x=barco.pos.x-deltax;
      this.pos.y=barco.pos.y-deltay;

      deltax=(sin((-barco.curso+45)*PI/180))*(largo) ;
      deltay=(cos((-barco.curso+45)*PI/180))*(largo) ;

      this.pos2.x=pos.x+deltax;
      this.pos2.y=pos.y-deltay;
    }
    if (this.us==6) {

      float alfa=atan(PApplet.parseFloat(barco.alto)/-PApplet.parseFloat(barco.ancho));
      float beta=((barco.curso)*PI/180)+alfa;
      float c=hip(barco.alto/4, barco.ancho/2);

      float deltax=(sin(beta)) *c ;
      float deltay=(cos(beta)) *c ;

      this.pos.x=barco.pos.x-deltax;
      this.pos.y=barco.pos.y-deltay;

      deltax=(cos((-barco.curso)*PI/180))*largo ;
      deltay=(sin((-barco.curso)*PI/180))*largo ;

      this.pos2.x=pos.x+deltax;
      this.pos2.y=pos.y+deltay;
    }

    if (this.us==7) {

      float alfa=atan(PApplet.parseFloat(barco.alto)/-PApplet.parseFloat(barco.ancho));
      float beta=-((barco.curso)*PI/180)+alfa;
      float c=hip(barco.alto/4, barco.ancho/2);

      float deltax=(sin(beta)) *c ;
      float deltay=(cos(beta)) *c ;

      this.pos.x=barco.pos.x-deltax;
      this.pos.y=barco.pos.y+deltay;

      deltax=(cos((-barco.curso)*PI/180))*largo ;
      deltay=(sin((-barco.curso)*PI/180))*largo ;

      this.pos2.x=pos.x+deltax;
      this.pos2.y=pos.y+deltay;
    }
  }


  public float cheak(obstaculo[] Obs) {

    PVector cheak= new PVector();
    
    float d= largo+1;
    for (int h=0; h<(Obs.length); h++) {
      for (int j=0; j<4; j++) {
        for (int i=0; i<4; i++) {
          cheak= USmed(this.pos, this.pos2, Obs[h].pts[i], Obs[h].pts[i+1]);

          if (cheak != null) { 
            fill(255,0,0);
            circle(cheak.x,cheak.y, 5);
            if (d>dist(this.pos.x, this.pos.y, cheak.x, cheak. y)) {
              d=dist(this.pos.x, this.pos.y, cheak.x, cheak. y);
            }
          }
        }
      }
    }
    if (d !=largo+1) {
      return d;
    } else {
      return largo;
    }
  }
}
  public void settings() {  size(800, 750); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Sim" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
