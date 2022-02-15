import dropbox

class TransferData:
    def __init__(self,access_token):
         self.access_token = access_token

    def upload_file(self, file_from, file_to):
            """upload a file to Dropbox using API v2
            """
            dbx=dropbox.Dropbox(self.access_token)

            with open(file_from, 'rb') as f:
             dbx.files_upload(f.read(), file_to)

def main():
    access_token ='sl.BCCt08Uord3knfcPJN-v_8CzDwyZcnoIXqZ2yE6J_o3i3fizI_1yy4_nMdfVva6Ws6Yqv2vkGf2ynuFNvEuczxA557XPduXirG-B0zpFHmQIoL4hQPeqwIUPBzaPmfV2Qk9RwiHdBnU'
    transferData= TransferData(access_token)

    file_from= input("Enter the file to be uploaded")
    file_to=input("Enter the full path to upload to dropbox: ")

     # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been successfully moved")

main()