import os

def defineRule(old, new, rules):
    '''Define single rule: replace old with new
       and append the rule to rules(list)
    '''   
     
    rule = [old, new]
    rules.append(rule)  

def BatchChangeFileName(folder, rules):
    '''
    Change file names in folder, according to the rule defined
    '''
    
    files = os.listdir(folder)   
    
    for file in files:
        fullSourceName = os.path.normpath(os.path.join(folder, file))
        fullNewName = fullSourceName

        for rule in rules:      
            fullNewName = fullNewName.replace(rule[0], rule[1])
        
        # only change name when having differences   
        if not fullSourceName.__eq__(fullNewName):  
            os.rename(fullSourceName, fullNewName)        
            print (fullSourceName, 'is changed to', fullNewName)          


if __name__ == "__main__":    
    rules = []
    defineRule('.pdf', '', rules) 

    BatchChangeFileName(r'\\stonenas\video\Episodes\少年天子', rules)