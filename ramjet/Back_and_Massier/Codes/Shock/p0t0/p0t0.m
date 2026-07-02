clear
clc
g=1.4;
%% P0
P = readmatrix("C:\Users\adity\Documents\IITB_Internship\SU2\SU2_Projects\CD_Nozzle26\Codes\Shock\p0t0\pres.csv");
M = readmatrix("C:\Users\adity\Documents\IITB_Internship\SU2\SU2_Projects\CD_Nozzle26\Codes\Shock\p0t0\mac.csv");
for i = 1:length(P)
P0(i) = P(i)*(1+(M(i)*M(i)*(g-1)/2))^(g/(g-1));
end
%% P0 to csv
% Specify the filename for the CSV file
filename = 'P0.csv';

% Open the file for writing
fileID = fopen(filename, 'w');

% Check if the file was opened successfully
if fileID == -1
    error('Could not open file for writing.');
end

% Write the header row (optional, but good practice)
fprintf(fileID, 'P0\n');

% Write the data rows
for i = 1:length(P0)
    fprintf(fileID, '%f\n', P0(i));
end

% Close the file
fclose(fileID);

disp(['Data successfully written to ', filename]);
%% T0
T = readmatrix("C:\Users\adity\Documents\IITB_Internship\SU2\SU2_Projects\CD_Nozzle26\Codes\Shock\p0t0\temp.csv");
M = readmatrix("C:\Users\adity\Documents\IITB_Internship\SU2\SU2_Projects\CD_Nozzle26\Codes\Shock\p0t0\mac.csv");
for i = 1:length(T)
T0(i)= T(i)*(1+(M(i)*M(i)*(g-1)/2));
end
%% T0 to csv
% Specify the filename for the CSV file
filename = 'T0.csv';

% Open the file for writing
fileID = fopen(filename, 'w');

% Check if the file was opened successfully
if fileID == -1
    error('Could not open file for writing.');
end

% Write the header row (optional, but good practice)
fprintf(fileID, 'T0\n');

% Write the data rows
for i = 1:length(T0)
    fprintf(fileID, '%f\n', T0(i));
end

% Close the file
fclose(fileID);

disp(['Data successfully written to ', filename]);
%% D0
D = readmatrix("C:\Users\adity\Documents\IITB_Internship\SU2\SU2_Projects\CD_Nozzle26\Codes\den.csv");
M = readmatrix("C:\Users\adity\Documents\IITB_Internship\SU2\SU2_Projects\CD_Nozzle26\Codes\Shock\p0t0\mac.csv");
for i = 1:length(D)
D0(i) = D(i)*(1+(M(i)*M(i)*(g-1)/2))^(1/(g-1));
end
%%  D0 to csv
% Specify the filename for the CSV file
filename = 'D0.csv';

% Open the file for writing
fileID = fopen(filename, 'w');

% Check if the file was opened successfully
if fileID == -1
    error('Could not open file for writing.');
end

% Write the header row (optional, but good practice)
fprintf(fileID, 'D0\n');

% Write the data rows
for i = 1:length(D0)
    fprintf(fileID, '%f\n', D0(i));
end

% Close the file
fclose(fileID);

disp(['Data successfully written to ', filename]);