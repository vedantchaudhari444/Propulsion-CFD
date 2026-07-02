%% Writing x coord to csv file
x = [0.997 
0.991 
0.977 
0.977 
0.958 
0.908 
0.900 
0.788 
0.728 
0.647 
0.505 
0.461 
0.323 
0.207 
0.199 
0.190 
0.176 
0.167 
0.159 
0.145 
0.132 
0.128 
0.124 
0.116 
0.108 
0.101 
0.095 
0.088 
0.083 
0.074 
0.069 ];


% Specify the filename for the CSV file
filename = 'x_co.csv';

% Open the file for writing
fileID = fopen(filename, 'w');

% Check if the file was opened successfully
if fileID == -1
    error('Could not open file for writing.');
end

% Write the header row (optional, but good practice)
fprintf(fileID, 'x_values\n');

% Write the data rows
for i = 1:length(x)
    fprintf(fileID, '%f\n', x(i));
end

% Close the file
fclose(fileID);

disp(['Data successfully written to ', filename]);