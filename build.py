#! /usr/bin/python2.7
# coding=utf-8
# vim:expandtab:ts=4:sw=4:
# 
import time
import re
import os
import sys
import shutil
import platform

curpath=os.getcwd();#当前文件目录
binfile=os.path.join(curpath,"bin")
def clean():
    if os.path.exists( binfile ):
        print "  remove local assets: %s" % binfile 
        shutil.rmtree( binfile ,True)

def buildfrp(name):
    frpspath=os.path.join(curpath,"cmd/"+name)
    os.chdir( frpspath )
    ret = os.system( "go build" )
    if ret != 0:
        print "build "+name+" Error!"
        return
    print "build "+name+" success!"
    target=os.path.join(binfile,name+"/")
    if os.path.exists( target )==False:
        os.makedirs(target)
    sysstr = platform.system()
    if sysstr=="windows":
        shutil.copyfile(os.path.join(frpspath,name+".exe"),os.path.join(target,name+".exe"))
    else:
        shutil.copyfile(os.path.join(frpspath,name),os.path.join(target,name))
    print "copy "+name+" success!"
    os.chdir( curpath )


if __name__=="__main__":
   clean()
   buildfrp("frps")
   buildfrp("frpc")
