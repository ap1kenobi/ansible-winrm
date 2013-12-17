#$myarg = $args[0]
#new-item "C:\Imaginaryfile.txt" -itemtype File
remove-item "C:\Imaginaryfile.txt" -force -errorvariable myerrvar -erroraction 0

Write-host "AnsibleResult:Changed"
Write-host "AnsibleDetail:Deleted file $myarg"
Write-host "AnsibleError:$myerrvar"
