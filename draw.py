import golly as g
import math
import re

# zendegi # reshto
pixels = [(11, 9), (11, 12), (11, 13), (11, 14), (12, 14), (13, 14), (14, 9), (14, 11), (14, 12), (15, 12), (16, 12), (17, 6), (17, 10), (17, 11), (17, 12), (18, 6), (18, 7), (18, 10), (18, 12), (19, 7), (19, 8), (20, 8), (20, 10), (20, 11), (20, 12), (21, 12), (22, 12), (22, 13), (22, 14), (23, 14), (24, 14), (25, 12), (25, 13), (25, 14), (8, 21), (8, 23), (9, 20), (9, 21), (9, 22), (9, 23), (9, 24), (10, 21), (10, 23), (11, 20), (11, 21), (11, 22), (11, 23), (11, 24), (12, 21), (12, 23), (19, 20), (24, 20), (23, 21), (20, 21), (18, 21), (26, 23), (23, 23), (21, 23), (19, 23), (17, 23), (15, 23), (25, 23), (15, 24), (15, 25), (26, 24), (25, 24), (24, 24), (23, 24), (22, 24), (21, 24), (20, 24), (19, 24), (18, 24), (17, 24), (25, 25), (26, 26), (16, 26), (15, 26), (25, 26)]

M = 8  # size of the variables. can be 8, 16 or 32

# Build assembly instructions to draw the pixels
program_lines = []
#program_lines.append("erase")

for (px, py) in pixels:
    # Build assembly lines to plot each pixel
    program_lines.append(f"write a1 {px}")
    program_lines.append(f"write a2 {py}")
    program_lines.append("disp a1 a2")

# Add an infinite jump so we don't keep running off the end
program_lines.append("goto 9999")

# Combine into one multiline string
program = "\n".join(program_lines)

program = program.strip()
program = program.rstrip(" \n")
program = program.lstrip(" \n")

# Calculate necessary parameters
addresses = re.findall('a[0-9]+', program)
Ns = [int(a[1:]) for a in addresses]
N = 2**int(math.ceil(math.log(max(Ns)+1,2)))
N = max(4,N)

P = len(program.split("\n"))
P = 2**int(math.ceil(math.log(P+1,2)))
P = max(16,P)


f = "patterns/computer_{}_{}_{}.mc".format(N,M,P)
print(f)

instructions = [" ","++", "-", "+", "or", "and", "xor", "not",">>","<<",
                "rr","rl","=0","!=0","less","most","write","move","rfb","wfb","disp","erase","print","*-"]
alu1 = ["++", "not",">>","<<","rr","rl","=0","!=0","less","most","move","*-"]
alu2 = ["-", "+", "or", "and", "xor"]

# The rest of the code remains the same as the original implementation
# (including all the helper functions: twos_complement, preprocess, assemble, etc.)
def twos_complement(v):
    v = bin(-v)[2:].zfill(M)
    v = "".join(["0" if c=="1" else "1" for c in v])
    v = int(v,2)+1
    v = bin(v)[2:].zfill(M)
    return v

def preprocess(program):
    lines = program.split("\n")
    processed = []
    for line in lines:
        # Remove leading/trailing whitespace
        line = line.strip()
        
        # Skip empty lines or lines that start with ';'
        if not line or line.startswith(";"):
            continue
        
        processed.append(preprocess_line(line))
    return processed

def preprocess_line(line):
    line = line.split()
    if not line:
        return ""
    instruction = line[0]
    aw = 'a0'
    ar1 = 'a0'
    ar2 = 'a0'
    data = 0
    if instruction in alu1:
        aw = line[1]
        ar1 = line[2]
    elif instruction in alu2:
        aw = line[1]
        ar1 = line[2]
        ar2 = line[3]
    if instruction == "-":
        aw = line[1]
        ar1 = line[3]
        ar2 = line[2]
    if instruction == "write":
        aw = line[1]
        data = line[2]
    if instruction == "rfb":
        aw = line[1]
        ar2 = line[2]
    if instruction == 'wfb':
        ar1 = line[1]
        ar2 = line[2]
    if instruction == 'disp':
        ar1 = line[1]
        ar2 = line[2]
    if instruction == 'print':
        ar1 = line[1]
    if instruction == 'goto':
        instruction = "write"
        data = line[1]
    if instruction == 'jump':
        instruction = "+"
        ar1 = line[1]
    return " ".join([instruction, aw, ar1, ar2, str(data)])

def assemble(lines):
    return list(map(assemble_line, lines))

def assemble_line(line):
    if not line.strip():
        return ""
    i = [" ","++", "-", "+", "or", "and", "xor", "not",">>","<<",
         "rr","rl","=0","!=0","less","most","write","move","rfb","wfb","disp","erase","print","*-"]
    parts = line.split()
    instruction = i.index(parts[0])
    aw = int(parts[1][1:])
    ar1 = int(parts[2][1:])
    ar2 = int(parts[3][1:])
    value = int(parts[4])
    return bin_from_id(instruction, aw, ar1, ar2, value)

def bin_from_id(instruction, aw, ar1, ar2, value):
    instruction = bin(instruction)[2:].zfill(5)
    aw = bin(aw)[2:].zfill(Nd)
    ar1 = bin(ar1)[2:].zfill(Nd)
    ar2 = bin(ar2)[2:].zfill(Nd)
    if value >= 0:
        value = bin(value)[2:].zfill(M)[::-1]
    else:
        value = twos_complement(value)
    return instruction + aw + ar1 + ar2 + value

def write_program(x,y,data,w=200):
    g.addlayer()
    g.open("bit2.mc")
    g.select([-w, -w, w*2, w*2])
    g.copy()
    g.dellayer()
    di = 4*30
    dj = Pd*2*30
    for il, line in enumerate(data):
        if not line:
            continue
        d1 = 0
        k = 0
        for i in range(5):
            if line[k] == "1":
                g.paste(x+d1+di*i+il*dj, y-d1-di*i+il*dj, "or")
            k += 1
        d2 = 30*30*4+4*30*Nd
        for i in range(Nd*3):
            if line[k] == "1":
                g.paste(x+d1+d2+5*di+di*i+il*dj, y-d1-d2-5*di-di*i+il*dj, "or")
            k += 1
        d3 = (3*N)*60-1110+300+900+6*30
        for i in range(M):
            if line[k] == "1":
                g.paste(x+d1+d2+d3+(5+Nd*3)*di+17*30*i+il*dj,
                         y-d1-d2-d3-(5+Nd*3)*di-17*30*i+il*dj, "or")
            k += 1

def paste(file, x, y):
    g.addlayer()
    g.open(file)
    rect = g.getrect()
    g.select(rect)
    g.copy()
    g.dellayer()
    g.paste(x, y, 'or')

def rm_line(x, y, dx, dy, w, N):
    for i in range(N):
        g.select([x+i*dx, y+i*dy, w, w])
        g.clear(0)

Nd = int(math.log(N, 2))
Pd = int(math.log(P, 2))
data = assemble(preprocess(program))

g.addlayer()
dj2 = 2*30
di2 = 60*Nd
left_input_x = -(3*N-1)*di2-(3*N-1)*dj2-900-500+123 + (3*Nd)*-4*30
left_input_y = -(3*N-1)*di2+(3*N-1)*dj2-300+73 + (3*Nd)*4*30
x,y = left_input_x-4*30*Nd, left_input_y+4*30*Nd
hm2 = 30*24*N+120*Nd + 5*30
wm = 30*17*M
walu = 1650*M+600
halu = 60*2*M+30*70
hp = 60*Pd*P
f = "patterns/computer_{}_{}_{}.mc".format(N,M,P)
print(f)
g.show(f)
g.open(f)
data = assemble(preprocess(program))
write_program(x-60*Pd*(P-1)-14274-249-240, y-60*Pd*(P-1)-6556-227+240, data)
if "disp" in program:
    paste('display.mc', halu+hm2+wm+M*60+438+3000, halu+hm2-wm+M*60-9487-3000)
    rm_line(halu+hm2+wm+M*60+1200-8*30, halu+hm2-wm+M*60+600-1-8*30, 4*30, 4*30, 100, 12)
g.save("programed.mc", 'mc')
