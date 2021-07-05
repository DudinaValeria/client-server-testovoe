import socket
import time
import threading as thr
def reversing(word):
    word2=word[::-1]
    time.sleep(2)   
    return word2

def replacing (word):
    word2=''
    for i in range(0, len(word), 2) :
        try:
            word2 += word[i + 1] + word[i]
        except IndexError:
            word2+=word[len(word)-1]
            print(word2)
    time.sleep(5)
    return word2    

def worker_2(val, res):
    
    
    res.append(val[0])
    res.append('in process')
    res.append(val[2])
    res.append(val[3])
    result_line.append(res)
    time.sleep(15)
    
    if val[2]=='1':
        res[3]=reversing(val[3])
    elif val[2]=='2':
        res[3]=replacing(val[3])
    
    res[1]='done'
    
    print('function is done')
    
    
if __name__=='__main__':
   # waiting_line=[['in waiting line','rtyuio','1','qwerty']]
    global wairing_line
    global result_line
    waiting_line=[]
    result_line=[]
    
    id_=0
    j=-1
    d=[]
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind(('127.0.0.1', 9779))
    
    server.listen()
    
    
    while True:
        user_socket, adress=server.accept()
        print('Connected by', adress)
        
        
        flag=0
        #user_socket.send('your operation code: '.encode('utf-8'))
        while True:
            proc_code=user_socket.recv(2048).decode('utf-8')
            
            
            if proc_code=='w':
                print('procedure code: ', proc_code)
                
                word=user_socket.recv(2048).decode('utf-8')
                code=user_socket.recv(2048).decode('utf-8')
                print('data:',word, code)
                id_=id_+1
                user_socket.send((str(id_)).encode('utf-8'))
                
                d=[id_,'in waiting line', code, word]
                
                d2=[]
                waiting_line.append(d)
                t=thr.Thread(target=worker_2, args=(d,d2))
                
                t.start()
                
            if proc_code=='s':
                        
                print('procedure code: ',proc_code)
                my_id=user_socket.recv(2048).decode('utf-8')
                print('id: ',my_id)
                if len(result_line) < int(my_id):
                    user_socket.send('in waiting line'.encode('utf-8'))
                else:
                    for u in result_line:
                        if str(u[0])==my_id:
                            
                            
                            user_socket.send(str(u[1]).encode('utf-8'))
            
                    
            if proc_code=='r':
                        print('procedure code: ',proc_code)
                        my_id=user_socket.recv(2048).decode('utf-8')
                        print('id: ',my_id)
                        
                        fl=0
                        if len(result_line) <int(my_id):
                            user_socket.send('not done yet'.encode('utf-8'))
                        else:
                        
                            for wl in result_line:
                                if str(wl[0])==my_id:
                                    
                                    if wl[1]=='done':
                                        fl=1
                                        user_socket.send(wl[3].encode('utf-8'))
                            if fl==0:
                                user_socket.send('not done yet'.encode('utf-8'))
                                
            
                    
                        
            
                
  
    
        
        