//PVector Null= new PVector(0,0);

PVector USmed(PVector US1, PVector US2, PVector obs1, PVector obs2) {

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

  void posicion(Barco barco) {

    this.barco= barco;

    if (this.us==0) {

      float alfa=atan(float(barco.alto)/-float(barco.ancho));
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

      float alfa=atan(float(barco.alto)/-float(barco.ancho));
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

      float alfa=atan(float(barco.ancho)/float(barco.alto));
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

      float alfa=atan(float(barco.ancho/2)/float(barco.alto));
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
      float alfa=atan(float(barco.ancho/2)/float(barco.alto));
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
      float alfa=atan(float(barco.ancho)/float(barco.alto));
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

      float alfa=atan(float(barco.alto)/-float(barco.ancho));
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

      float alfa=atan(float(barco.alto)/-float(barco.ancho));
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


  float cheak(obstaculo[] Obs) {

    PVector cheak= new PVector();
    
    float d= largo+1;
    for (int h=0; h<(Obs.length); h++) {
      for (int j=0; j<4; j++) {
        for (int i=0; i<4; i++) {
          cheak= USmed(this.pos, this.pos2, Obs[h].pts[i], Obs[h].pts[i+1]);

          if (cheak != null) { 
            fill(255,0,0);
            if (d>dist(this.pos.x, this.pos.y, cheak.x, cheak. y)) {
              d=dist(this.pos.x, this.pos.y, cheak.x, cheak. y);
              circle(cheak.x,cheak.y, 5);
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
