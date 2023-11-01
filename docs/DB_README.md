<h2>Install the Microsoft ODBC driver for SQL Server (Linux)</h2>
<ol>
	<li>
        <p>Create a file.sh with the following code:</p>
        <pre>
#!/bin/bash
<span></span>
if ! [[ "18.04 20.04 22.04 23.04" == *"$(lsb_release -rs)"* ]];
then
    echo "Ubuntu $(lsb_release -rs) is not currently supported.";
    exit;
fi
<span></span>
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
<span></span>
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
<span></span>
sudo apt-get update
<span># optional: for bcp and sqlcmd</span>
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18
echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
source ~/.bashrc
<span># optional: for unixODBC development headers</span>
sudo apt-get install -y unixodbc-dev
        </pre>
	</li>
    <br>
    <li>
        <p>Give the file permission to execute:</p>
        <code>chmod 700 file.sh</code>
    </li>
    <br>
    <li>
        <p>Run the script</p>
        <code>sudo ./file.sh</code>
    </li>
</ol>
<h2>Install the Microsoft ODBC driver for SQL Server (Windows)</h2>
<ol>
    <li>
        <p>Click on the desired link to get the installer:</p>
        <code><a href="https://go.microsoft.com/fwlink/?linkid=2249006">Download Microsoft ODBC Driver 18 for SQL Server (x64)</a></code>
        <p>or</p>
        <code><a href="https://go.microsoft.com/fwlink/?linkid=2249005">Download Microsoft ODBC Driver 18 for SQL Server (x86)</a></code>
    </li>
</ol>