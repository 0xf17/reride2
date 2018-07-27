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
  y=450;
  diff=fF-fB;
  var c1=color(114,168,255);
  var c2=color(255,255,255);
  a= round(map(diff,0,1023,0,100));
  frameRate(100);
}

function draw(){


//draw_line(700,850,400,450)
  background(255,255,255)
  textSize(32);
  noStroke()
  fill(0, 102, 153);
  text('fB=',750,450);
  text('fF=',750,500);
  text(round(fB), 800, 450);
  text(round(fF),800,500);
  text(round(diff),900,500);
  from = color(0, 0, 255);
  to = color(255,255, 255,);
  c1=lerpColor(from,to,0.6)
  c2=lerpColor(from,to,0.3)

  if (diff>0) {

    //for(var i=a;i>=0;i--)
    b=map(noise(xoff1),0,1,0,100)
    c=map(noise(yoff1),0,1,0,100)
    xoff1+=0.0058;
    yoff1+=0.0054;
    //fill(0,0,200)
    fill(55,123,232);
    quad(300,450,500,450,500,y-b,300,y-c)
    y1=y-b+100;y11=y-c+100;
    fill(98,155,247);
    quad(300,450,500,450,500,y1,300,y11)
    fill(136,180,252);
    y2=y-b+180;y22=y-c+180;
    quad(300,450,500,450,500,y2,300,y22)
    y=map(diff,0,1023,450,150);
    fill(255,255,255);
    quad(300,455,500,455,500,900,300,900)

  }
  if (diff<0) {

    //for(var i=a;i>=0;i--)
    b=map(noise(xoff1),0,1,0,100)
    c=map(noise(yoff1),0,1,0,100)
    xoff1+=0.0058;
    yoff1+=0.0054;
    //fill(0,0,200)
    fill(55,123,232);
    quad(300,450,500,450,500,y+b,300,y+c)
    y1=y+b-100;y11=y+c-100;
    fill(98,155,247);
    quad(300,450,500,450,500,y1,300,y11)
    fill(136,180,252);
    y2=y+b-180;y22=y+c-180;
    quad(300,450,500,450,500,y2,300,y22)
    y=map(diff,0,1023,450,150);
    fill(255,255,255);
    quad(300,445,500,445,500,0,300,0)

  }
  stroke(55,123,232)
  strokeWeight(10)
  line(200,450,600,450)
  textSize(32);
  noStroke()
  fill(0, 102, 153);
  text('b=',750,100);
  text('c=',750,150);
  text(round(b),800,100);
  text(round(c),800,150);
  text(y,1000,450);
  text(a,1000,350);
  diff=map(noise(xoff),0,1,-1023,1023);
  fF=map(noise(xoff),0,1,0,1023);
  fB=map(noise(xoff*4),0,1,0,1023);
  a=2+round(map(noise(xoff),0,1,0,100));
  xoff+=0.0022;

}
