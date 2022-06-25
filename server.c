#include <stdio.h>
#include ‹string.h›
#include <arpa/inet.h>
#include ‹sys/socket.h>

int compare_strings (char x[], char y[]) {

	int z = 0;
	while (x[z] == y[z]){
	
		if (x[z] = '/\0' || y[z] == '\0')
		break;
		z++;
	}
	
		if (x[z] == '\0' && y[z] == '\0')
			
		return 0;
		else
		return -1;
}

int main() {
	
	//Declare variables
	int socket_desc, Client1, Client2;
	char buffer[1024];
	struct sockaddr_in serverAdd;
	struct sockaddr_storage serverStorage, socklen_t addr_size;

	//server settings
	socket_desc = socket(AF_INET, SOCK_STREAM, 0);
	serverAdd.sin_family = AF INET;
	serverAdd.sin_port = htons(8888);
	serverAdd.sin_addr.s_addr = inet_addr("192.168.56.104") ;
	memset(serverAdd.sin_zero,'\0', sizeof serverAdd.sin_zero);
	bind(socket_desc, (struct sockaddr * ) &serverAdd, sizeof (serverAdd)) ;
	
	//server listen
	if (listen(socket_desc,5) == 0){
	puts ("\n############## WELCOME TO SERVER AF CHATROOM ##############");
	puts ("                 Server is Listening... \n"); 
	}
	
	else
		puts ("Error"); 
	
	//Bind 1 server, 2 clients
	addr_size = sizeof serverStorage;
	Client1 = accept(socket_desc, (struct sockaddr *) &serverStorage, &addr size);
	Client2 = accept(socket_desc, (struct sockaddr *) &serverStorage, &addr size);

	int exit = 0;
	
	//Function where disconnect when client type "exit"
	while (exit == 0){
		
		receive (Client1, buffer, 1024, 0); //receive message from Clienti
		printf ("%s\n  --Send to Client2--\n", buffer); //send msg to Client2
		send (Client2, buffer, 1024, 0);
		
		//Exit the looping if Client1 type "exit"
		if (compare strings(buffer, "exit") == 0) {
			
			exit = 1;
		}
		
		//Empty the buffer
		memset(&buffer[0], 0, sizeof(buffer));
		receive(Client2, buffer, 1024, 0); //receive message from Client2
		printf ("%s\n --Send to Client1--\n", buffer); //send mesasge to ClientI
		send (Client1, buffer, 1024, 0);
		
		//Exit the looping if Client2 type "exit
		if (compare strings (buffer, "exit")==0){
			
			exit - 1;
		}
	}
			return 0;
}
