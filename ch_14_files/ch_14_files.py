import os
import dbm
import wc

def main():
    # write_to_a_file()

    # dirname1 = 'ch_8_strings'
    # walk_without_git(dirname1)
    # dirname2 = os.getcwd()
    # walk_without_git(dirname2)

    # create_database('./ch_14_files/myFirstDB/captions')
    print(wc.linecount('./ch_14_files/wc.py'))



def create_database(name):
    db = dbm.open(name, 'c')
    db['cleese.png'] = 'Photo of John Cleese.'
    print(db['cleese.png'])
    db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
    print(db['cleese.png'])
    
    for key in db:
        print(key, db[key])

    db.close()
    return    

def walk_without_git(dirname):
    for name in os.listdir(dirname):
        if '.git' not in name:
            path = os.path.join(dirname, name)

            if os.path.isfile(path):
                print(path)
            else:
                walk_without_git(path)
    return


def write_to_a_file():
    filename = './ch_14_files/testwrite.txt'
    
    # if the file does not exist, it is created
    fout = open(filename, 'w')
    line1 = 'hello, file!'
    fout.write(line1)
    fout.close()

    fin = open(filename)
    for line in fin:
        print(line)
    fin.close()

    # if it already exists, it is overwritten
    fout = open(filename, 'w')
    line2 = 'goodbye, old file!'
    fout.write(line2)
    fout.close()

    fin = open(filename)
    for line in fin:
        print(line)
    fin.close()        
    return


if __name__ == "__main__": main()