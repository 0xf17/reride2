var fR,fL,fF,fB,a,y,yl,x1,x2,diff,xoff=0,xoff1=0,yoff=0,yoff1=0;
/*function draw_line(f1,f2,f5,f6){
  fF=(f1+f2)/2;
  fB=(f5+f6)/2;
  diff=fF-fB;
  if (fF>fB) {
    while (a<20) {
    a= round(map(diff,0,1023,0,20));
    y=300;
    for (var i=a; i>=0; i--) {
        x1= 300-sqrt(90000-(y-300)*(y-300));
        x2= 300+sqrt(90000-(y-300)*(y-300));
        stroke(mouseY,200,200)
        strokeWeight(4)
        line(x1,y,x2,y)
        y= y-(i*i);
        //diff=map(noise(xoff),0,1,0,1023);
        //xoff+=0.22;
    if (yl<0) {
      break;
    }
   }
    a=map(noise(xoff),0,1,0,20);
    xoff+=0.22;
  }
 }
}*/
function setup(){
  createCanvas(1440,900)
  fB=700;
  fF=1300;
  fR=900;
  fL=600;
  diff=fF-fB;
  var c1=color(114,168,255);
  var c2=color(255,255,255);
  a= round(map(diff,0,1023,0,20));
  frameRate(100);
}

function draw(){

  stroke(0,0,200)
  strokeWeight(10)
  line(100,450,700,450)
//draw_line(700,850,400,450)
  background(255,255,255)
  stroke(0,0,200)
  strokeWeight(10)
  line(200,450,600,450)
  textSize(32);
  noStroke()
  fill(0, 102, 153);
  text('fB=',750,450);
  text('fF=',750,500);
  text(round(fB), 800, 450);
  text(round(fF),800,500);
  text(round(diff),900,500);

  y=450;
  if (diff>0) {
    for (var i=a; i>=0; i--) {
      //x1= 300-sqrt(90000-(y-300)*(y-300));
      //x2= 300+sqrt(90000-(y-300)*(y-300));
      if (i==0) {
        b=map(noise(xoff1),0,1,0,60)
        c=map(noise(yoff1),0,1,0,60)
        xoff1+=0.0058;
        yoff1+=0.0054;
        fill(0,0,200)
        quad(300,y-c,300,y,500,y,500,y-b)
      //  quad(300,y-c-100,300,y-100,500,y-100,500,y-b-100)
        //noStroke()
        //quad(400,y-25,400,y-35,500,y-(b/2)-30,500,y+(b/2)-30);
        //lerpcolor(from,to,0.5)
        //quad(300,450,500,450,500,y-b,300,y-c)

        //triangle(300,y,500,y,500,y-b)

      }

      x1=300;
      x2=500;
      stroke(0,0,200)
      strokeWeight(3)
      line(x1,y,x2,y)
      y= y-(i*i*i/25);
      //y=y-50;
      //diff=map(noise(xoff),0,1,0,1023);
      //xoff+=0.22;
    if (y<=100) {
        break;
  }
 }
}

  if(diff<0) {
    for (var i=a; i>=0; i--) {
      //x1= 300-sqrt(90000-(y-300)*(y-300));
      //x2= 300+sqrt(90000-(y-300)*(y-300));
      if (i==0) {
        b=map(fR-fL,0,1023,0,60)
        fill(0,0,200)
        quad(400,y+5,400,y-5,300,y-(b/2),300,y+(b/2));
        //triangle(300,y,500,y,500,y+b)
      }
      x1=300;
      x2=500;
      stroke(0,0,200)
      strokeWeight(20)
      line(x1,y,x2,y)
      y= y+(i*i/5);
      //diff=map(noise(xoff),0,1,0,1023);
      //xoff+=0.22;
    if (y<=100) {
        break;
  }
 }
  }
  textSize(32);
  noStroke()
  fill(0, 102, 153);
  text('b=',750,100);
  text('c=',750,150);
  text(round(b),800,100);
  text(round(c),800,150);
  fF=map(noise(xoff),0,1,0,1023);
  fB=map(noise(xoff*4),0,1,0,1023);
  a=2+round(map(noise(xoff),0,1,0,18));
  xoff+=0.0022;
}
function setGradient(x, y, w, h, c1, c2, axis) {

  noFill();

  if (axis == Y_AXIS) {  // Top to bottom gradient
    for (var i = y; i <= y+h; i++) {
      var inter = map(i, y, y+h, 0, 1);
      var c = lerpColor(c1, c2, inter);
      stroke(c);
      line(x, i, x+w, i);
    }
  }
  else if (axis == X_AXIS) {  // Left to right gradient
    for (var i = x; i <= x+w; i++) {
      var inter = map(i, x, x+w, 0, 1);
      var c = lerpColor(c1, c2, inter);
      stroke(c);
      line(i, y, i, y+h);
    }
  }
}
