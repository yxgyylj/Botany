# Redifine the path
XIGE_LIB = /home/yang.2677/local/sundials/lib 
INCLUDES = -I. -I/home/yang.2677/local/sundials/include
LIBS = -L/usr/lib64/ -L$(XIGE_LIB)
# CLINKS = -lsundials_cvode -lsundials_nvecserial -lm
# CPPLINKS = -lm

CXX = gcc
CPPXX = g++
CFLAG = $(INCLUDES) -std=c99
CPPFLAG = -std=c++11

COBJ = BC_main.c
CPPOBJ = BC_main.cpp 	
	 
RM = /bin/rm -f

# -----------------------------------------------------------------

default: cpp

c:    $(COBJ)
	$(CXX) $(CFLAG) -o a_c $(COBJ) $(LIBS) $(CLINKS)

cpp:    $(CPPOBJ)
	$(CPPXX) $(CPPFLAG) -o a_cpp $(CPPOBJ) $(LIBS) $(CLINKS)
 
clean:
	$(RM) *.o *~ a_* Data/* 
