var f1,f2,f3,f4,f5,f6;
//function average(f1,f2,f3,f4,f5,f6){
function RL_lean(f1,f2){
	//f_right = (f1+f3+f5)/3;
	f_left = f1;
  //f_left = (f2+f4+f6)/3;
	f_right = f2;
if (f_right>f_left)
{
	var x_lean = map(f_right-f_left,-1023,1023,400,700);
}
else {
	var x_lean = map(f_left-f_right,-1023,1023,400,700);
}
return x_lean;
}
function FB_lean(f1,f2){
	//f_right = (f1+f3+f5)/3;
	f_left = f1;
  //f_left = (f2+f4+f6)/3;
	f_right = f2;
if (f_right>f_left)
{
	var x_lean = map(f_right-f_left,-1023,1023,400,700);
}
else {
	var x_lean = map(f_left-f_right,-1023,1023,400,700);
}
return x_lean;
}
function setup() {
	createCanvas(1440,900);
	x1=RL_lean(745,1012);
	y1=FB_lean(800,400);
	frameRate(5);
}
//var a= setInterval(draw,5000);
function draw() {
background(255,255,255)
fill(0,0,0)
ellipse(x1,y1,40,40);
x1 = 100+random(600);
y1 = 100+random(600);
 //await sleep(1000);
//stroke(0,0,0)
//line(x1,100,x1,700)
//stroke(0,0,0)
//line(100,y1,700,y1)

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
line(100,100,100,700)
stroke(0,0,255)
strokeWeight(2)
line(700,100,700,700)
stroke(255,0,0)
strokeWeight(2)
line(100,100,700,100)
stroke(255,0,0)
strokeWeight(2)
line(100,700,700,700)
stroke(255,0,0)
strokeWeight(2)
line(100,700,700,700)
stroke(0,0,0)
line(100,400,700,400)
stroke(0,0,0)
line(400,100,400,700)

}
