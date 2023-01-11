data= """
1	0.047
2	0.029
3	0.028
4	0.046
5	0.03
6	0.041
7	0.045
8	0.027
9	0.042
10	0.047
11	0.045
12	0.038
13	0.033
14	0.046
15	0.042
16	0.052
17	0.064
18	0.031
19	0.039
20	0.042
21	0.044
22	0.049
23	0.06
24	0.021
25	0.045
26	0.05
27	0.044
28	0.048
29	1.043
30	1.043
31	1.037
32	1.047
33	2.046
34	2.041
35	2.043
36	3.046
37	2.054
38	3.051
39	3.048
40	3.044
41	4.043
42	4.046
43	4.042
44	4.036
45	4.049
46	4.032
47	3.048

""".split('\n')

 # split this string on the "newline" character.

tlist = []
ylist = []
for s in data:
    if s:
        t,y = s.split()     # split the string in two
        t=float(t)          # convert time to float
        y=float(y)          # convert y-position (cm) to float in meters
        tlist.append(t)     # append to the list for time data
        ylist.append(y)     # append to the list for y-position data
        

import matplotlib.pyplot as plt
plt.title('Greedy')
plt.xlabel('No of objects')
plt.ylabel('Execution time in (ms)')
plt.plot(tlist,ylist,'m.')
plt.show()