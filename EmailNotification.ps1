

$client_path = "C:\Users\xxxx\Desktop\*.txt"
$server_path = "C:\Users\xxxx\Desktop\projects"

# all *.pdf from a to b


Copy-Item -Path $client_path -Destination $server_path -Recurse -Force


$server_path = "c:/users/xxxx/desktop/projects"

if(Test-Path $server_path ){
    $file = (Get-ChildItem $client_path | Measure-Object).Count
    $sender_email = "xxxxxxxxxxx"
    $recipient_email = "xxxxxxxxxxx"
    $Subject = "xxxxxxxxx"
    $Body = "The files has been moved. The folder contains $file files"
    
    $SmtpServer = "smtp.gmail.com"
    $SmtpClient = New-Object Net.Mail.SmtpClient($SmtpServer, 587)
    
    
    $SmtpClient.EnableSsl = $true
    $SmtpClient.Credentials = New-Object System.Net.NetworkCredential("xxxxxxxx","xxxxxxxxx")
    $SmtpClient.Send($sender_email, $recipient_email, $Subject, $Body)

}else {
    echo "file cannot be move"
}



