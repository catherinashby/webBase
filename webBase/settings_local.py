#    local development settings
LOCAL_SETTINGS = True
from .settings import *  # @UnusedWildImport

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
#    EMAIL_HOST = 'edgsmtp.broadridge.net'    #    devnet mail server

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

ALLOWED_HOSTS = []

#STATIC_ROOT = None
#MEDIA_ROOT = os.path.join( 'C:', os.path.sep, 'Temp', 'webBase' )

SITE_ID = 101
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

CONFIGURATION_DIRECTORY = os.path.join( 'C:', os.path.sep, 'localWork', 'deploy', 'webBase' )
LOCAL_APPS = []
LOCAL_ROUTERS = []
