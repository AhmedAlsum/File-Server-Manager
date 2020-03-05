import socket
import os

def Main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connect((host, port))
    print("Connected Successfully!")
    Answer = raw_input("Enter 'upload' or 'download' : ")
    if(Answer == "download"):
        mssg = "download"
        s.send(mssg.encode())
        print(os.listdir("/home/ahmed/server/"))
        FileName = raw_input("Enter Filename to Download from server : ")
        Data = "Temp"

        while True:
            s.send(FileName.encode())
            Data = s.recv(1024)
            DownloadFile = open("/home/ahmed/client/"+FileName,"wb")
            i = 1
            while Data:
                print('Recieving...%d' %(i))
                DownloadFile.write(Data)
                Data = s.recv(1024)
                i = i + 1
            print("Done Recieving")
            DownloadFile.close()
            break
        
    elif(Answer == "upload"):
        mssg = "upload"
        s.send(mssg.encode())
        print(os.listdir("/home/ahmed/client/"))
        FileName = raw_input("Enter Filename to Upload On server : ")
        s.send(FileName.encode())

        UploadFile = open("/home/ahmed/client/"+FileName,"rb")
        Read = UploadFile.read(1024)
        i = 1
        while Read:
            print("Sending...%d" %(i))
            s.send(Read) #sends 1KB 
            Read = UploadFile.read(1024)
        print("Done Sending")
        UploadFile.close()

        
    s.close()


if __name__ == '__main__':
    Main()

