def disp(v): for i in range(1,10,1):
        if(v[i]==i):
            print("-",end="")
        else:
            print(v[i],end=" ")
        if(i%3==0):
            print()
 v=[0,1,2,3,4,5,6,7,8,9]
 print("enter the position from1-9")
 disp(v)
 for c in range(0,9,1):
    if(c%2==0):
                   turn="x"
    else:
                   turn="0"
           while(True):
            try:
                val=int(input("play"+turn+":"))
            if(v[val]!="x" and v[val]!="0" val>0 an val<10):v[val]=turn;
                break;
                   print("this place is already occuied")
            except:
            print("enter valid input")
            disp(v)
    if(c>3):
            if(v[3]==v[5]==v[7]orv[1]==v[5]==v[9]):
                print("\n player"+turn+"win")
                break
            for i in range(1,4,1):
                    if(v[i]==v[i+3]==v[i+6]):
                        print("\n player"+turn+"win")
                        exit()
            for i in  range(1,8,3):
                    if(v[i]==v[i+1]==v[i+2]):
                        print("\n player "+turn+"win")
                        exit()
                    if(c==8):
                        print("it is a draw")



