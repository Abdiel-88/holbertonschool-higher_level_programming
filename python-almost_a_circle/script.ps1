# git_push_script.ps1

# Read the name of the file
$file = Read-Host -Prompt "Enter the name of the file"

# Read the commit message
$message = Read-Host -Prompt "Enter the commit message"

# Git commands
git add $file
git commit -m $message
git push
