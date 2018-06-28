var f1,f2,f3,f4,f5,f6;
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
	frameRate(1);
}
//var a= setInterval(draw,5000);
function draw() {
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
	strokeWeight(6)
	fill(80,80,80)
	ellipse(x1,y1,30,30);
	x1 = 100+random(600);
	y1 = 150+random(600);


//x1=noise(x1);
/*if(x1<700 && y1<700){
x1=x1+5;
y1=y1+5;
}
else {
x1=x1-5;
y1=y1-5;
}*/
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

}
