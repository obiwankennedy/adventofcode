#!/usr/bin/python3

import json

inputVal= """!alias maul !d20+4 #bite attack"""

inputVal="""!alias rm maul"""
inputVal= """!alias maul
!d20+4 #bite attack
!d8+4 #bite dmg
!d20+4 #claw atk
!2d6+4 #claw dmg"""

inputVal="""!maul"""



idServer="11111"
aliases={}
AllAliases={}
commands=[]
aliasName=""
addAlias=False
removeAlias=False
firstLine=True
if(inputVal.startsWith("!alias")):
    for line in inputVal.splitlines():
        tab=line.split(' ')
        if(not addAlias and not removeAlias and firstLine):
            if(tab[0] == "!alias"):
                if(tab[1] == "rm"):
                    removeAlias=True
                    aliasName=tab[2]
                else:
                    addAlias=True
                    aliasName=tab[1]

        if(addAlias):
            if(firstLine):
                cmd=""
                for i in range(2,len(tab)):
                    if(i!=tab[0]):
                        cmd+=str(tab[i])+" "
                if(len(cmd)>0):
                    commands.append(cmd)
            else:
                commands.append(line)

        firstLine=False

    if( idServer not in AllAliases):
        AllAliases.update({str(idServer):{}})

    val = AllAliases[idServer]
    if(addAlias):
        val.update({str(aliasName):commands})   
    elif(removeAlias):
        del val[aliasName]


    print(AllAliases)

    print(json.dumps(AllAliases,indent=4))

else:
    inputVal=inputVal.replace('!','')
    if ( idServer in AllAliases):
        val = AllAliases[idServer]
        if(inputVal in val):
            cmds=val[inputVal]
            for line in cmds:
                print("roll dice"+str(line))
    else
        print("roll dice"+str(inputVal))


