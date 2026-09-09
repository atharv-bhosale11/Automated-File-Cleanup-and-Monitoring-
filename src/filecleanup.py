import os
import sys
import time
import schedule

def DirectoryScanner(DirName):
    
    try:
        StartTime = time.time()
        TimeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        Border = "-"*52
        
        LogFileName = "FileLog_" + TimeStamp + ".log"
        fobj = open(LogFileName,"w")

        fobj.write(Border +"\n")
        fobj.write("Automated File Cleanup and Monitoring\n")
        fobj.write("Execution Log\n")
        fobj.write(Border +"\n")
        Ret = False

        Ret = os.path.exists(DirName)

        if Ret==False:
            print("There is No such Directory")
            return
        
        Ret = os.path.isdir(DirName)

        if Ret == False:
            print("It is not directory")
            return

        FileCount = 0
        EmptyFileCount = 0
        DeletedFileCount = 0
        FailedFileCount = 0

        for FolderName,SubFolder,FileName in os.walk(DirName):

            for fname in FileName:
                FileCount = FileCount + 1
                fname=os.path.join(FolderName,fname)

                try:

                    if(os.path.getsize(fname)==0):      #empty file
                        EmptyFileCount = EmptyFileCount + 1
                        fobj.write("Deleted File: " + fname + "\n")
                        os.remove(fname)
                        DeletedFileCount = DeletedFileCount + 1

                except PermissionError:

                    FailedFileCount = FailedFileCount + 1

                    print("Permission Denied: ",fname)
                    fobj.write("Permission Denied: "+ fname + "\n")
                
                except OSError as e:
                    FailedFileCount = FailedFileCount + 1

                    print("Error while processing: ",fname)
                    fobj.write("Error: "+ str(e) + "\n")
            
        EndTime = time.time()
        ExceutionTime = EndTime - StartTime 

        fobj.write("\n")
        fobj.write(Border + "\n")
        fobj.write("EXECUTION SUMMARY\n")
        fobj.write(Border + "\n")

        fobj.write("Directory Scanned       :"+DirName + "\n")
        fobj.write("Total Files Scanned     :"+str(FileCount) + "\n")
        fobj.write("Empty Files Found       :"+str(EmptyFileCount) + "\n")
        fobj.write("Files Deleted           :"+str(DeletedFileCount) + "\n")
        fobj.write("Files Failed            :"+str(FailedFileCount) + "\n")
        fobj.write("Execution Time          :"+str(round(ExceutionTime, 2)) + " seconds\n")
        fobj.write("Status                  : SUCCESS\n")
        
        fobj.write(Border + "\n")

        fobj.close()

        print("Log File Created         : ",LogFileName)
    
    except Exception as e:
        print("Unexpedted Error: ",e)


def main():
    Border = "-"*52
    print(Border)
    print("---------------------Automation Suite---------------")
    print(Border+"\n")

    if(len(sys.argv)!=2):
        print("Invalid number of arguments")
        print("Please!! Specify the Name of Directory")
        return

    DirectoryName = sys.argv[1]

    print("Directory to Scan        : ",DirectoryName)

    schedule.every(1).minutes.do(DirectoryScanner, DirectoryName)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Automated-File-Cleanup-and-Monitoring- stopped by the user"+"\n")

    print(Border)
    print("--------------------Automation Suite Ends-----------")
    print(Border)

if __name__ == "__main__":
    main()
