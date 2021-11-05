import os

def unlock():

    #Unlock the folder
    pw = "password"

    # while True:
    pw1 = input('Enter the password : ')
    if pw1 == pw:
        os.chdir("S:/folder")
        if not os.path.exists("Locker"):
            if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                os.mkdir("Locker")
                print("Locker Folder Successfully created")

            else:
                os.popen('attrib -h -s -r Locker')
                os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")
                print("Locker Folder has been Successfully Unlocked")
                # break

        else:
            print("Locker folder is not LOCKED")

    else:
        print("wrong password! Try again later")



def lock():      #lock the folder

    p_w = "password"

    # while True:
    pw1 = input('Enter the password : ')
    if p_w == pw1:
        os.chdir("S:/folder")
        # print("Your path Successfully Changed")
        # If Locker folder or Recycle bin does not exist then we will be create Locker Folder

        if os.path.exists("Locker"):
            os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
            print("Locker folder has been successfully locked")
            # sys.exit()
            # break

        else:
            os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.mkdir("Locker")
            print("Locker Folder Successfully created")
            os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
            print("Locker folder has been successfully locked")
            # break

    else:
        print("wrong password! Try again later")
        # break


lock()
unlock()