import os
import sys
from musixmatch2 import Musixmatch
musixmatch = Musixmatch('437f020971788f570fb9683878c740e8')

print musixmatch.track_get(15445219)