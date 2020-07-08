import re


def main():
    sed('way', '___', './ch_14_files/source.txt', './ch_14_files/destination.txt')


def sed(patternStr, replacementStr, filenameIn, filenameOut):
    '''open filenameIn, read the content and copy it to filenameOut. 
    Create filenameOut if not existing, else rewrite its content
    If patternStr occurs while reading filenameIn, replace it in filenameOut with replacementStr. 
    '''
    try:
        fin = open(filenameIn, 'r')
    except:
        print('invalid source file')
        return

    try:
        fout = open(filenameOut, 'w')    
    except:
        print('invalid destination file')
        return
    
    try:
        for lineIn in fin:
            if patternStr in lineIn:
                temp = re.split(patternStr, lineIn)
                lineOut = replacementStr.join(temp)
            else:
                lineOut = lineIn
            fout.write(lineOut)
        
        fin.close()
        fout.close()
    except:
        print('something went wrong')


if __name__ == "__main__":
    main()