from pymetasploit3.msfrpc import MsfRpcClient

def search_modules(client, service=None, version=None, cve=None):
    matching_modules = []

    # Get all exploit modules
    exploits = client.modules.exploits

    # Iterate over each exploit module
    for exploit in exploits:
        # Check if the module matches the criteria
        if (not service or service in exploit) and \
           (not version or version in exploit) and \
           (not cve or cve in exploit):
            matching_modules.append(exploit)
    
    return matching_modules

def test_msfrpc_connection():
    try:
        # Connect to the Metasploit RPC server
        client = MsfRpcClient(password="abc123", port=55552, ssl=True)

        # Test if the connection is successful
        if client.login('msf', 'abc123'):
            print("Successfully connected to the Metasploit RPC server!")
            # Get user input for search criteria
            service = input("Enter the service name (e.g., SMB): ")
            version = input("Enter the version (e.g., 1.0): ")
            cve = input("Enter the CVE number (e.g., CVE-2022-1234): ")
            # Search for modules
            matching_modules = search_modules(client, service=service, version=version, cve=cve)
            if matching_modules:
                print("Found matching modules:")
                for module in matching_modules:
                    print(module)
            else:
                print("No matching modules found.")
        else:
            print("Failed to authenticate with the Metasploit RPC server.")
    except Exception as e:
        print("Error connecting to the Metasploit RPC server:", e)

# Test the connection
test_msfrpc_connection()
