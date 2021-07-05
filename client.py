import socket
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 9779))
print('\n Type code of operation \n w - to input new word \n s - to get status of oparetion \n r - to get result of operation')
while True:
    
    proc=input('type code: ')
    client.send(proc.encode('utf-8'))
    
    
    if proc=='w':
        data_word=input('word: ')
        client.send(data_word.encode('utf-8'))
        print('\n Types of operations: \n 1 - revers all letters \n 2 - replace neighbouring letters')
        client.send(input('type: ').encode('utf-8'))
        code=client.recv(2048).decode('utf-8')
        print('Your request code is ', code)
        print('\n operation is started\n what you want to do next?')
        
        
    if proc=='s':        
        my_id=input('input your id: ')
        client.send(my_id.encode('utf-8'))
        status_code=client.recv(2048).decode('utf-8')
        print('status of operation: ',status_code)
    if proc=='r':
        
        my_id=input('input your id: ')
        client.send(my_id.encode('utf-8'))
        result=client.recv(2048).decode('utf-8')
        if result =='not done yet':
            print(result)
        else:
            print('result: ',result)
            
        
        