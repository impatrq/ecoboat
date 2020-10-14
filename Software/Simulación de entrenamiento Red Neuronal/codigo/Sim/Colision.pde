float hip(float a, float b) {

  float a2=pow(a, 2);
  float b2=pow(b, 2);
  float c= sqrt(a2+b2);
  return c;
}

boolean intersec(PVector barco1, PVector barco2, PVector obs1, PVector obs2) {

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

  void Hitbox(Barco Barco) {

    //calculo las 4 esquinas 

    float beta=atan(float(Barco.alto)/float(Barco.ancho));
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

  boolean colision(obstaculo[] Obs) {

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
