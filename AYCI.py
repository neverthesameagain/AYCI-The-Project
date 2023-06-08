import subprocess
import os
if not os.path.exists("myenv"):
    os.system('cmd /c "pip install virtualenv & virtualenv myenv')

subprocess.call(["python","setup.py"])