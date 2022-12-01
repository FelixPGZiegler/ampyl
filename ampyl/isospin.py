import numpy as np

# (+,+) (+,-) (-,+) (-,-)
prodOneHalfOneHalf = np.zeros((4,4),dtype = np.complex128)

# (+,+) (+,-) (0,+) (0,-) (-,+) (-,-)
prodOneOneHalf = np.zeros((6,6),dtype = np.complex128)

# (+,+) (+,0) (+,-) (0,+) (0,0) (0,-) (-,+) (-,0) (-,-)
prodOneOne = np.zeros((9,9),dtype = np.complex128)

# (++,+) (++,-) (+,+) (+,-) (-,+) (-,-) (--,+) (--,-)
prodThreeHalfOneHalf = np.zeros((8,8),dtype = np.complex128)

# (++,+) (++,0) (++,-) (+,+) (+,0) (+,-) (-,+) (-,0) (-,-) (--,+) (--,0) (--,-)
prodThreeHalfOne = np.zeros((12,12),dtype = np.complex128)

# (++,+) (++,-) (+,+) (+,-) (0,+) (0,-) (-,+) (-,-) (--,+) (--,-)
prodTwoOneHalf = np.zeros((10,10),dtype = np.complex128)

# (++,+) (++,0) (++,-) (+,+) (+,0) (+,-) (0,+) (0,0) (0,-) (-,+) (-,0) (-,-) (--,+) (--,0) (--,-)
prodTwoOne = np.zeros((15,15),dtype = np.complex128)

# J = 1, mJ = 1
prodOneHalfOneHalf[0][0] = 1.0
# J = 1, mJ = 0
prodOneHalfOneHalf[1][1] = 1.0 / np.sqrt(2.0)
prodOneHalfOneHalf[1][2] = 1.0 / np.sqrt(2.0)
# J = 1, mJ = -1
prodOneHalfOneHalf[2][3] = 1.0
# J = 0, mJ = 0
prodOneHalfOneHalf[3][1] = 1.0 / np.sqrt(2.0)
prodOneHalfOneHalf[3][2] = -1.0 / np.sqrt(2.0)

# J = 3/2, mJ = 3/2
# (+, +)
prodOneOneHalf[0][0] = 1.0
# J = 3/2, mJ = 1/2
# (+, -) (0, +)
prodOneOneHalf[1][1] = 1.0 / np.sqrt(3.0)
prodOneOneHalf[1][2] = np.sqrt(2.0/3.0)
# J = 3/2, mJ = -1/2
# (0, -) (-, +)
prodOneOneHalf[2][3] = np.sqrt(2.0/3.0)
prodOneOneHalf[2][4] = 1.0 / np.sqrt(3.0)
# J = 3/2, mJ = -3/2
# (-, -)
prodOneOneHalf[3][5] = 1.0
# J = 1/2, mJ = 1/2
# (+, -) (0, +)
prodOneOneHalf[4][1] = np.sqrt(2.0/3.0)
prodOneOneHalf[4][2] = -1.0 / np.sqrt(3.0)
# J = 1/2, mJ = -1/2
# (0, -) (-, +)
prodOneOneHalf[5][3] = 1.0 / np.sqrt(3.0)
prodOneOneHalf[5][4] = -np.sqrt(2.0/3.0)

# J = 2, mJ = 2
prodOneOne[0][0] = 1.0

# J = 2, mJ = 1
prodOneOne[1][1] = 1.0 / np.sqrt(2.0)
prodOneOne[1][3] = 1.0 / np.sqrt(2.0)

# J = 2, mJ = 0
prodOneOne[2][2] = 1.0 / np.sqrt(6.0)
prodOneOne[2][4] = np.sqrt(2.0/3.0)
prodOneOne[2][6] = 1.0 / np.sqrt(6.0)

# J = 2, mJ = -1

prodOneOne[3][5] = 1.0 / np.sqrt(2.0)
prodOneOne[3][7] = 1.0 / np.sqrt(2.0)

# J = 2, mJ = -2
prodOneOne[4][8] = 1.0

# J = 1, mJ = 1
prodOneOne[5][1] = 1.0 / np.sqrt(2.0)
prodOneOne[5][3] = -1.0 / np.sqrt(2.0)

# J = 1, mJ = 0
prodOneOne[6][2] = 1.0 / np.sqrt(2.0)
prodOneOne[6][6] = -1.0 / np.sqrt(2.0)

# J = 1, mJ = -1
prodOneOne[7][5] = 1.0 / np.sqrt(2.0)
prodOneOne[7][7] = -1.0 / np.sqrt(2.0)

# J = 0, mJ = 0
prodOneOne[8][2] = 1.0 / np.sqrt(3.0)
prodOneOne[8][4] = -1.0 / np.sqrt(3.0)
prodOneOne[8][6] = 1.0 / np.sqrt(3.0)


# J = 2 mJ = 2
prodThreeHalfOneHalf[0][0] = 1.0

# J = 2 mJ = 1
# (++, -) (+, +) 
prodThreeHalfOneHalf[1][1] = 0.5
prodThreeHalfOneHalf[1][2] = np.sqrt(3.0/4.0)

# J = 2 mJ = 0
prodThreeHalfOneHalf[2][3] = 1.0/np.sqrt(2.0)
prodThreeHalfOneHalf[2][4] = 1.0/np.sqrt(2.0)

# J = 2 mJ = -1
# (-,-) (--, +)
prodThreeHalfOneHalf[3][5] = np.sqrt(3.0/4.0)
prodThreeHalfOneHalf[3][6] = 0.5

# J = 2 mJ = -2
prodThreeHalfOneHalf[4][7] = 1.0

# J = 1 mJ = 1 (++,-) (+,+) 
prodThreeHalfOneHalf[5][1] = np.sqrt(3.0/4.0)
prodThreeHalfOneHalf[5][2] = -0.5

# J = 1 mJ = 0 (+,-) (-,+)
prodThreeHalfOneHalf[6][3] = 1.0/np.sqrt(2.0)
prodThreeHalfOneHalf[6][4] = -1.0/np.sqrt(2.0)

# J = 1 mJ = -1 (-,-) (--,+)
prodThreeHalfOneHalf[7][5] = 0.5
prodThreeHalfOneHalf[7][6] = -np.sqrt(3.0/4.0)

#
# (++,+) (++,0) (++,-) (+,+) (+,0) (+,-) (-,+) (-,0) (-,-) (--,+) (--,0) (--,-)
#

# J = 5/2 mJ = 5/2
# (++,+)
prodThreeHalfOne[0][0] = 1.0

# J = 5/2 mJ = 3/2
# (++,0) (+,+)
prodThreeHalfOne[1][1] = np.sqrt(2.0/5.0)
prodThreeHalfOne[1][3] = np.sqrt(3.0/5.0)

# J = 5/2 mJ = 1/2
# (++,-) (+,0) (-,+)
prodThreeHalfOne[2][2] = 1.0 / np.sqrt(10.0)
prodThreeHalfOne[2][4] = np.sqrt(3.0/5.0)
prodThreeHalfOne[2][6] = np.sqrt(3.0/10.0)

# J = 5/2 mJ = -1/2
# (+,-) (-,0) (--,+)
prodThreeHalfOne[3][5] = np.sqrt(3.0/10.0)
prodThreeHalfOne[3][7] = np.sqrt(3.0/5.0)
prodThreeHalfOne[3][9] = 1.0 / np.sqrt(10.0)

# J = 5/2 mJ = -3/2
# (-,-) (--,0)
prodThreeHalfOne[4][8]  = np.sqrt(3.0/5.0)
prodThreeHalfOne[4][10] = np.sqrt(2.0/5.0)

# J = 5/2 mJ = -5/2
# (--,-)
prodThreeHalfOne[5][11] = 1.0

# J = 3/2 mJ = 3/2
# (++,0) (+,+)
prodThreeHalfOne[6][1] = np.sqrt(3.0/5.0)
prodThreeHalfOne[6][3] = -np.sqrt(2.0/5.0)

# J = 3/2 mJ = 1/2
# (++,-) (+,0) (-,+)
prodThreeHalfOne[7][2] = np.sqrt(2.0/5.0)
prodThreeHalfOne[7][4] = 1.0 / np.sqrt(15.0)
prodThreeHalfOne[7][6] = -np.sqrt(8.0/15.0)

# J = 3/2 mJ = -1/2
# (+,-) (-,0) (--,+)
prodThreeHalfOne[8][5] =  np.sqrt(8.0/15.0)
prodThreeHalfOne[8][7] = -1.0 / np.sqrt(15.0)
prodThreeHalfOne[8][9] = -np.sqrt(2.0/5.0)

# J = 3/2 mJ = -3/2
# (-,-) (--,0)
prodThreeHalfOne[9][8]  =  np.sqrt(2.0/5.0)
prodThreeHalfOne[9][10] = -np.sqrt(3.0/5.0)

# J = 1/2 mJ = 1/2
# (++,-) (+,0) (-,+)
prodThreeHalfOne[10][2] = 1.0 / np.sqrt(2.0)
prodThreeHalfOne[10][4] = -1.0 / np.sqrt(3.0)
prodThreeHalfOne[10][6] = 1.0 / np.sqrt(6.0)

# J = 1/2 mJ = -1/2
# (+,-) (-,0) (--,+)
prodThreeHalfOne[11][5] = 1.0 / np.sqrt(6.0)
prodThreeHalfOne[11][7] = -1.0 / np.sqrt(3.0)
prodThreeHalfOne[11][9] = 1.0 / np.sqrt(2.0)

# (++,+) (++,-) (+,+) (+,-) (0,+) (0,-) (-,+) (-,-) (--,+) (--,-)

# J = 5/2 mJ = 5/2
# (++,+)
prodTwoOneHalf[0][0] = 1.0

# J = 5/2 mJ = 3/2
# (++,-) (+,+)  
prodTwoOneHalf[1][1] = 1.0/np.sqrt(5.0)
prodTwoOneHalf[1][2] = 2.0/np.sqrt(5.0)

# J = 5/2 mJ = 1/2
# (+,-) (0,+)
prodTwoOneHalf[2][3] = np.sqrt(2.0/5.0)
prodTwoOneHalf[2][4] = np.sqrt(3.0/5.0)

# J = 5/2 mJ = -1/2
# (0,-) (-,+)
prodTwoOneHalf[3][5] = np.sqrt(3.0/5.0)
prodTwoOneHalf[3][6] = np.sqrt(2.0/5.0)

# J = 5/2 mJ = -3/2
# (-,-) (--,+)
prodTwoOneHalf[4][7] = 2.0/np.sqrt(5.0)
prodTwoOneHalf[4][8] = 1.0/np.sqrt(5.0)

# J = 5/2 mJ = -5/2
# (--,-)
prodTwoOneHalf[5][9] = 1.0

# J = 3/2 mJ = 3/2
# (++,-) (+,+)  
prodTwoOneHalf[6][1] = 2.0/np.sqrt(5.0)
prodTwoOneHalf[6][2] = -1.0/np.sqrt(5.0)

# J = 3/2 mJ = 1/2
# (+,-) (0,+)
prodTwoOneHalf[7][3] = np.sqrt(3.0/5.0)
prodTwoOneHalf[7][4] = -np.sqrt(2.0/5.0)

# J = 3/2 mJ = -1/2
# (0,-) (-,+)
prodTwoOneHalf[8][5] = np.sqrt(2.0/5.0)
prodTwoOneHalf[8][6] = -np.sqrt(3.0/5.0)

# J = 3/2 mJ = -3/2
# (-,-) (--,+)
prodTwoOneHalf[9][7] =  1.0/np.sqrt(5.0)
prodTwoOneHalf[9][8] = -2.0/np.sqrt(5.0)


# (++,+) (++,0) (++,-) (+,+) (+,0) (+,-) (0,+) (0,0) (0,-) (-,+) (-,0) (-,-) (--,+) (--,0) (--,-)

# J = 3 mJ = 3
# (++,+)
prodTwoOne[0][0] = 1.0

# J = 3 mJ = 2
# (++,0) (+,+)
prodTwoOne[1][1] = 1.0/np.sqrt(3.0)
prodTwoOne[1][3] = np.sqrt(2.0/3.0)

# J = 3 mJ = 1
# (++,-) (+,0) (0,+) 
prodTwoOne[2][2] = 1.0/np.sqrt(15.0)
prodTwoOne[2][4] = np.sqrt(8.0/15.0)
prodTwoOne[2][6] = np.sqrt(2.0/5.0)

# J = 3 mJ = 0
# (+,-) (0,0) (-,+)
prodTwoOne[3][5] = 1.0/np.sqrt(5.0)
prodTwoOne[3][7] = np.sqrt(3.0/5.0)
prodTwoOne[3][9] = 1.0/np.sqrt(5.0)

# J = 3 mJ = -1
# (0,-) (-,0) (--,+)
prodTwoOne[4][8] = np.sqrt(2.0/5.0)
prodTwoOne[4][10] = np.sqrt(8.0/15.0)
prodTwoOne[4][12] = 1.0/np.sqrt(15.0)

# J = 3 mJ = -2
# (-,-) (--,0)
prodTwoOne[5][11] = np.sqrt(2.0/3.0)
prodTwoOne[5][13] = 1.0/np.sqrt(3.0)

# J = 3 mJ = -3
# (--,-)
prodTwoOne[6][14] = 1.0

# J = 2 mJ = 2
# (++,0) (+,+)
prodTwoOne[7][1] = np.sqrt(2.0/3.0)
prodTwoOne[7][3] = -1.0/np.sqrt(3.0)

# J = 2 mJ = 1
# (++,-) (+,0) (0,+) 
prodTwoOne[8][2] = 1.0/np.sqrt(3.0)
prodTwoOne[8][4] = 1.0/np.sqrt(6.0)
prodTwoOne[8][6] = -1.0/np.sqrt(2.0)

# J = 2 mJ = 0
# (+,-) (0,0) (-,+)
prodTwoOne[9][5] = 1.0/np.sqrt(2.0)
prodTwoOne[9][9] = -1.0/np.sqrt(2.0)

# J = 2 mJ = -1
# (0,-) (-,0) (--,+)
prodTwoOne[10][8]  = 1.0/np.sqrt(2.0)
prodTwoOne[10][10] = -1.0/np.sqrt(6.0)
prodTwoOne[10][12] = -1.0/np.sqrt(3.0)

# J = 2 mJ = -2
# (-,-) (--,0)
prodTwoOne[11][11] = 1.0/np.sqrt(3.0)
prodTwoOne[11][13] = -np.sqrt(2.0/3.0)

# J = 1 mJ = 1
# (++,-) (+,0) (0,+) 
prodTwoOne[12][2] = np.sqrt(3.0/5.0)
prodTwoOne[12][4] = -np.sqrt(3.0/10.0)
prodTwoOne[12][6] = 1.0/np.sqrt(10.0)

# J = 1 mJ = 0
# (+,-) (0,0) (-,+)
prodTwoOne[13][5] = np.sqrt(3.0/10.0)
prodTwoOne[13][7] = -np.sqrt(2.0/5.0)
prodTwoOne[13][9] = np.sqrt(3.0/10.0)

# J = 1 mJ = -1
# (0,-) (-,0) (--,+)
prodTwoOne[14][8]  = 1.0/np.sqrt(10.0)
prodTwoOne[14][10] = -np.sqrt(3.0/10.0)
prodTwoOne[14][12] = np.sqrt(3.0/5.0)

CG_dict = [[[2.0,1.0],[2.0,0.5],[1.5,1.0],[1.5,0.5],[1.0,1.0],[1.0,0.5],[0.5,0.5]],[prodTwoOne,prodTwoOneHalf,prodThreeHalfOne,prodThreeHalfOneHalf,prodOneOne,prodOneOneHalf,prodOneHalfOneHalf]]

def get_mvalues(j):
    dj = int(2*j+1)
    return np.linspace(j,-j,num=dj)

def get_jvalues(j1,j2):
    jmin = abs(j1 - j2)
    jmax = j1 + j2
    nj = int(jmax + 1 - jmin)
    return [val for val in np.linspace(jmax,jmin,num=nj)]
    
class SpinObj:
    def __init__(self, j = 1.0):
        self.j = j
        self.mlist = get_mvalues(self.j)

class IsospinComposite:
    def __init__(self, j1 = 1.0, j2 = 1.0):
        self.j1 = j1
        self.j2 = j2
        self.jmin = abs(j1-j2)
        self.jmax = j1 + j2
        self.nj = int(self.jmax + 1 - self.jmin)
        self.jlist = get_jvalues(self.j1,self.j2)
        self.mlist = []    
        for j in self.jlist:
            self.mlist.append([val for val in get_mvalues(j)])
    def get_uncoupled_basis(self):
        c = []
        a = get_mvalues(self.j1)
        b = get_mvalues(self.j2)
        for ea in a:
            for eb in b:
                c.append([ea,eb])
        return c
    def get_coupled_basis(self):
        return [self.jlist, self.mlist, [int(2*j+1) for j in self.jlist]]
    def get_ucb_index(self,m):
        ucb = self.get_uncoupled_basis()
        tmp = []
        for i in range(0,len(ucb)):
            if (sum(ucb[i]) == m):
                tmp.append(i)
        return tmp
    def get_cg_col_info(self):
        ucb = self.get_uncoupled_basis()
        cb = self.get_coupled_basis()
        print("Info on building blocks for coupled states --- column indices in the CG matrix.")
        print("Set of J values = " + str(cb[0]) + "\n")
        for i in range(0,len(cb[0])):
            for mJ in cb[1][i]:
                idx = self.get_ucb_index(mJ)
                print("m = " + str(mJ) + ", Index set = " + str(idx) + ", (m1,m2) building blocks = " + str([ucb[elem] for elem in idx]))
            print("\n")
    def get_cg_row_index(self,j,m):
        cb = self.get_coupled_basis()
        #print(cb)
        idx = cb[0].index(j)
        #print(idx)
        iy = idx
        sum = 0
        for k in range(0,iy):
            sum += cb[2][k]
        midx = cb[1][iy].index(m)
        iz = sum + midx
        return iz
        
class TPIsospinComposite:
    def __init__(self,j1=1.0,j2=1.0,j3=1.0):
        if(j1 == 0.0 or j2 == 0.0 or j3 == 0.0):
            raise ValueError('Zero spin not supported at the moment.')
        self.j1 = j1
        self.j2 = j2
        self.j3 = j3
        self.Imax = self.j1 + self.j2 + self.j3
        self.mImin = 0.0
        if (int(2 * self.Imax) % 2 == 1):
            self.mImin = 0.5
        self.Dimer=IsospinComposite(j1,j2)
        self.Spectator=SpinObj(j3)
        self.DimerSpectatorList = [IsospinComposite(j,j3) for j in self.Dimer.jlist]
        self.j1basis = get_mvalues(j1)
        self.j2basis = get_mvalues(j2)
        self.j3basis = get_mvalues(j3)
        self.TPuncoupledbasis = []
        self.TPIzerochannelbasis = []
        for i in self.j1basis:
            for j in self.j2basis:
                for k in self.j3basis:
                    tmp = [i,j,k]
                    self.TPuncoupledbasis.append(tmp)
        for elem in self.TPuncoupledbasis:
            if(sum(elem) == self.mImin):
                self.TPIzerochannelbasis.append(elem)
        sizeCC = len(self.TPIzerochannelbasis)
        self.CaligraphicC = np.zeros((sizeCC,sizeCC),dtype=np.complex128)
        self.Iset = [get_jvalues(j,j3) for j in self.Dimer.jlist]
        self.Ilist = []
        self.Ishelllist = []
        for j in self.Dimer.jlist:
            tmp = get_jvalues(j,j3)
            self.Ishelllist.append(tmp)
            for elem in tmp:
                if elem not in self.Ilist:
                    self.Ilist.append(elem)
    def get_Ishell_ancestors(self):
        idxlist = []
        vallist = []
        for Ival in self.Ilist:
            tmp = []
            valtmp = []
            for elem in self.Dimer.jlist:
                i = self.Dimer.jlist.index(elem)
                for ite in self.Ishelllist[i]:
                    if(ite == Ival):
                        tmp.append([i,self.Ishelllist[i].index(ite)])
                        valtmp.append(elem)
            idxlist.append(tmp)
            vallist.append(valtmp)
        return idxlist,vallist
    def print_Ishell_composition(self):
        x,y = self.get_Ishell_ancestors()
        print("Total isospin in descending order:\n")
        for Ival in self.Ilist:
            print("I3 = " + str(Ival) + " contains:")
            for elem in y[self.Ilist.index(Ival)]:
                print("  J2 = " + str(elem))
    def set_CaligraphicC(self):
        innerObj = IsospinComposite(self.j1,self.j2)
        iucb = innerObj.get_uncoupled_basis()
        calc_row_counter = 0
        x,y = self.get_Ishell_ancestors()
        for Ival in self.Ilist:
            jlist = y[self.Ilist.index(Ival)]
            for j in jlist:
                outerObj = IsospinComposite(j,self.j3)
                cg_row_index = outerObj.get_cg_row_index(Ival,self.mImin)
                cg_col_index_list = outerObj.get_ucb_index(self.mImin)
                ucb = outerObj.get_uncoupled_basis()
                for im in cg_col_index_list:
                    m = ucb[im][0]
                    icg_row_index = innerObj.get_cg_row_index(j,m)
                    icg_col_index_list = innerObj.get_ucb_index(m)
                    for iidx in icg_col_index_list:
                        tpucbelem = [iucb[iidx][0],iucb[iidx][1],ucb[im][1]]
                        calc_col_index = self.TPIzerochannelbasis.index(tpucbelem)
                        cg_outer_match_list = [j,self.j3]
                        cg_inner_match_list = [self.j1,self.j2]
                        if (j != 0.0):
                            X = CG_dict[1][CG_dict[0].index(cg_outer_match_list)]
                            Y = CG_dict[1][CG_dict[0].index(cg_inner_match_list)]
                            f1 = X[cg_row_index,im]
                            f2 = Y[icg_row_index,iidx]
                        else:
                            f1 = 1.0
                            Y = CG_dict[1][CG_dict[0].index(cg_inner_match_list)]
                            f2 = Y[icg_row_index,iidx]
                        self.CaligraphicC[calc_row_counter,calc_col_index] = f1 * f2
                calc_row_counter+=1
# ToDo list: 
# 1) Check that Caligraphic C is an orthogonal matrix 
# 2) Automatic computation of the CG coefficients using the recursion formula
# 3) Change Caligraphic to Calligraphic :P