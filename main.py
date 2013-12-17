import subprocess


PSSCRIPTFILE = '/home/trond/Documents/ansible-winrm/script.ps1'
PSHOSTNAME = "192.168.188.155"
PSUSERNAME = "Administrator"
PSPASSWORD = "Co0lip1.12"
proc = subprocess.Popen(['/opt/ActiveTcl-8.6/bin/tclsh', '/home/trond/Documents/ansible-winrm/winrmrunner.tcl', PSSCRIPTFILE,PSHOSTNAME, PSUSERNAME, PSPASSWORD], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#RESULT = subprocess.call(['/opt/ActiveTcl-8.6/bin/tclsh', '/home/trond/Documents/ansible-winrm/winrmrunner.tcl', PSSCRIPTFILE,PSHOSTNAME, PSUSERNAME, PSPASSWORD ])
#subprocess.check_output(['/opt/ActiveTcl-8.6/bin/tclsh', '/home/trond/Documents/ansible-winrm/winrmrunner.tcl', PSSCRIPTFILE,PSHOSTNAME, PSUSERNAME, PSPASSWORD ])

out, err = proc.communicate()
outtext = out.rstrip()
outtext = outtext.strip()

print 'stdout:', outtext


#RESULT = "Fake"
#print RESULT

if outtext == 'Changed':
    print 'Changed stuff'
elif outtext == 'Unchanged':
    print 'Did not change stuff'
else:
    print "Not sure what we did"


#tcl = Tcl()
# Execute proc main from foo.tcl with MYFILE as the arg
#tcl.eval('source /home/trond/Documents/ansible-winrm/winrmrunner.tcl')
#tcl_str = tcl.eval('main %s' % MYFILE)


# Access the contents of a Tcl variable, $tclVar from python
#tcl.eval('set tclVar foobarme')
#tclVar = tcl.eval('return $tclVar')