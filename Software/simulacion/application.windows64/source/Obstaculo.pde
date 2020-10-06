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

  void display() {

    stroke(200, 100);
    fill(160, 150, 0);
    rect(this.x, this.y, this.ancho, this.alto);
  }
}
