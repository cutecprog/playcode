#--------------------------------------------------------------------
# Makefile
#
# author:   (Andrew) Scott Grooms
# course:   COSC2425
# date:     Feb 9, 2010
#--------------------------------------------------------------------

FIRSTNAME   =   Scott
LASTNAME    =   Grooms

LAB         =   4
PROJECT     =   jumpTable

TOOLS       = /tools/bin
CLIB        = /tools/lib
MINGWDIR    = /tools/MinGW/bin
NASMDIR     = /tools/NASM

ASM         = $(NASMDIR)/nasm.exe 
GCC         = $(MINGWDIR)/gcc.exe
LINK        = $(MINGWDIR)/gcc.exe
ZIP         = $(TOOLS)/zip.exe
RM          = $(TOOLS)/rm.exe
DEBUG       = $(TOOLS)/ollydbg.exe


FILES       =  $(PROJECT).asm \
                Makefile


all:        $(PROJECT).exe

$(PROJECT).obj:       $(PROJECT).asm
	$(ASM)-f win32 $(PROJECT).asm

$(PROJECT).exe:     $(PROJECT).obj
	$(LINK) $(PROJECT).obj /tools/lib/COSC2425lib.a -o $(PROJECT).exe
	
clean:
	$(RM)   \*.exe \*.obj

zip:    $(FILES)
	$(ZIP) Lab$(LAB)_$(FIRSTNAME)_$(LASTNAME) $(FILES)
		
debug:      $(PROJECT).exe
	$(DEBUG) $(PROJECT).exe



