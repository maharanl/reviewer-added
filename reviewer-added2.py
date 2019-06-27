#  reviewer-added --change <change id> --change-url <change url> --change-owner <change owner> --change-owner-username <username> --project <project name> --branch <branch> --reviewer <reviewer> --reviewer-username <username>
import argparse
import os
import sys
import requests
import json

'''if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run ./build when present.')
    parser.add_argument('--project', metavar='PROJECT_NAME', required=True)  # project/name.git
    parser.add_argument('--refname', required=True)  # refs/heads/master
    parser.add_argument('--uploader', required=True)  # Werner Beroux (werner@beroux.com)
    parser.add_argument('--oldrev', metavar='SHA1', required=True)
    parser.add_argument('--newrev', metavar='SHA1', required=True)
    args = parser.parse_args()

    gerrit_site = os.environ['GERRIT_SITE']
    gerrit_tmp = os.environ['GERRIT_TMP']
    git_dir = os.environ['GIT_DIR']

    # Debug output:
    print('--project=' + args.project)
    print('--refname=' + args.refname)
    print('--uploader=' + args.uploader)
    print('--oldrev=' + args.oldrev)
    print('--newrev=' + args.newrev)
    print('GERRIT_SITE=' + gerrit_site)
    print('GERRIT_TMP=' + gerrit_tmp)
    print('GIT_DIR=' + git_dir)
'''

