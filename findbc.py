#coding=utf-8

##################################################################################################################
#    ____                                                                                                        #
#   /    \    ___     ___      ___   ___     ____    ___     ___     |                                           #
#   |____    /   \   /   \   |/     /   \   /       /   \   |     ---|---                                        #
#        |  |       |     |  |     |        -----  |     |  |---     |                                           #
#    ____/   \___/   \___/   |      \___/   ____/   \___/   |        |__/                                        #
#                                                                           Scorcsoft.com | 天蝎软件 2018-09-15  #
##################################################################################################################

import re
import sys
import getopt
import os.path

def usage(error=False):
    if error:
        print("%s\n"%(error))
    usage = '''usage: python findbc.py path [OPTIONS]

    -h\t\tshow help information
    -k\t\tkeyword
    -t\t\tfile type: only find with type file
    -o\t\toutput: save the result to output
    --type\tfile type: only find with type file
    

Example:
Find files containing abc:
python findbc ./ -k abc

Find files containing abc and save the result to result.txt:
python findbc ./ -k abc -o result.txt

Find the html,php,txt file containing abc:
python findbc ./ -k abc -t html,php,txt

Find the html file containing abc:
python findbc ./ -k abc --html'''
    print(usage)
    exit()


def key_scan(P,K,O):
    try:
        file = open(P,"r") 
        flag = re.search(K,file.read())
        file.close()
        if flag == None:
            pass
        else:
            print(P)
            if O: #找到一个就写入一个, 防止程序意外终止导致结果丢失
                file = open(O,"a+")
                file.write("%s\n"%(P))
                file.close()
    except IOError:
        pass


def file_type_check(P,K,T,O):
    if os.path.splitext(P)[1][1:] in T:
        key_scan(P,K,O)

def run(P,K,T,O):
    for dirs in os.walk(P):
        for i in dirs[2]:
            string = "%s/%s"%(dirs[0],i)
            if T:
                file_type_check(string,K,T,O)
            else:
                key_scan(string,K,O)
    if O:
        print("\n[*] The result has been saved to file %s"%(O))


def main():
    if len(sys.argv) < 2:
        usage()
    long_argv = ''


    try:
        argv_list = []
        for i in sys.argv[2:]:
            if i[0:2] == '--':
                long_argv = i[2:]
            else:
                argv_list.append(i)
        arg = getopt.getopt(argv_list,'-h-k:-t:-o:',[])


        P = sys.argv[1]
        if os.path.isdir(P) == False:
            if P == "-h":
                usage()
            print("[!] Error: %s is not a directory"%(P)) 


        K = O = ''
        T = []
        for opt_k,opt_v in arg[0]:
            if opt_k == "-h":
                usage()
            if opt_k == "-k":
                if opt_v == '':
                    usage("[!] Error: the keyword is null")
                K = opt_v
            if opt_k == "-t":
                T = opt_v.split(',')
            if opt_k == "-o":
                if opt_v != '':
                    file = open(opt_v,'w')
                    file.close()
                O = opt_v
        if K == '':
            usage("[!] Error: the keyword is null")
        if T == []:
            if long_argv != '':
                T.append(long_argv)

        run(P,K,T,O)
    except getopt.GetoptError:
        usage("[!] Error: the keyword is null")

main()