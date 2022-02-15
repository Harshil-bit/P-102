from dropbox.files import WriteMode
import dropbox
import os
class TransferData:
    def __init__(self,access_token):
         self.access_token = access_token

    def upload_file(self, file_from, file_to):
            """upload a file to Dropbox using API v2
            """
            dbx=dropbox.Dropbox(self.access_token)
            for root,dirs,files in os.walk(file_from):
                for file_name in files:
                    localPath=os.path.join(root,file_name)
                    relativePath=os.path.relpath(localPath,file_from)
                    dropboxPath=os.path.join(file_to,relativePath)
            with open(localPath, 'rb') as f:
             dbx.files_upload(f.read(), dropboxPath,mode=WriteMode('overwrite'))

def main():
    access_token ='azkrkhpV1EMAAAAAAAAAAQQGAeb-8-mQToki0u2IYDVI2BnY5jtOIvYpQvOF-Czk'
    transferData= TransferData(access_token)

    file_from= str(input("Enter the file to be uploaded"))
    file_to=input("Enter the full path to upload to dropbox: ")

     # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been successfully moved")

main()