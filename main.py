from Tkinter import Tcl

MYFILE = '/home/trond/Downloads/script.ps1'
tcl = Tcl()
# Execute proc main from foo.tcl with MYFILE as the arg
tcl.eval('source /home/trond/Documents/winrmrunner.tcl')
tcl_str = tcl.eval('main %s' % MYFILE)


# Access the contents of a Tcl variable, $tclVar from python
#tcl.eval('set tclVar foobarme')
#tclVar = tcl.eval('return $tclVar')