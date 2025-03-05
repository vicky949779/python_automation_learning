''' Package and Module Names
------------------------------------------
Modules (Python files): Use short, lowercase names. Underscores only if needed.

✅ network.py
✅ network_utils.py (if needed for clarity)
Packages (folders): Use short, lowercase names. Avoid underscores.

✅ mypackage
C/C++ Extension Modules: Start with an underscore if there's a Python wrapper.

✅ _socket (C module) → socket (Python wrapper)
'''

from .password_gen import user_cmd_gen, users_cmd_gen
from .cisco_task import cisco_cmd_executor # type: ignore
# from .cisco_task import cisco_cmd_executor

