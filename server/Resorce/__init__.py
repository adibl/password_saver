import sys

sys.path.insert(0, "D:/adi/Documents/password_saver/server/Resorce")  # FIXME: make this unesesery

from API import handle_client as process_request
import database
from validate import ValidateResorce
