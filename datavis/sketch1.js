var fR,fL,fF,fB,a,y,yl,x1,x2,diff,xoff=0,xoff1=0;
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
  fF=800;
  fR=900;
  fL=600;
  diff=fF-fB;
  a= round(map(diff,0,1023,0,20));
  frameRate(100);
}

function draw(){
  stroke(0,0,200)
  strokeWeight(3)
  line(100,450,700,450)
//draw_line(700,850,400,450)
  background(255,255,255)
  stroke(0,0,200)
  strokeWeight(3)
  line(200,450,600,450)
  y=450;
  if (diff>0) {
    for (var i=a; i>=0; i--) {
      //x1= 300-sqrt(90000-(y-300)*(y-300));
      //x2= 300+sqrt(90000-(y-300)*(y-300));
      if (i==0) {
        b=map(noise(xoff1),0,1,0,80)
        xoff1+=0.0058;
        fill(0,0,200)
        //noStroke()
        triangle(300,y,500,y,500,y-b)
      }
      x1=300;
      x2=500;
      stroke(0,0,200)
      strokeWeight(3)
      line(x1,y,x2,y)
      y= y-(i*i/5);
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
        b=map(fR-fL,0,1023,0,80)
        fill(0,0,200)
        triangle(300,y,500,y,500,y+b)
      }
      x1=300;
      x2=500;
      stroke(0,0,200)
      strokeWeight(3)
      line(x1,y,x2,y)
      y= y+(i*i/5);
      //diff=map(noise(xoff),0,1,0,1023);
      //xoff+=0.22;
    if (y<=100) {
        break;
  }
 }
  }
  fF=map(noise(xoff),0,1,0,1023);
  fB=map(noise(xoff),0,1,0,1023);
  a=2+round(map(noise(xoff),0,1,0,18));
  xoff+=0.0022;

}
