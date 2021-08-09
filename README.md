A tool that will gather information about an IP.

You'll need to create an account on https://ipinfo.io/.

After that you can copy your token that you'll need for the script to run.

Usage:

	Step 1 -  python3 input_ipinfo.py
	
	Step 2 - Insert your token
	
	Step 3 - Insert an IP
	

After executing the script it will be created a .json file with the information gathered.

The information in the file will have this structure:

	{
		"Result": [
		    {
		        "ip": "X.X.X.X",
		        "city": "X",
		        "region": "X",
		        "country": "X",
		        "loc": "XX.XXXX,-XXX.XXXX",
		        "postal": "X",
		        "timezone": "X",
		        "hosting_provider": "X",
		        "reverse_dns": "X"
		    }
		]
	}


