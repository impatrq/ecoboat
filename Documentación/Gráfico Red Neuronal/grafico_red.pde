int altoI=110;

void setup() {
  fullScreen();
}

void draw() {
  background(51);

  textSize(30);
  text("Entradas", 160, 50);

  for (int i=0; i<10; i++) {
    textSize(20);
    if (i<8) {
      text("Sensor "+i, 150, altoI+5+(i*70));
    }
    if (i==8) {
      text("Curso Actual", 130, altoI+5+(i*70));
    }
    if (i==9) {
      text("Curso Deseado", 120, altoI+5+(i*70));
    }

    for (int j=0; j<8; j++) { 
      stroke(5);
      strokeWeight(2);
      line(300, altoI+(i*70), 650, 180+(j*70));
      if (i==9) {
        for (int h=0; h<8; h++) { 
          stroke(5);
          strokeWeight(2);
          line(650, 180+(j*70), 950, 180+(h*70));
          if (i==9) {
            for (int k=0; k<8; k++) { 
              stroke(5);
              strokeWeight(2);
              line(950, 180+(k*70), 1300, 425);

              fill(200);
              noStroke();
              circle(950, 180+(k*70), 50);
            }
          }
        }
        fill(200);
        noStroke();
        circle(650, 180+(j*70), 50);
      }
    }

    fill(200);
    noStroke();
    circle(300, altoI+(i*70), 50);
  }

  textSize(20);
  text("Timón", 1350, 425);
  noStroke();
  circle(1300, 425, 50);
  textSize(30);
  textMode(CENTER);
  text("Capas Intermedias", width/2-130, 50);
  text("Salida", 1250, 50);
  //rectMode(CENTER);
  //rect(width/2, 425, 400, 400, 20);

  noLoop();
}
