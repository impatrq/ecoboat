import controlP5.*;

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

void setup() {
  size(800, 750);

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

void draw() {

  background(101, 166, 185);

  fill(255, 0, 0);
  circle(meta.x, meta.y, 10);
  
  if (mostrarO==true){
    for (int i=0; i<obsT; i++) {
      obs[i].display();
    }
  }

  barco.timon=timon;
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

void keyPressed() {
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

void guardar() {
  for (int j = 0; j < barco.inputs.length; j++) {
    JSONObject temp2 = new JSONObject();
    temp2.setFloat("id", barco.inputs[j]);
    values.setJSONObject(j+ (i*barco.inputs.length), temp2);
  }
  i+=1;
}

void nextgen() {
  timon=0;
  cp5.addSlider("timon", -30, 30, 0, 20, height-100, 200, 30);
  barco= new Barco(36, 56);
  for (int i=0; i<obsT; i++) {
    obs[i]=new obstaculo((width/2)-80+random(160), 
      random(100, (height-250)/2), 
      40, int(random(10, 50)));
  }
}
