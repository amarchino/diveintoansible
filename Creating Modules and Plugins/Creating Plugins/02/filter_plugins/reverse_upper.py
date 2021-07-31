# (c) 2012, Jeroen Hoekx <jeroen@hoekx.be>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Make coding more python3-ish
__metaclass__ = type

from ansible.module_utils._text import to_text

def reverse_upper(string):
    ''' Reverse and upper string '''
    string = to_text(string, errors='surrogate_or_strict', nonstring='simplerepr')
    return string[::-1].upper()

class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'reverse_upper': reverse_upper
        }
