# how to write in a file


path = "S:/LTTS/Python stuff/5g_stuff/Paging/UE/Paging_request.txt"
file = open(path, 'a')
st = " Action is preformed successfully"
file.write(st)
file = open(path, 'r')
readfile = file.read()
if st  in readfile:
    print('YEsh its done')
else:
    print('its not done')
file.close()

