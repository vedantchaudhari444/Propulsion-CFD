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
Plane Surface(1) = {1, 2, 3, 4};
//+
Curve Loop(5) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -39, -38, -36, -35, -33, -32, -31, -30, -28, -27, 22};
//+
Plane Surface(2) = {5};
//+
Curve Loop(6) = {23, 24, 25, 26, 29, -7, 9, 20, 34, -21, 37, -39, -38, -36, -35, -33, -32, -31, -30, -28, -27, 22};
//+
Plane Surface(3) = {6};
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
Surface(1) = {1};
//+
Extrude {0, 0, 0.152} {
  Curve{34}; Curve{20}; Curve{9}; Curve{7}; Curve{29}; Curve{26}; Curve{25}; Curve{24}; Curve{23}; Curve{39}; Curve{27}; Curve{30}; Curve{31}; Curve{32}; Curve{33}; Curve{35}; Curve{21}; Curve{36}; Curve{38}; Curve{37}; Curve{40}; 
}
