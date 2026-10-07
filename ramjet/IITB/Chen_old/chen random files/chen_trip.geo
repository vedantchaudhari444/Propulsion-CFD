// Gmsh project created on Wed Jul 02 14:01:29 2025
SetFactory("OpenCASCADE");
Circle(1) = {0.178, -0.204, 0, 0.255, 0, 0.068};
//+
Circle(2) = {0.178, -0.204, 0, 0.255, 0, 0.068};
//+
Circle(3) = {0.178, -0.204, 0, 0.255, 0, 0.068};
//+
Circle(4) = {0.178, -0.204, 0, 0.255, 0, 0.068};
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
Point(14) = {0.102, 0.051, 0, 1.0};
//+
Point(15) = {0.102, 0.05049, 0, 1.0};
//+

//+
Point(16) = {0.10251, 0.05049, 0, 1.0};
//+
Point(17) = {0.10251, 0.051, 0, 1.0};
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
Split Curve {1} Point {19, 20, 18};
//+
SetFactory("OpenCASCADE");
BooleanDifference{ Curve{1}; }{ Curve{5}; }
//+
//+
BooleanFragments{ Curve{1}; Point{19}; Point{22}; Point{18}; }{ Curve{5}; Point{20}; Point{21}; }
//+
BooleanDifference{ Curve{1}; Delete; }{ Curve{5}; Delete; }
//+
Recursive Delete {
  Curve{6}; 
}
//+
SetFactory("Built-in");
//+
SetFactory("Built-in");
//+
SetFactory("OpenCASCADE");
//+
Recursive Delete {
  Curve{5}; 
}
//+
Recursive Delete {
  Curve{8}; 
}
//+
Recursive Delete {
  Curve{14}; Point{20}; 
}
//+
Recursive Delete {
  Curve{10}; Point{18}; 
}
//+
Recursive Delete {
  Curve{12}; Point{18}; 
}
//+
Recursive Delete {
  Curve{16}; Point{18}; Point{22}; 
}
//+
Coherence;
//+
Circle(20) = {0.229, 0.437, 0, 0.389, 0, 0.155};
//+
Rotate {{0, 0, 1}, {0.229, 0.437, 0}, -Pi/2} {
  Curve{20}; 
}
//+
Circle(21) = {0.735, -0.542, 0, 0.656, 0, 0.155};
//+
Rotate {{0, 0, 1}, {0.735, -0.542, 0}, Pi/2} {
  Curve{21}; 
}

//+
Point(29) = {0.193, 0, 0, 1.0};
//+
Point(30) = {0.229, 0, 0, 1.0};
//+
Point(31) = {0.289, 0, 0, 1.0};
//+
Point(32) = {0.646, 0, 0, 1.0};
//+
Point(33) = {0.735, 0, 0, 1.0};
//+
Point(34) = {1.041, 0, 0, 1.0};
//+
Point(35) = {1.041, 0.114, 0, 1.0};
//+
Recursive Delete {
  Point{32}; 
}
//+
Recursive Delete {
  Point{23}; Curve{2}; Point{22}; 
}
//+
Point(36) = {0.634, 0, 0, 1.0};
//+
Point(37) = {0.102, 0, 0, 1.0};
//+
Point(38) = {0.10251, 0, 0, 1.0};
//+

//+
Line(23) = {10, 14};
//+
Line(24) = {14, 15};
//+
Line(25) = {15, 16};
//+
Line(26) = {16, 17};
//+
Line(27) = {9, 37};
//+
Line(28) = {37, 38};
//+
Line(29) = {17, 19};
//+
Line(30) = {38, 11};
//+
Line(31) = {11, 29};
//+
Line(32) = {29, 30};
//+
Line(33) = {30, 31};
//+
Line(34) = {26, 28};
//+
Line(35) = {31, 36};
//+
Line(36) = {36, 33};
//+
Line(37) = {27, 35};
//+
Line(38) = {33, 34};
//+
//+
Coherence;
//+
Coherence;
//+
Curve Loop(1) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -39, -38, -36, -35, -33, -32, -31, -30, -28, -27, 22};
//+
Curve Loop(2) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -39, -38, -36, -35, -33, -32, -31, -30, -28, -27, 22};
//+
Curve Loop(3) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -39, -38, -36, -35, -33, -32, -31, -30, -28, -27, 22};
//+
Curve Loop(4) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -39, -38, -36, -35, -33, -32, -31, -30, -28, -27, 22};
//+
Curve Loop(5) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -39, -38, -36, -35, -33, -32, -31, -30, -28, -27, 22};
//+
Curve Loop(6) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -39, -38, -36, -35, -33, -32, -31, -30, -28, -27, 22};
//+
Recursive Delete {
  Surface{2}; 
}
//+
Recursive Delete {
  Surface{3}; 
}
//+
Recursive Delete {
  Curve{22}; 
}
//+
Recursive Delete {
  Curve{22}; 
}
//+
Recursive Delete {
  Curve{22}; Point{9}; Point{10}; 
}
//+
Recursive Delete {
  Curve{22}; 
}
//+
Recursive Delete {
  Curve{22}; 
}
//+
Recursive Delete {
  Curve{22}; Point{9}; 
}
//+
Recursive Delete {
  Curve{22}; Point{10}; 
}
//+
Point(40) = {0, 0.05049, 0, 1.0};
//+
Split Curve {22} Point {10, 40, 9};
//+
SetFactory("Built-in");
//+
Split Curve {22} Point {10, 40, 9};
//+
Recursive Delete {
  Curve{22}; 
}
//+
SetFactory("OpenCASCADE");
BooleanFragments{ Curve{22}; Delete; }{ Point{10}; Point{40}; Point{9}; Delete; }
//+
Recursive Delete {
  Curve{22}; 
}
//+
Recursive Delete {
  Point{9}; 
}
//+
Recursive Delete {
  Point{10}; 
}
//+
Recursive Delete {
  Point{40}; 
}
//+
Delete {
  Point{40}; 
}
//+
Delete {
  Point{10}; 
}
//+
Delete {
  Curve{22}; 
}
//+
Delete {
  Point{9}; 
}
//+
Coherence;
//+
Coherence;
//+
Coherence;
//+
Coherence;
//+
//+
//+
Coherence;
//+
//+
Line(39) = {9, 10};
//+
Line(40) = {34, 35};
//+
Curve Loop(1) = {29, -7, 9, 20, 34, -21, 37, -40, -38, -36, -35, -33, -32, -31, -30, -28, -27, 39, 23, 24, 25, 26};
//+
Curve Loop(3) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -40, -38, -36, -35, -33, -32, -31, -30, -28, -27, 39};
//+
Curve Loop(4) = {29, -7, 9, 20, 34, -21, 37, -40, -38, -36, -35, -33, -32, -31, -30, -28, -27, 39, 23, 24, 25, 26};
//+
Curve Loop(5) = {34, -21, 37, -40, -38, -36, -35, -33, -32, -31, -30, -28, -27, 39, 23, 24, 25, 26, 29, -7, 9, 20};
//+
Curve Loop(6) = {34, -21, 37, -40, -38, -36, -35, -33, -32, -31, -30, -28, -27, 39, 23, 24, 25, 26, 29, -7, 9, 20};
//+
Curve Loop(7) = {34, -21, 37, -40, -38, -36, -35, -33, -32, -31, -30, -28, -27, 39, 23, 24, 25, 26, 29, -7, 9, 20};
//+
Curve Loop(8) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -40, -38, -36, -35, -33, -32, -31, -30, -28, -27, 39};
//+
Curve Loop(9) = {34, -21, 37, -40, -38, -36, -35, -33, -32, -31, -30, -28, -27, 39, 23, 24, 25, 26, 29, -7, 9, 20};
//+
Physical Curve(41) = {39, 23, 24, 26, 25, 29, 7, 9, 20, 34, 21, 37};
//+
Physical Curve("TOPWALL", 42) = {23, 24, 26, 25, 29, 7, 9, 20, 34, 21, 37};
//+
Physical Curve("BOTWALL", 43) = {27, 30, 31, 32, 33, 35, 36, 38};
//+
Physical Curve("INLET", 44) = {39};
//+
Physical Curve("OUTLET", 45) = {40};
//+
Physical Curve(41) -= {39};
//+
Curve Loop(10) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -40, -38, -36, -35, -33, -32, -31, -30, -28, -27, 39};
//+
Curve Loop(11) = {33, 35, 36, 38, 40, -37, 21, -34, -20, -9, 7, -29, -26, -25, -24, -23, -39, 27, 28, 30, 31, 32};
//+
Line(41) = {15, 37};
//+
Line(42) = {16, 38};
//+
Line(43) = {19, 11};
//+
Line(44) = {24, 29};
//+
Line(45) = {39, 30};
//+
Line(46) = {26, 31};
//+
Line(47) = {28, 36};
//+
Line(48) = {27, 33};
//+
Point(40) = {-0, 0.05049, -0, 1.0};
//+
Point(41) = {0.178, 0.05049, -0, 1.0};
//+
Line(49) = {40, 15};
//+
Line(50) = {16, 41};
//+
//+
Physical Curve(41) -= {43};
//+
Recursive Delete {
  Surface{1}; 
}
//+
Recursive Delete {
  Surface{2}; Curve{47}; Curve{48}; 
}
//+
Recursive Delete {
  Curve{46}; Curve{44}; Curve{43}; Curve{41}; Curve{42}; Curve{49}; Curve{50}; 
}
//+
Recursive Delete {
  Surface{3}; 
}
//+
Recursive Delete {
  Surface{4}; 
}
//+
Recursive Delete {
  Curve{45}; 
}
//+
Physical Curve(" TOPWALL", 42) -= {29, 21, 34, 20, 9, 7, 26, 25, 24, 36, 23, 35, 33, 32, 31, 30, 28, 27, 37, 40, 38, 39};
//+
Physical Curve(" BOTWALL", 43) -= {40, 34, 20, 38, 9, 7, 29, 26, 25, 24, 36, 23, 35, 33, 32, 31, 30, 28, 27, 39, 37, 21};
//+
Physical Curve(" INLET", 44) -= {7, 29, 26, 25, 24, 23, 31, 30, 28, 27, 39};
//+
Physical Curve(" OUTLET", 45) -= {40, 37, 38};
//+
Physical Curve(41) -= {40, 37, 38, 21, 36, 34, 35, 20, 9, 33, 7, 32, 31, 29, 26, 25, 24, 30, 28, 23, 27, 39};
//+
Curve Loop(12) = {35, 36, 38, 40, -37, 21, -34, -20, -9, 7, -29, -26, -25, -24, -23, -39, 27, 28, 30, 31, 32, 33};
//+
Curve Loop(13) = {35, 36, 38, 40, -37, 21, -34, -20, -9, 7, -29, -26, -25, -24, -23, -39, 27, 28, 30, 31, 32, 33};
//+
Surface(1) = {13};
//+
Transfinite Curve {23, 23, 24, 25, 26, 29, 29, 7, 9, 20, 34, 21, 37, 27, 27, 28, 30, 31, 32, 33, 35, 36, 38} = 200 Using Progression 1;
//+
Transfinite Curve {39, 40} = 60 Using Progression 1;
//+
Physical Curve("TOPWALL", 46) = {23, 24, 26, 25, 29, 7, 9, 20, 34, 21, 37};
//+
Physical Curve("BOTWALL", 47) = {27, 28, 30, 31, 32, 33, 35, 36, 38};
//+
Physical Curve("INLET", 48) = {39};
//+
Physical Curve("OUTLET", 49) = {40};
//+
Field[1] = BoundaryLayer;
Field[1].EdgesList = {23, 24, 26, 25, 29, 7, 9, 20, 34, 21, 37, 27, 28, 30, 31, 32, 33, 35, 36, 38};
Field[1].hwall_n = 0.0005;
Field[1].thickness = 0.02;
Field[1].ratio = 1.2;
Field[1].Quads = 1;

BoundaryLayer Field = 1;

//+
Recombine Surface {1};
