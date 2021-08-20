import dropbox

class TransferData: 
    def __init__(self,access_token):
        self.access_token = access_token
        
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'sl.A269ZQyyg5rDfxe1vAKn5JIcVzeAZMKi0Oy7_AU9gswEga-Q2cRBit10swzIZuJLd-jZFe8eiHl5n2b7bVPLHnoiHjYqi3mHXUDpmO35JcxZQQIc7sT8QyR9JrotOriTtrutGPE'
    transferData = TransferData(access_token)
    #file_from = 'test.txt'
    #file_to = '/test_dropbox/test.txt'
    file_from = input('Enter the file you want to transfer: ')
    file_to = input('Enter the full path to enter to dropbox: ')
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

if __name__ == '__main__':
    main()
