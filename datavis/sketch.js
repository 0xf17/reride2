var f1,f2,f3,f4,f5,f6,x2=1095,y2=150,x3=1095,y3=750,b,c;
var xoff=0,r=0,g=0,b=0;
var yoff=0;
var x1off=0;
var y1off=0;
//function average(f1,f2,f3,f4,f5,f6){
function RL_lean(f1,f2){
	//f_right = (f1+f3+f5)/3;
	f_left = f1;
  //f_left = (f2+f4+f6)/3;
	f_right = f2;
if (f_right>f_left)
{
	var x_lean = map(f_right-f_left,0,1023,400,700);
}
else {
	var x_lean = map(f_right-f_left,-1023,0,100,400);
}
return x_lean;
}
function FB_lean(f3,f4,f5,f6){
	//f_right = (f1+f3+f5)/3;
	f_forward = (f3+f4)/2;
	f_backward = (f5+f6)/2;
  //f_left = (f2+f4+f6)/3;
if (f_forward>f_backward)
{
	var y_lean = map(f_forward-f_backward,0,1023,450,150);
}
else {
	var y_lean = map(f_forward-f_backward,-1023,0,450,750);
}
return y_lean;
}
function setup() {
	createCanvas(1440,900);
	x1=RL_lean(835,820);
	y1=FB_lean(800,700,700,750);

	//x2=FB_lean(800,700,700,750);
	frameRate(100);
}
//var a= setInterval(draw,5000);
function draw() {
	//weight distrubution of rider
	background(250,250,250)
	stroke(230,230,230)
	strokeWeight(1)
	fill(255,255,255)
	rect(50,100,700,700)
	stroke(240,240,240)
	line(x1,150,x1,750)
	stroke(240,240,240)
	line(100,y1,700,y1)
	stroke(255,255,255)
	strokeWeight(10)
	fill(r,g,b)
	ellipse(x1,y1,80,80);
	//noise generates random continuous values
	x1 = 100+map(noise(xoff),0,1,0,600);
	y1 = 150+map(noise(yoff),0,1,0,600);
	xoff+=0.0022;
	yoff+=0.0032;
	if (x1<=400)
	{
		r=map(x1,100,400,255,0);
		g=map(x1,200,300,255,0);
		b=map(x1,100,400,0,255);
	}
	else {
		r=map(x1,400,700,0,255);
		g=map(x1,500,600,0,255);
		b=map(x1,400,700,255,0);
	}

	//lines for axes
	stroke(0,0,255)
	strokeWeight(2)
	line(100,150,100,750)
	stroke(0,0,255)
	strokeWeight(2)
	line(700,150,700,750)
	stroke(255,0,0)
	strokeWeight(2)
	line(100,150,700,150)
	stroke(255,0,0)
	strokeWeight(2)
	line(100,750,700,750)
	stroke(210,210,210)
	line(100,450,700,450)
	stroke(210,210,210)
	line(400,150,400,750)

//lean and head stoop angles
/*	stroke(230,230,230)
	strokeWeight(1)
	fill(255,255,255)
	rect(800,100,590,700)
	stroke(240,240,240)
	line(x3,750,x2,150)
	stroke(240,240,240)
	line(820,y3,1370,y2)
//noise generates random continuous values for lean angles
	x2= 1095+map(noise(x1off),0,1,-100,100);
	x3= 1095-(x2-1095);
	y2= 450+map(noise(y1off),0,1,-50,50);
	y3= 450-(y2-450);
	x1off+=0.0022;
	y1off+=0.0032;*/
	strokeWeight(1)
	fill(255,255,255)
	//rect(800,100,590,700)
	ellipse(1095,450,600,600)
	stroke(240,240,240)
	line(x3,y3,x2,y2)
	//stroke(240,240,240)
	//line(820,y3,1370,y2)
	x2=1095+map(noise(xoff),0,1,-100,100);
	y2=sqrt(300*300-(x2-1095)*(x2-1095)) + 450;
  x3=2*1095-x2;
	y3=900-y2;
	b=atan((x2-1095)/(450-y2))*(180/PI);
	c=round(b);
	fill(0, 102, 153)
	textSize(24)
	text(c,1095,450)

//axes for lean angles
	stroke(210,210,210)
	strokeWeight(2)
	line(795,450,1395,450)
	stroke(210,210,210)
	strokeWeight(2)
	line(1095,150,1095,750)
	/*stroke(0,0,0)
	strokeWeight(2)
	line(820,150,820,750)
	stroke(0,0,0)
	strokeWeight(2)
	line(1370,150,1370,750)
	stroke(0,0,0)
	strokeWeight(2)
	line(820,150,1370,150)
	stroke(0,0,0)
	strokeWeight(2)
	line(820,750,1370,750)*/

}
