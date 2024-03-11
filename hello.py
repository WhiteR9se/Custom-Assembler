def r_binaryconverter(opcodes,registers,instruction):
    L=instruction.split(" ")
    L1=[]
    x=""
    for i in L:
        L1=L1+i.split(",")
    L2=L1.copy()
    L2.pop(0)
    L2=L2[::-1]
    print(L1)
    if L1[0] in rtype_instruction:
        x=x+rtype_instruction[L1[0]][0]+registers[L2[0]]+registers[L2[1]]+rtype_instruction[L1[0]][1]+registers[L2[2]]+opcodes[L1[0]]
    return x
#funct7 rs2 rs1 funct3 rd opcode

def twos_complement(binary1):
    str1=""
    for i in range(len(binary1)):
        if(binary1[i]=="0"):
            str1+="1"
        else:
            str1+="0"
    str1=str1[::-1]
    carry=1
    str2=""
    for i in range(len(str1)):
        if(str1[i]=='1' and carry==1):
            str2+='0'
            carry=1
        elif (str1[i]=='1' and carry==0 ) or (str1[i]=='0' and carry==1 ):
            str2+='1'
            carry=0
        else:
            str2+='0'
            carry=0
    if(carry==1):
        str2+='1'
    str2=str2[::-1]
    return str2

def decimal_to_11digitbinary(number):
    num=abs(number)
    #print(number)
    q=[]
    while num>=1:
        rem=num%2
        q.append(str(rem))
        num//=2
    q=q[::-1]
    q1=""
    for i in q:
        q1+=i
    q2=q1[::-1]
    while len(q2)!=12:
        q2+="0"
    if number>=0:
        pass
    else:
        q1=q2[::-1]
        q1=twos_complement(q1)
    return q1
def decimal_to_20digitbinary(number):
    num=abs(number)
    print(number)
    q=[]
    while num>=1:
        rem=num%2
        q.append(str(rem))
        num//=2
    q=q[::-1]
    q1=""
    for i in q:
        q1+=i
    q2=q1[::-1]
    while len(q2)!=20:
        q2+="0"
    if number>=0:
        pass
    else:
        q1=q2[::-1]
        q1=twos_complement(q1)
    
    return q1
def u_type(instruction, opcodes, registers):
    l1=instruction.split()
    imm=decimal_to_20digitbinary(l[2])
    rd=registers[l1[1][0:2]]
    if l1[0]=="lui":
        opcode="0110111"
    if l1[0]=="auipc":
        opcode="0010111"
    return(imm[19:0:-1]+rd+opcode)

def s_type(instruction, opcodes, registers):
    L = instruction.split(" ")
    L11 = []
    L1 = []
    x = ""
    for i in L:
        L11.extend(i.split(","))
    for i in L11:
        L1.extend(i.split("("))
    if L1[-1].endswith(")"):
        L1[-1] = L1[-1][:-1]
    imm=decimal_to_11digitbinary(l1[3])
    rs2=registers[l1[1]]
    rs1=registers[l1[4]]
    function="010"
    op="010011"
    return (imm[11:5:-1]+rs2+rs1+function+imm[4:0:-1]+op)

def b_type(instruction,opcodes,register):
    l=instruction.split()
    rs2=registers[l[1][0:2]]
    imm=decimal_to_11digitbinary(l[4])
    rs1=registers[l[2][0:2]]
    if l1[0]=="beq":
        funct="000"
    if l1[0]=="bne":
        funct="001"
    if l1[0]=="blt":
        funct="100"
    if l1[0]=="bge":
        funct="101"
    if l1[0]=="bltu":
        funct="110"
    if l1[0]=="bgeu":
        funct="111"
    op="1100011"
    return (imm[11]+imm[9:5:-1]+rs2+rs1+funct+imm[4:1:-1]+imm[10]+opcode)

def j_type(instruction,opcode,register):
    l=instruction.split()
    imm=decimal_to_20digitbinary(2)
    regis=registers[l[1][0:2]]
    opcode="1101111"
    return(imm[19]+ imm[9:0:-1]+imm[10]+imm[18:11:-1]+regis+opcode)
def i_binaryconverter(opcodes,registers,instruction):
    L=instruction.split(" ")
    L1=[]
    x=""
    for i in L:
        L1=L1+i.split(",")
    L2=L1.copy()
    L2.pop(0)
    L2.pop()
    L2=L2[::-1]
    #print(L1)
    if L1[0] in itype_instruction:
        x=x+decimal_to_11digitbinary(int(L1[-1]))+registers[L2[0]]+itype_instruction[L1[0]]+registers[L2[1]]+opcodes[L1[0]]
    return x       
def u_type(instruction, opcodes, registers):
    instruction="auipc rd, imm[31,12]"
    l=instruction.split(" ")
    l1=[]
    for i in l:
        l1=l1+i.split(",")
    #imm=
    rd=registers[l1[1]]
    if l1[0]=="lui":
        opcode="0110111"
    if l1[0]=="auipc":
        opcode="0010111"
    return(imm[19:0]+rd+opcode)

def s_type(instruction, opcodes, registers):
    instruction="auipc rd, imm[31,12]"
    l=instruction.split(" ")
    l1=[]
    for i in l:
        l1=l1+i.split(",")
    #imm=r_binaryconverter(opcodes,registers,instructions)
    rs2=registers[l1[1]]
    temp=l1[4]
    rs1=registers[temp[3:6]]
    function="010"
    op="010011"
    return (imm[11:5]+rs2+rs1+function+imm[4:0]+op)

def b_type(instruction,opcodes,register):
    instruction="auipc rd, imm[31,12]"
    l=instruction.split(" ")
    l1=[]
    for i in l:
        l1=l1+i.split(",")
    rs2=registers[l1[1]]
    #imm=
    rs1=registers[l1[3]]
    if l1[0]=="beq":
        funct="000"
    if l1[0]=="bne":
        funct="001"
    if l1[0]=="blt":
        funct="100"
    if l1[0]=="bge":
        funct="101"
    if l1[0]=="bltu":
        funct="110"
    if l1[0]=="bgeu":
        funct="111"
    op="1100011"
    return (imm[11]+imm[9:5]+rs2+rs1+funct+imm[4:1]+imm[10]+opcode)

def j_type(instruction,opcode,register):
    instruction="auipc rd, imm[31,12]"
    l=instruction.split(" ")
    l1=[]
    for i in l:
        l1=l1+i.split(",")
    #imm=
    regis=registers[l1[1]]
    opcode="1101111"
    return(imm[19]+ imm[9:0]+imm[10]+imm[18:11]+regis+opcode)




instruction=input()

file_path = "stdin.txt"
instruction = []
with open(file_path, "r") as file:
    for line in file:
        words = line.strip().split()
        instruction.extend(words)



#instruction: func7, func3

rtype_instruction = {"add": ("0000000","000"), "sub": ("0100000","000"), "and": ("0000000","111"), 
                        "or": ("0000000","110"), "xor": ("0000000","100"),
                        "slt": ("0000000","010"), "sltu": ("0000000","011"), 
                        "sll": ("0000000","001"), "srl": ("0000000","101")}
itype_instruction ={"lw": "010","addi": "000","sltiu": "011","jalr": "000"}

stype_instruction = {"sw": "010"}

btype_instruction = {"beq": "000", "bne": "001", "blt": "100", 
                     "bge": "101", "bltu": "110", "bgeu": "111" }

registers = {"zero":"00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100",
             "t0":"00101","t1":"00110","t2":"00111","t3":"11100","t4":"11101","t5":"11110","t6":"11111",
             "s0":"01000","s1":"01001","s2":"10010","s3":"10011","s4":"10100","s5":"10101","s6":"10110",
             "s7":"10111","s8":"11000","s9":"11001","s10":"11010","s11":"11011",
             "a0":"01010","a1":"01011","a2":"01100","a3":"01101","a4":"01110","a5":"01111","a6":"10000","a7":"10001"}


opcodes={"add": "0110011", "sub": "0110011", "sll": "0110011", "slt": "0110011", 
         "sltu": "0110011", "xor": "0110011", "srl": "0110011", 
         "or": "0110011", "and":"0110011", "lw": "0000011", "addi": "0010011", 
         "sltiu": "0010011", "jalr": "1100111", "sw": "0100011", "beq": "1100011", "bne": "1100011", 
         "blt": "1100011", "bge": "1100011", "bltu": "1100011", "bgeu": "1100011", 
         "lui": "0110111", "auipc": "0010111", "jal": "1101111"}
print(r_binaryconverter(opcodes,registers,instruction))
    
    












