stco = ['09001','09005','09009','34003','34013','34017','34019','34021',\
        '34023','34025','34027','34029','34031','34035','34037','34039','34041',\
        '36005','36047','36061','36081','36085','36027','36071','36079',\
        '36087','36105','36111','36119','36059','36103']  

sub = {'09001':'CT','09005':'CT','09009':'CT',\
       '34003':'NJ','34013':'NJ','34017':'NJ','34019':'NJ','34021':'NJ','34023':'NJ','34025':'NJ',\
        '34027':'NJ','34029':'NJ','34031':'NJ','34035':'NJ','34037':'NJ','34039':'NJ','34041':'NJ',\
        '36005':'NYC','36047':'NYC','36061':'NYC','36081':'NYC','36085':'NYC','36027':'HV','36071':'HV',\
        '36079':'HV','36087':'HV','36105':'HV','36111':'HV','36119':'HV','36059':'LI','36103':'LI'}

stco_2 = {'09':['001','005','009'],\
        '34':['003','013','017','019','021','023','025','027','029',\
              '031','035','037','039','041'],\
        '36':['005','027','047','059','061',\
         '071','079','081','085','087','103','105','111','119']}

sub_2 = {'CT':['09001','09005','09009'],\
       'NJ':['34003','34013','34017','34019','34021','34023','34025','34027',\
       '34029','34031','34035','34037','34039','34041'],\
       'NYC':['36005','36047','36061','36081','36085'],\
       'HV':['36027','36071','36079','36087','36105','36111','36119'],\
       'LI':['36059','36103']}