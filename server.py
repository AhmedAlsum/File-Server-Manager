import threading 
import socket
import os

online_user = []
class RecieveFiles(threading.Thread):

    def __init__ (self,c):
        threading.Thread.__init__(self)
        self._c =c

    def run(self):
        data = self._c.recv(1024)
        if (data.decode() == "download"):
            print(os.listdir("/home/ahmed/server/")) #Shows all the files at server side    
            FileName = self._c.recv(1024)
            for file in os.listdir("/home/ahmed/server/"):
                if file == FileName.decode():
                    FileFound = 1
                    break

            if FileFound == 0:
                print(" Not Found On Server")

            else:
                print("File Found")
                upfile = FileName.decode()
                UploadFile = open("/home/ahmed/server/"+upfile,"rb")
                Read = UploadFile.read(1024)
                i = 1
                while Read:
                    print("Sending...%d" %(i))
                    self._c.send(Read)  
                    Read = UploadFile.read(1024)
                print("Done Sending")
                UploadFile.close()
                
                self._c.close()

        elif (data.decode() == "upload"):
            FileName = self._c.recv(1024)
            downfile = FileName.decode()
            Data = self._c.recv(1024)
            DownloadFile = open("/home/ahmed/server/"+downfile,"wb")
            i = 1
            while Data:
                print('Recieving...%d' %(i))
                DownloadFile.write(Data)
                Data = self._c.recv(1024)
                i = i + 1
            print("Done Recieving")
            DownloadFile.close()
            self._c.close()

def main():
    try:
        print "Starting the server up"
        s=socket.socket()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0',5000))
        s.listen(5)
        while True:
            c ,addr = s.accept()
            print "client %s connected" %str(addr)
            u = RecieveFiles(c)
            print "started thread for sending and recieving files"
            u.start()
        s.close()
    except :
        pass

    finally :
        print "Server Shutdown"
    



if __name__ == "__main__":
    main()
