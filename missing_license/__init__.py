import sys

from github import Github
import click

issue_body = """
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

@click.command()
@click.option('--username', help='GitHub Username', prompt='Username: (testUser)')
@click.option('--repo', help='GitHub Repo That is Missing License',
               prompt='Repo: (testUser/myRepo)')
@click.option('--password', prompt=True,
               hide_input=True, confirmation_prompt=True,
	       help='Your GitHub Password')
def create_issue(username, repo, password):
   g = Github(username, password)


   gitRepo = g.get_repo(repo)
   gitRepo.create_issue("Missing LICENSE?", issue_body)

   print "Issue Created at repo: " + repo

if __name__ == '__main__':
    create_issue()
