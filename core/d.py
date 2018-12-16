d = """29
36
29
34
34
31
30
32
34
28
28
34
34
32
27
32
33
36
32
36
25
29
31
30
30"""

k = d.split()
for pm in k:
    if int(float(pm)) < 30:
        color = '#00c9fa'
    elif int(float(pm)) < 80:
        color = '#72da00'
    elif int(float(pm)) < 120:
        color = '#ffbd00'
    elif int(float(pm)) < 200:
        color = '#ff5a00'
    elif int(float(pm)) < 900:
        color = '#ff0000'
    else:
        color = '#fafafa'
    print(color)