import sys
import re

class Oppa:
    def __init__(self):
        self.vars={}
        self.goto_point=None
    def toNumber(self,code:str):
        result=code
        for i in self.vars:
            result=result.replace(i+' 뭐야?',str(self.vars[i]))
        try:
            if re.fullmatch('[0-9+\-*)( ]+', result):
                return eval(result)
            else:
                sys.exit('오빠, 오빠, 오빠 계산이 이상해!\n\t'+code+'     <-')
        except:
            sys.exit('오빠, 오빠, 오빠 계산이 이상해!\n\t'+code+'     <-')
            #raise ArithmeticError('오빠, 오빠, 오빠 계산이 이상해!\n\t'+code+'<-')
    def type(self,code:str):
        if code.endswith('에 돈 많아'):
            return 'PLUS_1',code[:-6]
        if code.endswith(' 비싸'):
            return 'MINUS_1',code[:-3]
        if code.endswith(' 있어'):
            return 'DEF',code[:-3]
        if code.endswith(' 있어?'):
            return 'NO_OVER_LOADING_DEF',code[:-4]
        if code.endswith(' 집 어디야?'):
            return 'IF_GOTO',code[:-7]
        if code.startswith('집 '):
            return 'GOTO_POINT_SET',self.toNumber(code[2:])
        if code.endswith(' 좋아~'):
            return 'PRINT_NUMBER',self.toNumber(code[:-4])
        if code.endswith(' 좋아~~'):
            return 'PRINT_CHAR',self.toNumber(code[:-5])
        if code.endswith(' 뭐야??'):
            return 'INPUT_NUMBER',code[:-5]
        if code.endswith(' 뭐야???'):
            return 'INPUT_CHAR',code[:-6]
        NUMBER=' '.join(code.split(' ')[1:])
        if NUMBER[0]=='(' and NUMBER[-1]==')' or NUMBER.isdigit():
            return 'DEF_AND_RESET',code.split(' ')[0],self.toNumber(NUMBER)
        if code=='꽉 잡아~':
            return 'GOTO'
        return 'No',0
    def compileLine(self,code:str):
        if not code.startswith('오빠, 오빠, 오빠 '):
            sys.exit("오빠, 오빠, 오빠 나 불러!\n\t"+code+'<-')
        raw_code=code[11:]
        types=self.type(raw_code)
        if types[0]=='PLUS_1':
            if not types[1] in self.vars.keys():
                sys.exit('오빠, 오빠, 오빠 변수 없어~\n\t'+code+'<-')
            self.vars[types[1]]+=1
        if types[0]=='MINUS_1':
            if not types[1] in self.vars.keys():
                sys.exit('오빠, 오빠, 오빠 변수 없어~\n\t'+code+'<-')
            self.vars[types[1]]-=1
        if types[0]=='DEF':
            self.vars[types[1]]=0
        if types[0]=='NO_OVER_LOADING_DEF':
            if not types[1] in self.vars.keys():
                self.vars[types[1]]=0
        if types[0]=='GOTO_POINT_SET':
            self.goto_point=types[1]
        if types[0]=='IF_GOTO':
            if not self.goto_point:
                sys.exit('오빠, 오빠, 오빠 어디가?\n\t'+code+'<-')
            if types[1]=='' or self.vars[types[1]]>0:
                return self.goto_point
        if types[0]=='PRINT_NUMBER':
            print(types[1],end='')
        if types[0]=='PRINT_CHAR':
            print(chr(types[1]),end='')
        if types[0]=='INPUT_NUMBER':
            try:
                self.vars[type[1]]=int(input(':'))
            except:
                sys.exit('오빠, 오빠, 오빠 정수만 입력해\n\t'+code+'<-')
        if types[0]=='INPUT_CHAR':
            self.vars[type[1]]=ord(input(':'))
        if types[0]=='DEF_AND_RESET':
            self.vars[types[1]]=types[2]
        if types=='GOTO':
            if not self.goto_point:
                sys.exit('오빠, 오빠, 오빠 어디가?\n\t'+code+'<-')
            return self.goto_point
        #print(raw_code,self.vars,self.goto_point)
    def compile(self,code):
        line_codes=code.split('\n')
        i=0
        while i<len(line_codes):
            #print(line_codes[i],self.vars)
            jp=self.compileLine(line_codes[i])
            #print(jp)
            i+=1
            if jp:
                i=jp-1
        return jp
if __name__=='__main__':
    example_code="""오빠, 오빠, 오빠 i 있어
오빠, 오빠, 오빠 j 있어
오빠, 오빠, 오빠 i에 돈 많아
오빠, 오빠, 오빠 j에 돈 많아
오빠, 오빠, 오빠 집 11          
오빠, 오빠, 오빠 집 어디야?
오빠, 오빠, 오빠 i (9-(i 뭐야?))
오빠, 오빠, 오빠 i에 돈 많아
오빠, 오빠, 오빠 j (9-(j 뭐야?))
오빠, 오빠, 오빠 j에 돈 많아
오빠, 오빠, 오빠 (i 뭐야?) 좀 쩔어~
오빠, 오빠, 오빠 42 좀 쩔지~
오빠, 오빠, 오빠 (j 뭐야?) 좀 쩔어~
오빠, 오빠, 오빠 61 좀 쩔지~
오빠, 오빠, 오빠 ((i 뭐야?) * (j 뭐야?)) 좀 쩔어~
오빠, 오빠, 오빠 10 좀 쩔지~
오빠, 오빠, 오빠 j (9-(j 뭐야?))
오빠, 오빠, 오빠 집 9
오빠, 오빠, 오빠 j 집 어디야?
오빠, 오빠, 오빠 j 8
오빠, 오빠, 오빠 i (9-(i 뭐야?))
오빠, 오빠, 오빠 집 7
오빠, 오빠, 오빠 i 집 어디야?"""
    a=Oppa()
    a.compile(example_code)