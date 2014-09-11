from github import Github
import sys

if len(sys.argv) < 3:
    print "command <username> <password> <githubrepo>\n"
    print "command liam-middlebrook ****** repouser/testRepo"
    exit()

g = Github(sys.argv[1], sys.argv[2])

body = """
First, the standard disclaimer: I am not a lawyer, and this does not constitute legal or financial advice.

Generally, IMHO, it is a good idea to use FSF or OSI Approved Licenses (which can be found here https://www.gnu.org/licenses/licenses.html and here http://opensource.org/licenses/category)

The Free Software Foundation has a useful guide for choosing a license: https://www.gnu.org/licenses/license-recommendations.html

I often reference the Software Freedom Law Center's Legal Primer for both practical and academic purposes (highly recommended): https://www.softwarefreedom.org/resources/2008/foss-primer.html#x1-60002.2

https://tldrlegal.com/ is quite a useful resource for comparing the various FOSS licenses out there once you have some context

To get ahold of actual lawyers/advisors who help FOSS projects, you can reach out to the FSF, SFLC, and OSI at:
licensing@fsf.org
help@softwarefreedom.org
license-discuss@opensource.org

Hope this helps, and happy hacking!
"""

repo = g.get_repo(sys.argv[3])
repo.create_issue("Missing LICENSE?", body)

print "Issue Created at repo: " + sys.argv[3]
