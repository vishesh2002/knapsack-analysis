data= """
1	0.001
2	0.0015
3	0.0019
4	0.002
5	0.003
6	0.0054
7	0.0067
8	0.005
9	0.006
10	0.03
11	0.04
12	0.076
13	0.075
14	0.148
15	0.148
16	0.245
17	0.3
18	0.45
19	0.3
20	0.594
21	0.892
22	0.9102
23	0.96
24	1.134
25	1.164
26	1.595
27	2.418
28	2.428
29	3.815
30	3.1809
31	3.7
32	3.815
33	4.2
34	4.174
35	4.3
36	5.176
37	5.602
38	5.7
39	6.433
40	6.9002
41	7.12
42	7.3
43	7.9
44	8.1
45	10.102
46	9.4302
47	9.48
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
plt.title('Backtrack')
plt.xlabel('No of objects')
plt.ylabel('Execution time in (ms)')
plt.plot(tlist,ylist,'m.')
plt.show()