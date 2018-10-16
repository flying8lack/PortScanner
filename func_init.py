import sys



def Port_Report(Port):
    '''report if port is open'''
    return "Port "+str(Port)+" is Open."


def Port_Scan(Socket, Server, Max_Port):
    ''' the funcion that would do the scan'''
    
    try:
        for Port in range(1, Max_Port+1):
            Result = Socket.connect_ex((Server, Port))
            if Result == 0:
                Port_Report(Port)


    except KeyboardInterrupt:
            sys.exit()

    except Exception as e:
        print("Erorr has been encoutered.")
        print("Error:", str(e))
        


