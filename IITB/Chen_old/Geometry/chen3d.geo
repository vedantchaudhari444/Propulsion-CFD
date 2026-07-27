// Gmsh project created on Wed Jun 04 13:41:03 2025
SetFactory("OpenCASCADE");
//+
Circle(1) = {0.178, -0.204, 0, 0.255, 0, 0.068};
//+
Circle(2) = {0.178, -0.204, 0, 0.255, 0, 0.068};
//+
Circle(3) = {0.178, -0.204, 0, 0.255, 0, 0.068};
//+
Circle(4) = {0.178, -0.204, 0, 0.255, 0, 0.068};
//+
Point(9) = {0, 0, 0, 1.0};
//+
Point(10) = {0, 0.051, 0, 1.0};
//+
Point(11) = {0.178, 0, 0, 1.0};
//+
Rotate {{0, 0, 1}, {0.178, -0.204, 0}, Pi/2} {
  Curve{1}; 
}
//+
Rotate {{0, 0, 1}, {0.178, -0.204, 0}, -0.068} {
  Curve{1}; 
}
//+
Circle(5) = {0.229, 0.303, 0, 0.255, 0, 0.142};
//+
Rotate {{0, 0, 1}, {0.229, 0.303, 0}, -Pi/2} {
  Curve{5}; 
}
//+
Rotate {{0, 0, 1}, {0.229, 0.303, 0}, -0.142} {
  Curve{5}; 
}
//+
BooleanUnion{ Curve{1}; }{ Curve{5}; }
//+
SetFactory("Built-in");
//+
Split Curve {1} Point {16, 12, 13};
//+
SetFactory("OpenCASCADE");
BooleanDifference{ Curve{1}; }{ Curve{5}; }
//+
BooleanFragments{ Curve{1}; Point{16}; Point{12}; Point{13}; }{ Curve{5}; Point{14}; Point{15}; }
//+
BooleanDifference{ Curve{1}; Delete; }{ Curve{5}; Delete; }
//+
Recursive Delete {
  Curve{6}; 
}
//+
Recursive Delete {
  Curve{10}; 
}
//+
BooleanDifference{ Curve{5}; Delete; }{ Curve{12}; Delete; }
//+
Recursive Delete {
  Curve{8}; Point{14}; 
}
//+
SetFactory("OpenCASCADE");
//+
SetFactory("Built-in");
//+
SetFactory("OpenCASCADE");
//+
Recursive Delete {
  Curve{16}; 
}
//+
Recursive Delete {
  Curve{14}; 
}
//+
Recursive Delete {
  Curve{18}; Point{14}; 
}
//+
Recursive Delete {
  Curve{2}; 
}
//+
Recursive Delete {
  Curve{3}; Point{6}; Point{5}; 
}
//+
Recursive Delete {
  Curve{4}; Point{8}; Point{7}; 
}
//+
Circle(20) = {0.229, 0.437, 0, 0.389, 0, 0.155};
//+
Rotate {{0, 0, 1}, {0.229, 0.437, 0}, -Pi/2} {
  Curve{20}; 
}
//+
Point(21) = {0.193, 0, 0, 1.0};
//+
Point(22) = {0.229, 0, 0, 1.0};
//+
Point(23) = {0.289, 0, 0, 1.0};
//+
Circle(21) = {0.735, -0.542, 0, 0.656, 0, 0.887};
//+
Recursive Delete {
  Curve{21}; 
}
//+
Circle(21) = {0.735, -0.542, 0, 0.656, 0, 0.155};
//+
Rotate {{0, 0, 1}, {0.735, -0.542, 0}, Pi/2} {
  Curve{21}; 
}
//+
Point(26) = {0.646, 0, 0, 1.0};
//+
Point(27) = {0.735, 0, 0, 1.0};
//+
Point(28) = {1.041, 0, 0, 1.0};
//+
Point(29) = {1.041, 0.114, 0, 1.0};
//+
Recursive Delete {
  Point{26}; 
}
//+
Point(30) = {0.634, 0, 0, 1.0};
//+
Line(22) = {9, 10};
//+
Line(23) = {28, 29};
//+
Line(24) = {10, 13};
//+
Line(25) = {9, 11};
//+
Line(26) = {11, 21};
//+
Line(27) = {21, 22};
//+
Line(28) = {22, 23};
//+
Line(29) = {23, 30};
//+
Line(30) = {20, 25};
//+
Line(31) = {30, 27};
//+
Line(32) = {27, 28};
//+
Line(33) = {24, 29};
//+
Recursive Delete {
  Point{16}; 
}
//+
Recursive Delete {
  Point{16}; 
}
Line(34) = {15, 19};
//+
Line(35) = {14, 16};
//+
Line(36) = {17, 18};
//+
LineLoop(1) = {34, 35, 36};

//+
Coherence;
//+
Curve Loop(1) = {24, -7, 9, 20, 30, -21, 33, -23, -32, -31, -29, -28, -27, -26, -25, 22};
//+
Surface(1) = {1};
//+
Transfinite Surface {1} = {10, 9, 28, 29};
//+
Transfinite Curve {22, 23} = 20 Using Progression 1;
//+
Transfinite Curve {24, 25} = 25 Using Progression 1;
//+
Transfinite Curve {7, 26} = 5 Using Progression 1;
//+
Transfinite Curve {9, 27} = 10 Using Progression 1;
//+
Transfinite Curve {20, 28} = 15 Using Progression 1;
//+
Transfinite Curve {30, 29} = 35 Using Progression 1;
//+
Transfinite Curve {21, 31} = 20 Using Progression 1;
//+
Transfinite Curve {33, 32} = 30 Using Progression 1;
//+
Recombine Surface {1};
//+
Transfinite Curve {24, 25} = 35 Using Progression 1;
//+
Transfinite Curve {24, 25} = 40 Using Progression 1;
//+
Transfinite Curve {24, 25} = 45 Using Progression 1;
//+
Transfinite Curve {30, 29} = 65 Using Progression 1;
//+
Transfinite Curve {33, 32} = 60 Using Progression 1;
//+
Transfinite Curve {22, 23} = 40 Using Progression 1;
//+
Transfinite Curve {22, 23} = 40 Using Bump 1.05;
//+
Transfinite Curve {22, 23} = 40 Using Bump 1.1;
//+
Transfinite Curve {22, 23} = 40 Using Bump 3;
//+
Transfinite Curve {22, 23} = 40 Using Bump 0.5;
//+
Transfinite Curve {22, 23} = 60 Using Bump 0.1;
//+
Transfinite Curve {22, 23} = 70 Using Bump 0.05;
//+
Transfinite Curve {22, 23} = 80 Using Bump 0.01;
//+
Transfinite Curve {22, 23} = 90 Using Bump 0.005;

//+
Extrude {0, 0, 0.152} {
  Surface{1}; Layers {40}; Recombine;
}
//+
Physical Volume("FLUID", 66) = {1};
//+
Physical Surface("INLET", 67) = {2};
//+
Physical Surface("OUTLET", 68) = {10};
//+
Physical Surface("WALL", 69) = {17, 16, 15, 14, 13, 12, 11, 3, 4, 5, 6, 7, 8, 9};
//+
Physical Surface("SYMMETRY", 70) = {18, 1};
