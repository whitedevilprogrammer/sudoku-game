import random as r
class Sudoku:
    def __init__(self):
        self.row1 =[i for i in range(1,10)]
        self.row2 =[i for i in range(1,10)]
        self.row3 =[i for i in range(1,10)]
        self.row4 =[i for i in range(1,10)]
        self.row5 =[i for i in range(1,10)]
        self.row6 =[i for i in range(1,10)]
        self.row7 =[i for i in range(1,10)]
        self.row8 =[i for i in range(1,10)]
        self.row9 =[]
    def Basic_information(self):
        print('-' * 69)
        rules = '''KNOW THE RULES
Sudoku is a puzzle based on a small number of very simple rules:

1)Every square has to contain a single number
2)Only the numbers from 1 through to 9 can be used
3)Each 3×3 box can only contain each number from 1 to 9 once
4)Each vertical column can only contain each number from 1 to 9 once
5)Each horizontal row can only contain each number from 1 to 9 once
6)Once the puzzle is solved, this means that every row, column,
and 3×3 box will contain every number from 1 to 9 exactly once.'''
        pattern = '''*********SUDOKU GAME**********
   1  2  3  4  5  6  7  8  9
  ---------------------------
1 [0, 0, 2, 0, 7, 0, 1, 0, 0]
2 [0, 4, 6, 5, 1, 9, 3, 2, 7]
3 [1, 0, 0, 8, 2, 3, 5, 0, 0]
  ---------------------------
4 [0, 0, 1, 0, 6, 2, 7, 4, 0]
5 [4, 0, 5, 1, 8, 7, 0, 3, 6]
6 [6, 0, 3, 9, 5, 0, 8, 0, 2]
  ---------------------------
7 [0, 1, 0, 7, 3, 8, 0, 0, 0]
8 [0, 6, 8, 2, 9, 0, 4, 7, 3]
9 [0, 3, 9, 0, 0, 5, 0, 8, 1]
  ---------------------------'''
        print(rules)
        print(pattern)
        print('0 is the empty value'.upper())
        print('\nenter the vaild formate is :'.upper())
        print('Enter your row number column number and result of the number:9 6 3 ')
        print('9 is the Row')
        print('6 is the Column')
        print('3 is the enter your value on this place')
        print('mistake number is 3...! and then game is over..!!!')
        print('wait one minute! or not loading sudoku game please run again the program!'.upper())
        print('-' * 69)
        print()
    def main(self):
        r.shuffle(self.row1)
        r.shuffle(self.row2) # row2 line coding...
        on = 0
        true = True
        while true:
            for v in self.row2:
                if v != self.row1[on] :#and v != row2[on] and v != row3[on] and v != row4[on]:
                    on += 1
                    if on == 9:
                        v1 = set(self.row1[:3])&set(self.row2[:3])
                        v2 = set(self.row1[3:6])&set(self.row2[3:6])
                        v3 = set(self.row1[6:])&set(self.row2[6:])
                        if v1 == set() and v2 == set() and v3 == set():
                            #print('This is empty set...')
                            true = False # this place add the row3 coding with function
                            self.Row3()
                        else:
                            #print('this is some value in set..')
                            r.shuffle(self.row2)
                            on = 0
                            break
                else:
                    r.shuffle(self.row2)
                    on = 0
                    break


    def Row3(self):
        r.shuffle(self.row3) # row3 coding ...
        while True:
            v1,c1 = set( self.row2[:3])&set( self.row3[:3]),set( self.row1[:3])&set( self.row3[:3])
            v2,c2 = set( self.row2[3:6])&set( self.row3[3:6]),set( self.row1[3:6])&set( self.row3[3:6])
            v3,c3 = set( self.row2[6:])&set( self.row3[6:]),set( self.row1[6:])&set( self.row3[6:])
            if v1 == set() and v2 == set() and v3 == set() and c1 == set() and c2 == set() and c3 == set():
                #print('This is empty set...')
                self.Row4()
                break # this place add the row4 coding with function
            else:
                #print('this is some value in set..')
                r.shuffle( self.row3)
                on = 0

    def Row4(self):
        r.shuffle(self.row4) # row4 line coding...
        on = 0
        true = True
        while true:
            for v in self.row4:
                if v != self.row1[on] and v != self.row2[on] and v != self.row3[on] :
                    on += 1
                    if on == 9:
                        #print('end.')
                        self.Row5()
                        true = False # this place add the row5 coding with function
                else:
                    r.shuffle(self.row4)
                    on = 0
                    break

    def Row5(self):
        r.shuffle(self.row5) # row5 coding ...
        on = 0
        true = True
        while true:
            for v in self.row5:
                if v != self.row1[on] and v != self.row2[on] and v != self.row3[on] and v != self.row4[on] :
                    on += 1
                    if on == 9:
                        v1= set(self.row4[:3])&set(self.row5[:3])
                        v2 = set(self.row4[3:6])&set(self.row5[3:6])
                        v3 = set(self.row4[6:])&set(self.row5[6:])
                        if v1 == set() and v2 == set() and v3 == set():
                            #print('This is empty set...')
                            self.Row6()
                            true = False # this place add the row4 coding with function
                        else:
                            #print('this is some value in set..')
                            r.shuffle(self.row5)
                            on = 0
                            break
                else:
                    r.shuffle(self.row5)
                    on = 0
                    break

    def Row6(self):
        r.shuffle(self.row6) # row6 coding ... some problem on this place!!!
        on = 0
        true = True
        while true:
            for v in self.row6:
                if v != self.row1[on] and v != self.row2[on] and v != self.row3[on] and v != self.row4[on] and v != self.row5[on]:
                    on += 1
                    if on == 9:
                        v1,c1 = set(self.row4[:3])&set(self.row6[:3]),set(self.row5[:3])&set(self.row6[:3])
                        v2,c2 = set(self.row4[3:6])&set(self.row6[3:6]),set(self.row5[3:6])&set(self.row6[3:6])
                        v3,c3 = set(self.row4[6:])&set(self.row6[6:]),set(self.row5[6:])&set(self.row6[6:])
                        if v1 == set() and v2 == set() and v3 == set() and c1 == set() and c2 == set() and c3 == set():
                            #print('This is empty set...')
                            self.Row7()
                            true = False # this place add the row7 coding with function
                        else:
                            r.shuffle(self.row6)
                            on = 0
                            break
                else:
                    r.shuffle(self.row6)
                    on = 0
                    break

    def Row7(self):
        r.shuffle(self.row7)
        on = 0
        true = True
        while true:
            for v in self.row7:
                if v != self.row1[on] and v != self.row2[on] and v != self.row3[on] and v != self.row4[on] and v != self.row5[on] and v != self.row6[on]:
                    on += 1
                    if on == 9:
                        self.Row8()
                        true = False
                else:
                    r.shuffle(self.row7)
                    on = 0
                    break

    def Row8(self):
        r.shuffle(self.row8)
        on = 0
        true = True
        while true:
            for v in self.row8:
                if v != self.row1[on] and v != self.row2[on] and v != self.row3[on] and v != self.row4[on] and v != self.row5[on] and v != self.row6[on] and v != self.row7[on]:
                    on += 1
                    if on == 9:
                        v1 = set(self.row7[:3])&set(self.row8[:3])
                        v2 = set(self.row7[3:6])&set(self.row8[3:6])
                        v3 = set(self.row7[6:])&set(self.row8[6:])
                        if v1 == set() and v2 == set() and v3 == set():
                            #print('This is empty set...')
                            self.Row9()
                            true = False
                        else:
                            #print('this is some value in set..')
                            r.shuffle(self.row8)
                            on = 0
                            break
                else:
                    r.shuffle(self.row8)
                    on = 0
                    break

    def Row9(self):
        true = True
        on = 0
        while True:
            v = r.randrange(1,10)
            if v != self.row1[on] and v != self.row2[on] and v != self.row3[on] and v != self.row4[on] and v != self.row5[on] and v != self.row6[on] and v != self.row7[on] and v != self.row8[on]:
                self.row9.append(v)
                on += 1# entha statement ulla vantha.. (value is correct)
                if on == 9:
                    break # end of the place...

    def Two_access(self):
        self.r1 = self.row1[:]
        self.r2 = self.row2[:]
        self.r3 = self.row3[:]
        self.r4 = self.row4[:]
        self.r5 = self.row5[:]
        self.r6 = self.row6[:]
        self.r7 = self.row7[:]
        self.r8 = self.row8[:]
        self.r9 = self.row9[:]

    def Printing_formate(self,name=None):
        all_list = [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r7,self.r8,self.r9]
        if name:
            all_list = [self.row1, self.row2, self.row3, self.row4, self.row5, self.row6, self.row7, self.row8,
                        self.row9]
        l = 27
        d = '-'
        v = '  '
        gname = 'Sudoku game'.upper()
        print(gname.center(30,'*'))
        for i in range(len(all_list)):
            if i == 0:
                print('  ',1,'',2,'',3,'',4,'',5,'',6,'',7,'',8,'',9)
                print(v + d*l)
            if i == 3 or i == 6:
                print(v + d*l)

            print(i+1,all_list[i])
        print(v + d*l)

    def Some_place_removing(self):
        all_list = [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r7,self.r8,self.r9]
        for one_list in all_list:
            #print(one_list)
            v = r.randrange(1,9)
            for one_value in range(v):
                index = r.randrange(9)
                one_list[index] = 0

    def Mistake_or_not(self):
        self.v[0] = int(self.v[0]) - 1
        self.v[1] = int(self.v[1]) - 1
        self.v[2] = int(self.v[2])
        all_list = [self.row1,self.row2,self.row3,self.row4,self.row5,self.row6,self.row7,self.row8,self.row9]
        all_lists = [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9]
        if all_lists[self.v[0]][self.v[1]] != 0:
            print('some value on this place, not change it !'.upper())
            self.Printing_formate()
        elif all_list[self.v[0]][self.v[1]] == self.v[2] and all_lists[self.v[0]][self.v[1]] == 0:
            all_lists[self.v[0]][self.v[1]] = self.v[2]
            print('this is correct answer'.title())
            self.Printing_formate()
            for one_list in all_lists:
                if 0 not in one_list:
                    win = True
                else:
                    win = False
                    break
            if win:
                print('win the sudoku game!!!'.title())
                self.true = False
        else:
            self.run += 1
            if self.run == 3:
                print(f'mistake number {self.run}...!')
                print('The game is end...'.upper())
                self.true = False
            else:
                print(f'mistake number {self.run}...!')

    def Checking_value(self):
        self.run = 0
        self.true = True
        while self.true:
            user = str(input('Enter your row number column number and result of the number:')).strip()
            if user.lower() == 'show me answer':
                print('This Sudoku Answer'.upper())
                self.Printing_formate(name=True)
                break
            self.v = user.split()
            for i in self.v:
                if i.isdigit() and 0 < int(i) and 10 > int(i):
                    yes = True
                else:
                    yes = False
                    break
            if len(user) == 5 and yes:
                self.Mistake_or_not()
            else:
                print('printing formate is worng, example '.upper() + ':9 6 3')
                self.Printing_formate()


if __name__ == '__main__':
    start = Sudoku()
    start.Basic_information()# basic information of sudoku...
    start.main()# this is the main function of the class...
    start.Two_access()# this is example r1 == row1...
    start.Some_place_removing()# removing the value in sudoku...
    start.Printing_formate()# user ku display panna vendiya out put
    start.Checking_value()# checking the user value and then proccess the date correct or not !!!
        
            
            
            
            

    

        



            
        
        


