import csv

data = """
0.018749	1.04E+06
0	1.04E+06
0.066524	9.64E+05
0.10222	2.56E+05
0.15049	78003
0.017437	1.04E+06
0.016094	1.04E+06
0.014723	1.04E+06
0.013326	1.04E+06
0.011905	1.04E+06
0.010464	1.04E+06
0.0090035	1.04E+06
0.0075274	1.04E+06
0.0060379	1.04E+06
0.0045378	1.04E+06
0.0030297	1.04E+06
0.0015162	1.04E+06
0.067803	9.48E+05
0.069105	9.29E+05
0.070429	9.09E+05
0.071775	8.88E+05
0.073139	8.66E+05
0.074522	8.43E+05
0.075922	8.18E+05
0.077336	7.91E+05
0.078764	7.63E+05
0.080204	7.33E+05
0.081655	7.02E+05
0.084583	6.36E+05
0.087534	5.66E+05
0.089015	5.31E+05
0.090497	4.95E+05
0.091979	4.60E+05
0.093459	4.26E+05
0.094936	3.92E+05
0.096408	3.60E+05
0.097873	3.30E+05
0.099331	3.01E+05
0.10078	2.76E+05
0.020154	1.04E+06
0.021559	1.04E+06
0.022964	1.04E+06
0.024369	1.04E+06
0.025775	1.04E+06
0.02718	1.04E+06
0.028585	1.03E+06
0.02999	1.03E+06
0.031395	1.03E+06
0.0328	1.03E+06
0.034205	1.03E+06
0.035611	1.03E+06
0.037016	1.03E+06
0.038421	1.03E+06
0.039826	1.03E+06
0.041231	1.03E+06
0.042636	1.03E+06
0.044042	1.03E+06
0.045447	1.02E+06
0.046852	1.02E+06
0.048257	1.02E+06
0.049662	1.02E+06
0.051067	1.02E+06
0.052472	1.02E+06
0.053878	1.01E+06
0.055283	1.01E+06
0.056688	1.01E+06
0.058093	1.00E+06
0.059498	9.98E+05
0.060903	9.93E+05
0.062308	9.88E+05
0.063714	9.81E+05
0.065119	9.74E+05
0.10364	2.43E+05
0.10506	2.33E+05
0.10648	2.24E+05
0.1079	2.15E+05
0.10932	2.07E+05
0.11074	2.00E+05
0.11216	1.93E+05
0.11358	1.86E+05
0.115	1.79E+05
0.11642	1.73E+05
0.11784	1.67E+05
0.11926	1.61E+05
0.12068	1.55E+05
0.1221	1.49E+05
0.12352	1.44E+05
0.12494	1.39E+05
0.12636	1.34E+05
0.12778	1.29E+05
0.1292	1.25E+05
0.13062	1.21E+05
0.13204	1.16E+05
0.13346	1.12E+05
0.13488	1.08E+05
0.1363	1.05E+05
0.13772	1.01E+05
0.13914	97866
0.14056	94643
0.14198	91581
0.1434	88692
0.14482	85998
0.14624	83543
0.14766	81411
0.14908	79703
0.083115	6.69E+05
0.086056	6.01E+05




"""

lines = data.strip().split('\n')
positions = []
pressures = []

for line in lines:
    x, p = line.split()
    pressures.append(float(p))
    positions.append(float(x))

# Create a list of tuples (position, pressure)
data_tuples = list(zip(positions, pressures))

# Sort the tuples based on position (first element of each tuple)
sorted_data = sorted(data_tuples)

# Prepare data for CSV writing
sorted_positions = [item[0] for item in sorted_data]
sorted_pressures = [item[1] for item in sorted_data]

# Write to CSV file
filename = "sorted_pressure_position.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Position', 'Pressure'])  # Header row
    for i in range(len(sorted_positions)):
        csvwriter.writerow([sorted_positions[i], sorted_pressures[i]])

print(f"Sorted data written to sorted_pressure_position.csv")
