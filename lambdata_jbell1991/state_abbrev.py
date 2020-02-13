class State:

    country = 'US State'

    def __init__(self, name, abv):
        self.name = name
        self.abv = abv

class Territory(State):

    country = 'US Territory'

    def __init__(self, name, abv, inhabited=True):
      super().__init__(name, abv)
      self.inhabited = inhabited 



if __name__ == "__main__":

    AL = State('Alabama', 'AL')
    AK = State('Alaska', 'AK')
    AZ = State('Arizona', 'AZ')
    AR = State('Arkansas', 'AR')
    AS = Territory('American Samoa', 'AS')
    CA = State('California', 'CA')
    CO = State('Colorado', 'CO')
    CT = State('Connecticut', 'CT')
    DE = State('Delaware', 'DE')
    DC = State('District of Columbia', 'DC')
    FL = State('Florida', 'FL')
    GA = State('Georgia', 'GA')
    GU = Territory('Guam', 'GU')
    HI = State('Hawaii', 'HI')
    ID = State('Idaho', 'ID')
    IL = State('Illinois', 'IL')
    IN = State('Indiana', 'IN')
    IA = State('Iowa', 'IA')
    KS = State('Kansas', 'KS')
    KY = State('Kentucky', 'KY')
    LA = State('Louisiana', 'LA')
    ME = State('Maine', 'ME')
    MD = State('Maryland', 'MD')
    MA = State('Massachusetts', 'MA')
    MI = State('Michigan', 'MI')
    MN = State('Minnesota', 'MN')
    MS = State('Mississippi', 'MS')
    MO = State('Missouri', 'MO')
    MT = State('Montana', 'MT')
    NE = State('Nebraska', 'NE')
    NV = State('Nevada', 'NV')
    NH = State('New Hampshire', 'NH')
    NJ = State('New Jersey', 'NJ')
    NM = State('New Mexico', 'NM')
    NY = State('New York', 'NY')
    NC = State('North Carolina', 'NC')
    ND = State('North Dakota', 'ND')
    MP = Territory('Northern Mariana Islands', 'MP')
    OH = State('Ohio', 'OH')
    OK = State('Oklahoma', 'OK')
    OR = State('Oregon', 'OR')
    PA = State('Pennsylvania', 'PA')
    PR = Territory('Puerto Rico', 'PR')
    RI = State('Rhode Island', 'RI')
    SC = State('South Carolina', 'SC')
    SD = State('South Dakota', 'SD')
    TN = State('Tennessee', 'TN')
    TX = State('Texas', 'TX')
    UT = State('Utah', 'UT')
    VT = State('Vermont', 'VT')
    VI = Territory('Virgin Islands', 'VI')
    VA = State('Virginia', 'VA')
    WA = State('Washington', 'WA')
    WV = State('West Virginia', 'WV')
    WI = State('Wisconsin', 'WI')
    WY = State('Wyoming', 'WY')
