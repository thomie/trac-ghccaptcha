version = '0.1'
url = "https://github.com/thomie/trac-ghccaptcha"

import random

from trac.core import Component, implements
from tracspamfilter.captcha import ICaptchaMethod

CHALLENGES = [
    ('glasgow', "What does the letter 'G' stand for in GHC? (all lowercase)"), 
    ('haskell', "What does the letter 'H' stand for in GHC? (all lowercase)"), 
    ('compiler', "What does the letter 'C' stand for in GHC? (all lowercase)"),
]

class GhcCaptcha(Component):
    implements(ICaptchaMethod)

    def generate_captcha(self, req):
        return random.choice(CHALLENGES)

    def verify_captcha(self, req):
        return False

    def is_usable(self, req):
        return True