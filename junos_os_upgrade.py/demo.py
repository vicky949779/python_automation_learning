# from jnpr.junos import Device  # type: ignore
# from jnpr.junos.exception import ConnectError  # type: ignore
# from lxml import etree  # type: ignore # Required for XML parsing
# import getpass  # For secure password input

# def execute_rpc_commands(dev, commands):
#     """
#     Executes a list of Junos RPC or CLI commands and prints the output.
#     """
#     for cmd in commands:
#         try:
#             print(f"\n🔹 Executing: {cmd['description']}")
            
#             if cmd['method'] == 'cli':
#                 output = dev.cli(cmd['args']['command'])
#             else:
#                 rpc_method = getattr(dev.rpc, cmd['method'])
#                 output = rpc_method(**cmd.get('args', {}))
#                 output = etree.tostring(output, pretty_print=True).decode()
            
#             print(output)

#         except Exception as err:
#             print(f"❌ Error executing '{cmd['description']}': {err}")

# def os_upgrade():
#     """
#     Connects to a Junos device via SSH, runs pre-check commands,
#     and retrieves software version using RPC.
#     """
#     host = input("🔹 Enter device IP/Hostname: ")
#     username = input("🔹 Enter username: ")
#     password = getpass.getpass("🔹 Enter password: ")  # Secure password input

#     # Define RPC and CLI commands to execute
#     rpc_commands = [
#         {
#             'description': 'Show version',
#             'method': 'get_software_information',
#             'args': { 'format': 'text'}
#             # 'cli_fallback': 'show version'
#         },
#         {
#             'description': 'Show interfaces terse',
#             'method': 'get_interface_information',
#             'args': {'terse': True,'format': 'text' },
#             # 'cli_fallback': 'show interfaces terse'
#         },
#         {
#             'description': 'Show LLDP neighbors',
#             'method': 'get_lldp_neighbors_information',
#             # 'cli_fallback': 'show lldp neighbors'
#             'args': { 'format': 'text'}
#         },
#         {
#             'description': 'Show virtual-chassis',
#             'method': 'get_virtual_chassis_information',
#             # 'cli_fallback': 'show virtual-chassis',
#             'args': { 'format': 'text'}
#         },
#         {
#             'description': 'Show interfaces description',
#             'method': 'cli',
#             'args': {'command': 'show configuration interfaces | match description','format': 'text'},
#             # 'cli_fallback': 'show configuration interfaces | match description'
#         }
#     ]

#     # Use 'with' to manage device connection automatically
#     try:
#         with Device(host=host, user=username, passwd=password) as dev:
#             print(f"\n🔌 Connecting to {host}...")
#             print("✅ Connection successful!\n")

#             # Run pre-check RPC commands
#             print("📢 Running pre-check commands...")
#             execute_rpc_commands(dev, rpc_commands)

#     except ConnectError as err:
#         print(f"❌ Connection failed: {err}")
#     except Exception as err:
#         print(f"❌ Unexpected error: {err}")

# # Run the function
# os_upgrade()

#############################################################################

from jnpr.junos import Device  # type: ignore
from jnpr.junos.exception import ConnectError, RpcError  # type: ignore
from lxml import etree  # type: ignore
import getpass  # Secure password input

# Output file names
PRECHECK_OUTPUT_FILE = "precheck_outputs.txt"
POSTCHECK_OUTPUT_FILE = "postcheck_outputs.txt"

def run_checks(dev, commands, phase):
    """
    Executes CLI and RPC commands and saves the exact Junos output to a text file.
    """
    output_file = PRECHECK_OUTPUT_FILE if phase == "pre-check" else POSTCHECK_OUTPUT_FILE

    with open(output_file, "w") as file:  # Overwrites file for each run
        for cmd in commands:
            try:
                print(f"\n🔹 Executing {phase}: {cmd['description']}")

                if cmd['method'] == 'cli':
                    output = dev.cli(cmd['args']['command'])  # CLI output as-is
                else:
                    rpc_method = getattr(dev.rpc, cmd['method'])
                    response = rpc_method(**cmd.get('args', {}))
                    output = etree.tostring(response, pretty_print=True, encoding="unicode")  # Ensure formatted XML output  

                # Write output exactly as it appears on Junos device
                file.write(f"\n===== {cmd['description']} ({phase}) =====\n")
                file.write(output + "\n")

                print(output)  # Print the exact same output

            except RpcError as rpc_err:
                print(f"❌ RPC Error executing '{cmd['description']}': {rpc_err}")
            except Exception as err:
                print(f"❌ Error executing '{cmd['description']}': {err}")

    print(f"\n📄 Successfully executed {phase} results saved in '{output_file}'")

def os_upgrade():
    """
    Connects to a Junos device via SSH, runs pre-check commands, 
    performs the upgrade (placeholder), and then runs post-check commands.
    """
    host = input("🔹 Enter device IP/Hostname: ")
    username = input("🔹 Enter username: ")
    password = getpass.getpass("🔹 Enter password: ")  # Secure password input

    # Define CLI & RPC commands
    commands = [
        {'description': 'Show version', 'method': 'get_software_information'},
        {'description': 'Show interfaces terse', 'method': 'get_interface_information', 'args': {'terse': True}},
        {'description': 'Show LLDP neighbors', 'method': 'get_lldp_neighbors_information'},
        {'description': 'Show virtual-chassis', 'method': 'get_virtual_chassis_information'},
        # {'description': 'Show interfaces description', 'method': 'cli', 'args': {'command': 'show interfaces description'}},
        {'description': 'Show interfaces description', 'method': 'get_interface_information', 'args': {'descriptions': True}},
        {'description': 'Show Ethernet Switching Table', 'method': 'get_ethernet_switching_table_information'}
    ]

    try:
        with Device(host=host, user=username, passwd=password) as dev:
            print(f"\n🔌 Connecting to {host}...")
            print("✅ Connection successful!\n")

            # Run pre-checks
            print("📢 Running PRE-CHECK commands...")
            run_checks(dev, commands, phase="pre-check")

            # Placeholder for upgrade process
            print("\n🚀 Performing OS upgrade... (Add actual upgrade logic here)")
            # Add upgrade logic here

            # Run post-checks
            print("\n📢 Running POST-CHECK commands...")
            run_checks(dev, commands, phase="post-check")

    except ConnectError as err:
        print(f"❌ Connection failed: {err}")
    except Exception as err:
        print(f"❌ Unexpected error: {err}")

# Run the function
os_upgrade()
