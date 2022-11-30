import numpy as np

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
        self.Dimer=IsospinComposite(j1,j1)
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
            if(sum(elem) == 0.0):
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
        return
        # Use shell ancestors 
        # inner and outer tmp. IsoSpinComposite objects 
        # row, column indices, m values