class Barco {

  int ancho;
  int alto;
  float timon;

  float vel=0.2;

  PVector pos= new PVector(width/2, height-300);
  float curso= 0;
  float cursoD;

  boolean choque = false;
  boolean llegada= false;

  float fitness=0;
  
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

  void display() {
    //muestro el barco
    //hay mucha trigonometrica y cosas para mostrarlo bien
    //confien en que esta bien
    if (this.choque == false) {
      push();

      translate(this.pos.x, this.pos.y);
      rotate(radians(-this.curso));

      noStroke();
      fill(180, 135, 11);
      rect(0-(this.ancho/2), 0-(this.alto/2), this.ancho, this.alto);

      fill(101, 166, 185);
      rect(0-(this.ancho/4), 0-(this.alto/2), this.ancho/2, this.alto/4);

      pop();
    }
  }

  //muevo el barco-------------------------------------------------------------------------------------------------------------------------------------------------------
  void move() {
    //si ya llego a la meta que se quede ahi
    if (llegada==true || this.pos.y<=0) {
      vel=0;
      return;
    }

    //si no choco hasta el momento
    if (this.choque == false) {
      //aca hago que el curso se mantenga entre valores de 0 a 360
      if (this.curso>=360) {
        this.curso=0;
      }
      if (this.curso<0) {
        this.curso=360+this.curso;
      }

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
  void update(obstaculo[] obs) {
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
    
    this.curso+= map(this.timon, -30,30, -0.15,0.15);

    //si no choco 
    if (this.choque==false) {
      //mido con los US y guardo los valores en la array de inputs
      for (int i=0; i<8; i++) {
        us[i].posicion(this);
        this.inputs[i]=map(us[i].cheak(obs), 0, 80, 0, 400);
      }
    }
    this.inputs[8]=this.curso;
    this.inputs[9]=cursoD;
    this.inputs[10]=this.timon;
  }
}
