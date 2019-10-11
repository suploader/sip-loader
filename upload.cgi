#!/usr/local/bin/python
# -*- coding: EUC-JP -*-
 
import cgi
import cgitb; cgitb.enable()
import os, sys
 
print "Content-Type: text/html; charset=EUC-JP"
print
 
UPLOAD_DIR = "./upload"
 
def save_uploaded_file (upload_dir):
    form = cgi.FieldStorage()
    if not form.has_key("file"):
        print "ファイルを入力してください"
        return
    fileitem = form["file"]
    if not fileitem.file:
        print "ファイルを入力してください"
        return
 
    if not fileitem.filename:
        print "ファイルを入力してください"
        return
 
    if form["name"].value is "":
        print "名前を入力してください"
        return
 
    fout = file (os.path.join(upload_dir, form["name"].value + os.path.basename(fileitem.filename)), 'wb')
    while 1:
        chunk = fileitem.file.read(100000)
        if not chunk: break
        fout.write (chunk)
    fout.close()
    print "送信しました"
 
save_uploaded_file(UPLOAD_DIR)
